from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView, name='payments_home'),
    path('config/', views.stripe_config, name='stripe_config'),
    path('create-checkout-session/', views.create_checkout_session,
         name='create_checkout_session'),
    path('success/', views.success, name='payment_success'),
    path('cancelled/', views.cancelled, name='payment_cancelled'),
]
