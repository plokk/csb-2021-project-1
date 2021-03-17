from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add-credit-card/', views.add_credit_card, name='add_credit_card'),
    path('profile/<int:user_id>', views.profile, name='profile'),
]
