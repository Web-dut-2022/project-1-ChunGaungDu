from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search',views.search,name="search"),
    path('random',views.randomEn,name="random"),
    path('new/',views.newEn,name="new"),
    path('saveNewMD',views.saveNewMD),
    path("<str:entry_name>",views.entry, name="entry")
]
