from django.urls import path
from .views import *

urlpatterns = [
    path('list/',AppealList.as_view(),name='appeal_list'),   
    path('create/<int:pk>',AddApeal.as_view(),name='appeal_create'),   
    path('detail/<int:pk>',AppealDetail.as_view(),name='appeal_detail'),   
    path('update/<int:pk>',UpdateAppeal.as_view(),name='appeal_update'),   
    path('delete/<int:pk>',DeleteAppeal.as_view(),name='appeal_delete'),   

]