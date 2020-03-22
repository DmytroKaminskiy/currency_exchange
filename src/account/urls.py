from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('smoke/', views.smoke, name='smoke'),
    path('profile/<int:pk>/', views.MyProfile.as_view(), name='my-profile'),
    path('contact-us/', views.ContactUs.as_view(), name='contact-us'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('activate/<uuid:activation_code>/', views.Activate.as_view(), name='activate'),
]
