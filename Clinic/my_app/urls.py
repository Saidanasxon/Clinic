from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.log_in, name='login'),
    # path('logout/', views.log_out, name='logout'),
    path('error_404/', views.error_404, name='error_404'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('feature/', views.feature, name='feature'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('vaqt_add/', views.vaqt_add, name='vaqt_add'),

]
