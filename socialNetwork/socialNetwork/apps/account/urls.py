from django.urls import path
from django.contrib.auth import views as standart_views
from .views import *

app_name = 'account'
urlpatterns = [
    path('account/', user_account, name = 'user_account'),
    path('account_setting/', account_setting, name = 'account_setting'),
    path('friends/', friends, name = 'friends'),
    path('friend_request/', friend_request, name = 'friend_request'),
    path('id<int:account_id>/add_friend', add_friend, name = 'add_friend'),
    path('id<int:account_id>/add_follower', add_follower, name = 'add_follower'),
    path('confirm_friend<int:account_id>/', confirm_friend, name = 'confirm_friend'),
    path('delete_friend<int:account_id>/', delete_friend, name = 'delete_friend'),
    path('delete_follower<int:account_id>/', delete_follower, name = 'delete_follower'),
    path('users/', find_users, name = 'find_users'),
    path('id<int:account_id>/', account, name = 'account'),
    ]
