from django.urls import path, include
from users.views import dashboard, register, emailsending
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    # path('accounts/password_change/', auth_views.LoginView.as_view(template_name='custom_template.html')),
    path('', dashboard, name="dashboard"),
    path('register/', register, name="register"),
    path('email/', emailsending, name="emailsending"),
]
