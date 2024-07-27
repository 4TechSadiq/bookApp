from django.urls import path
from . import views

urlpatterns = [
    path("",views.createBook),
    path("listview/",views.listBook),
    path("detailsview/<int:book_id>",views.detailsview,name="details"),
    path("updateview/<int:book_id>",views.updateBook,name="update"),
    path("delete/<int:book_id>",views.deleteView,name="delete")

]