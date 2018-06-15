from django.urls import path
from django.contrib import admin
from blog import views

urlpatterns = [
    path('test-delete/', views.test_delete, name='test_delete'),
    path('test-session/', views.test_session, name='test_session'),
    path('', views.post_list, name='post_list2'),
    path('save-session-data/', views.save_session_data, name='save_session_data'),
    path('access-session-data/', views.access_session_data, name='access_session_data'),
    path('delete-session-data/', views.delete_session_data, name='delete_session_data'),
    path('track_user/', views.track_user, name='track_user'),
    path('stop-tracking/', views.stop_tracking, name='stop_tracking'),
	path('cookie/', views.test_cookie, name='cookie'),
	path('<int:pk>/<slug:post_slug>/', views.post_detail, name='post_detail'),
	path('category/<slug:category_slug>/', views.post_by_category, name='post_by_category'),
    path('tag/<slug:tag_slug>/',views.post_by_tag, name='post_by_tag'),
    path('lousy-login/', views.lousy_login, name='lousy_login'),
    path('lousy-secret/', views.lousy_secret, name='lousy_secret'),
    path('lousy-logout/', views.lousy_logout, name='lousy_logout'),
    path('login/', views.login, name='blog_login'),
    path('logout/', views.logout, name='blog_logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
]