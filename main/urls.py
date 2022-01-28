from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('signout', views.signout),
    path('signup', views.signup),

    path('add', views.add),
    path('remove/<int:item_id>', views.deleteItem)
]