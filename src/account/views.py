from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View, ListView

from account.forms import SignUpForm
from account.models import User, Contact, ActivationCode
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
        return redirect('index')


from django_filters.views import FilterView
from account.filters import RateFilter


class RatesList(LoginRequiredMixin, FilterView):
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
