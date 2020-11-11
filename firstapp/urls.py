from django.urls import path
from .views import index,create,detail

urlpatterns = [
    path('create/', create, name="create"),
    path('detail/<int:detail_id>', detail, name="detail"),
]