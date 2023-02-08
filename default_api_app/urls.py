from django.urls import path
from .api_views import ItemAPIList, ItemAPIDetail
from .frontend_views import (
    ItemCreateView,
    ItemDetailView,
    ItemDeleteView,
    ItemListView,
    ItemUpdateView,
)

urlpatterns = [
    path('api/v1/list/', ItemAPIList.as_view(), name='item_list_api'),
    path('api/<int:pk>/', ItemAPIDetail.as_view(), name='item_detail_api'),
    path('', ItemListView.as_view(), name='list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='delete'),
]
