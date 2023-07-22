from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('pagina1',views.pagina1,name='pagina1'),
    path('artista',views.artista,name='artista'),
    path('artista/add',views.addartista,name='artista-add'),
    path('artista/edit',views.editartista, name='edit-artista')
]