from django.urls import path
from . import views




urlpatterns = [
    path('',views.index,name="home"),
    path('collection',views.collection,name="collection"),
    path('about',views.about,name="about"),
    path('contact', views.Contactview.as_view(), name="contact"),


]
