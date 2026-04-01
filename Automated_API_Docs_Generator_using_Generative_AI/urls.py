from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as mainView
from admins import views as admins
from users import views as usr

urlpatterns = [

    # ---------------- ADMIN PANEL ---------------- #
    path('admin/', admin.site.urls),

    # ---------------- MAIN ---------------- #
    path("", mainView.index, name="index"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),

    # ---------------- ADMIN FEATURES ---------------- #
    path("AdminHome/", admins.adminHome, name="AdminHome"),
    path("adminlogin/", admins.adminLoginCheck, name="AdminLoginCheck"),

    path("users-list/", admins.RegisterUsersView, name="view_users"),
    path("activate/<int:id>/", admins.activateUser, name="activate_user"),
    path("deactivate/<int:id>/", admins.DeactivateUsers, name="deactivate_user"),
    path("delete-user/<int:id>/", admins.deleteUser, name="delete_user"),

    # ---------------- USER FEATURES ---------------- #
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("register/", usr.UserRegisterActions, name="register"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),

    # ---------------- TRANSLATION ---------------- #
    path("translate/", usr.TranslateQuestionPaper, name="Translate"),

    # ---------------- HISTORY ---------------- #
    path("history/", usr.UserHistory, name="history"),
    path("delete-history/<int:id>/", usr.DeleteHistory, name="delete_history"),

    path("logout/", usr.logoutUser, name="logout"),
]

# ---------------- MEDIA FILES ---------------- #
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   