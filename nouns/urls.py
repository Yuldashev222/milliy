from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="nouns"),
    path("edit-noun/<int:id>/", editNoun, name="edit-noun"),
    path("add-noun/", addNoun, name="add-noun"),
    path("delete-noun/<int:id>/", deleteNoun, name="delete-noun"),
    path("add-objs/", add_objs, name="add-objs"),
]