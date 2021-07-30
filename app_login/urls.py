from django.urls import path
from app_login import views



app_name ='app_login'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('user_profile_change/', views.user_profile_change, name='user_profile_change'),
    path('password/', views.password_change, name='password_change'),
    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('change_profile_pic/',views.change_profile_pic, name='change_profile_pic')
   

]

