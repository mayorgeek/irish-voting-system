"""votingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.student_login, name="student_login"),
    path('student/register/', views.student_register, name="student_register"),
    path('admin/login/', views.admin_login, name="admin_login"),
    path('admin/register/', views.admin_register, name="admin_register"),
    path('admin/', views.account_page, name="account_page"),
    path('admin/start-voting/', views.start_voting, name="start_voting"),
    path('admin/view-all-voting/', views.view_all_voting, name="view_all_voting"),
    path('admin/add-new-candidate/', views.add_new_candidate, name="add_new_candidate"),
    path('admin/view-all-candidates/', views.view_all_candidates, name="view_all_candidates"),
    path('admin/view-all-results/', views.view_all_results, name="view_all_results"),
    path('admin/view-all-students/', views.view_all_students, name="view_all_students"),
    path('voting-page/', views.voting_page, name="voting_page"),
]
