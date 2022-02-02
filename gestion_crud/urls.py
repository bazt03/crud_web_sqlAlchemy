from unicodedata import name
from django.urls import path
from . import views 
urlpatterns = [
    path('create', views.createView),
    #nuevamente creamos la ruta para manejar la solicitud POST
    path('store', views.store, name='store'),
    #url que muestra la lista de usuarios en una tabla
    path('', views.index),
    path('details/<int:pk>', views.detailEmp, name='detailEmp'),
    #url para elimar un registro de la DB por ID 
    path('detele/<int:pk>', views.deleteEmp, name='deleteEmp'),
    #url para actualizar los datos del formulario
    path('update/<int:pk>', views.updateEmp, name='updateEmp'),
    #
    path('edit/<int:pk>', views.update, name='edit'),
    path('json', views.jsondata, name = "jsondata")
]
