from django.urls import path
from apps.authentication import views

urlpatterns=[
     path('activate/<uidb64>/<token>/',views.activate_account, name='activate'),
     path('password-reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
     path('supplier-register/',views.SupplierRegister.as_view(), name='supplier_register'),
     path('login/',views.login_request, name='login'),
     path('forgot-password/', views.forgot_password, name='forgot_password'),
     path('logout/',views.logout_view, name='logout'),
     path("staffs/add/", views.add_staff_user, name="add_staff_user"),
     path("staffs/invitation/<uidb64>/", views.staff_invite_setup, name="setup_invite_account"),
     path("staffs/invitation/decline/<str:uuid>/", views.reject_staff_invitation, name="reject_invite"),
     path("staffs/invitation/accept/<str:uuid>/", views.CreateStaffUser.as_view(), name="accept_invite"),
]
