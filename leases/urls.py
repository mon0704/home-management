from django.urls import path
from .views import LeaseList, LeaseDetail

urlpatterns = [
    path('leases/', LeaseList.as_view(), name='lease-list'),
    path('leases/<int:pk>/', LeaseDetail.as_view(), name='lease-detail'),
]