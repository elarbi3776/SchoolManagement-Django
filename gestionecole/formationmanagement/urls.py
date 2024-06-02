
from django.contrib import admin
from django.urls import path
from formation import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path('customer/',include('customer.urls')),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='formation/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    
    path('adminlogin', LoginView.as_view(template_name='formation/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('admin-course', views.admin_course_view,name='admin-course'),
    path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('admin-update-course', views.admin_update_course_view,name='admin-update-course'),
    path('update-course/<int:pk>', views.update_course_view,name='update-course'),
    path('admin-delete-course', views.admin_delete_course_view,name='admin-delete-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),

    path('admin-view-course-holder', views.admin_view_course_holder_view,name='admin-view-course-holder'),
    path('admin-view-approved-course-holder', views.admin_view_approved_course_holder_view,name='admin-view-approved-course-holder'),
    path('admin-view-disapproved-course-holder', views.admin_view_disapproved_course_holder_view,name='admin-view-disapproved-course-holder'),
    path('admin-view-waiting-course-holder', views.admin_view_waiting_course_holder_view,name='admin-view-waiting-course-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),

]
