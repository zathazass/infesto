from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import GeneratePDF

urlpatterns = [
    path('pdf/',GeneratePDF.as_view(),name="pdf"),
    path('events/',views.events,name="events"),
    path('register_list/',views.register_list,name="register_list"),
    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('home/',views.home_view,name="new_home"),
    path('logout/',views.logout_view,name="logout"),
    path('profile/',views.profile,name='profile'),
    path('profile_edit/',views.profile_edit,name='profile_edit'),
    path('about/',views.about,name="about"),
    #Reset Password urlpatterns
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'),name="password_change"),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name="password_change_done"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html'),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),

]
