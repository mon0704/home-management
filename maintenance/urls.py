from django.urls import path
from .views import MaintenanceRequestList, MaintenanceRequestDetail

urlpatterns = [
    path('maintenance/', MaintenanceRequestList.as_view(), name='maintenance-list'),
    path('maintenance/<int:pk>/', MaintenanceRequestDetail.as_view(), name='maintenance-detail'),
]