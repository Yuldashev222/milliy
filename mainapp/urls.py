from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("edit-adjective/<int:id>/", editAdjective, name="edit-adjective"),
    path("add-adjective/", addAdjective, name="add-adjective"),
    path("delete-adjective/<int:id>/", deleteAdjective, name="delete-adjective"),
    path("add-objs/", add_objs, name="add-objs"),
]