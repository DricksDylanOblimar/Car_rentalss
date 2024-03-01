
# from django.urls import path
# from CarRent.views import CarListView, CarRentDetailView, CarCreateView, CarUpdateView, CarDeleteView

# urlpatterns = [
#     path('', CarListView.as_view(), name='list-view-car'),
#     path('detail/<int:pk>/', CarRentDetailView.as_view(), name= 'detail-view-car'),
#     path('create/', CarCreateView.as_view(), name='car-create-view'),
#     path('update/<int:pk>/', CarUpdateView.as_view(), name='car-update-view'),
#     path('delete/<int:pk>/', CarDeleteView.as_view(), name='car-delete-view')


# ]

from django.urls import path
from car.views import CarListView, CarRentDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name='list-view-car'),
    path('detail/<int:pk>/', CarRentDetailView.as_view(), name='detail-view-car'),
    path('create/', CarCreateView.as_view(), name='car-create-view'),
    path('update/<int:pk>/', CarUpdateView.as_view(), name='car-update-view'),
    path('delete/<int:pk>/', CarDeleteView.as_view(), name='car-delete-view'),
]

