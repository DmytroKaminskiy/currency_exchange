from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View, ListView, TemplateView

from account.forms import SignUpForm
from account.models import User, Contact, ActivationCode
from account.tasks import send_tel_message
from currency.models import Rate


def smoke(request):
    return HttpResponse('smoke')


# def my_profile(request):
#     return render(request, 'my_profile.html')

class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('email', )
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


class ContactUs(CreateView):
    template_name = 'my_profile.html'
    queryset = Contact.objects.all()
    fields = ('email', 'title', 'body')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        #### send email
        print(self.object)
        # send_email_async.delay()
        return response


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class Activate(View):
    def get(self, request, activation_code):
        ac = get_object_or_404(
            ActivationCode.objects.select_related('user'),
            code=activation_code, is_activated=False,
        )

        if ac.is_expired:
            raise Http404

        ac.is_activated = True
        ac.save(update_fields=['is_activated'])

        user = ac.user
        user.is_active = True
        user.save(update_fields=['is_active'])

        ### SEND MESSAGE
        # send_tel_message()
        send_tel_message.delay()

        return redirect('index')


from django_filters.views import FilterView
from account.filters import RateFilter


class RatesList(FilterView):
    filterset_class = RateFilter
    queryset = Rate.objects.all()
    template_name = 'rates.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        from urllib.parse import urlencode
        context = super().get_context_data(*args, **kwargs)

        query_params = dict(self.request.GET.items())
        if 'page' in query_params:
            del query_params['page']
        context['query_params'] = urlencode(query_params)

        return context

    # @property
    # def template_name(self):

    # @property
    # def paginate_by(self):
    #     paginate = int(self.request.GET.get('paginate-by'))
    #     return paginate


class LatestRates(TemplateView):
    template_name = 'latest-rates.html'

    def get_context_data(self, **kwargs):
        from currency import model_choices as mch
        from django.core.cache import cache

        context = super().get_context_data(**kwargs)
        # rates = {
        #     'privatBank': [Rate.objects.filter(source=mch.SR_PRIVAT, currency=mch.CURR_USD).last(),
        #                    Rate.objects.filter(source=mch.SR_PRIVAT, currency=mch.CURR_EUR).last()],
        #     'MonoBank': [Rate.objects.filter(source=mch.SR_MONO, currency=mch.CURR_USD).last(),
        #                    Rate.objects.filter(source=mch.SR_MONO, currency=mch.CURR_EUR).last()]
        # }

        rates = []
        for bank in mch.SOURCE_CHOICES:
            source = bank[0]
            for curr in mch.CURRENCY_CHOICES:
                currency = curr[0]
                from currency.utils import generate_rate_cache_key
                cache_key = generate_rate_cache_key(source, currency)

                rate = cache.get(cache_key)

                if rate is None:
                    rate = Rate.objects.filter(source=source, currency=currency).order_by('created').last()
                    if rate:
                        rate_dict = {
                            'currency': rate.currency,
                            'source': rate.source,
                            'sale': rate.sale,
                            'buy': rate.buy,
                            'created': rate.created,
                        }
                        rates.append(rate_dict)
                        cache.set(cache_key, rate_dict, 60 * 15)  # 15 minutes
                        # cache.set(cache_key, rate_dict, 5)  # 5 seconds
                else:
                    rates.append(rate)

        context['rates'] = rates
        # Rate.objects.filter(source=mch.SR_PRIVAT, currency=mch.CURR_USD).order_by('-created')[0]
        return context

'''
source PrivatBank - latest USD, latest UER
source MonoBank - latest USD, latest UER
'''
