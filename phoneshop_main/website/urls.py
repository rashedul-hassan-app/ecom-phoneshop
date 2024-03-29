from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.RobotsTxtView, name='robots'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('add_product', views.add_product, name='add_product'),
    path('newsletters/', views.newsletters, name='newsletters'),
    path('newsletters/send/', views.send_newsletters, name='send_newsletters'),
]

handler404 = 'website.views.error_404_view'
