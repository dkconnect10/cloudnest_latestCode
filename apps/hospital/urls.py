from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateHospital.as_view(), name='hospital-create'),
    path('list/', HospitalListOrDetailView.as_view(), name='hospital-list-or-detail'),
    path('update/', UpdateHospital.as_view(), name='hospital-update'),
    path('delete/<int:hospital_id>/', DeleteHospital.as_view(), name='hospital-delete'),
    path('toggle-status/<int:hospital_id>/', ToggleHospitalStatus.as_view(), name='hospital-toggle-status'),
    path('user-create/', HospitalUserCreate.as_view(), name='hospital-user-create'),
    path('get-users-and-roles/<int:hospital_id>/', GetUserAndRole.as_view(), name='get-users-and-roles'),
    path('assign-role-to-hospital/', AssignUserRoleToHospital.as_view(), name='assign-role-to-hospital'),
]
