from django.urls import path
from .views import CarCreate, CarList, CarDetail, CarUpdate, CarDelete


urlpatterns = [
    path('create/', CarCreate.as_view(), name='create-customer'),
    path('', CarList.as_view()),
    path('<int:pk>/', CarDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', CarUpdate.as_view(), name='update-customer'),
    path('delete/<int:pk>/', CarDelete.as_view(), name='delete-customer')
]
