from django.urls import path
from .views import *

urlpatterns = [
    path('list/',CompanyList.as_view(),name='company_list'),
    path('create/',AddCompany.as_view(),name='create_company'),
    path('detail/<int:pk>/',CompanyDetail.as_view(),name='company_detail'),
    path('update/<int:pk>/',CompanyUpdate.as_view(),name='company_update'),
    path('delete/<int:pk>/',CompanyDelete.as_view(),name='company_delete'),
    
]