from django.urls import path
from . import views

urlpatterns = [
    path('', views.main.as_view(), name="main"),
    path('adding/', views.adding.as_view(), name="adding"),
    path('<firstname>_<lastname>__delete', views.deleting.as_view(), name="deleting"),
    path('<firstname>_<lastname>__edit', views.editing.as_view(), name="editing"),
]
