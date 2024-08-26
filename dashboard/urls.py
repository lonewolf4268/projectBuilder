from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='dashboard'),
    path('home/', views.home_view, name='home'),
    path('service/', views.service_view, name='service'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.blog_view, name='blog'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('about/', views.about_view, name='about'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

]