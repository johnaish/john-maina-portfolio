from django.urls import path
from . import views
from . import views_admin

urlpatterns = [
    path('admin-login/', views_admin.user_login, name='admin_login'),
    path('admin-logout/', views_admin.user_logout, name='admin_logout'),
    path('dashboard/', views_admin.dashboard, name='dashboard'),
    path('dashboard/project/new/', views_admin.create_project, name='create_project'),
    path('dashboard/post/new/', views_admin.create_post, name='create_post'),
    path('dashboard/project/<int:pk>/edit/', views_admin.edit_project, name='edit_project'),
    path('dashboard/project/<int:pk>/delete/', views_admin.delete_project, name='delete_project'),
    path('dashboard/post/<int:pk>/edit/', views_admin.edit_post, name='edit_post'),
    path('dashboard/post/<int:pk>/delete/', views_admin.delete_post, name='delete_post'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
