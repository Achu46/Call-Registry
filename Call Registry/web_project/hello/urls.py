from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home-page"),
    path("a",views.home,name="a"),
    path("insert/",views.insert,name="insert"),
    path("b",views.search,name="b"),
    path("c",views.show,name="c"),
    path("order/",views.order,name="order")
]