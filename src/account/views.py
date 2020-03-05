from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from account.models import User, Contact


def smoke(request):
    return HttpResponse('smoke')


# def my_profile(request):
#     return render(request, 'my_profile.html')

class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = User.objects.filter(is_active=True)
    fields = ('email', )
    success_url = reverse_lazy('index')


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
