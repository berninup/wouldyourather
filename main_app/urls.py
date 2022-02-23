from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('questions/', views.question_index, name='index'),
    path('questions/<int:question_id>/', views.question_detail, name='detail'),
    path('questions/<int:question_id>/votes', views.question_vote, name='vote'),
    path('questions/<int:question_id>/vote', views.vote, name='vote'),
    path('questions/create/', views.WouldYouRatherCreate.as_view(), name='question_create'),
]