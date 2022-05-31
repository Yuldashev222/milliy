from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("sifatlar/", home, name="home"),
    path("sifatlar/edit-adjective/<int:id>/", editAdjective, name="edit-adjective"),
    path("add-adjective/", addAdjective, name="add-adjective"),
    path("delete-adjective/<int:id>/", deleteAdjective, name="delete-adjective"),
    path("add-objs/", add_objs, name="add-objs"),
]