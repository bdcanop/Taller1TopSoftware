from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('client/',ClientIndexView.as_view(),name='client_index'),
    path('client/form',CreateClient.as_view(),name='client_form'),
    path('creado',CreatedPage.as_view(),name='creado'),
    path('client/<int:id>',ClientShowView.as_view(),name='show_client'),
    path('client/delete/<int:id>',DeleteClient,name='delete_client'),
]