from django.urls import path

# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.indexCo, name='indexCo'),
        path('indexRe', views.indexRe, name='indexRe'),
        path('crear/persona', views.crear_persona, name='crear_persona'),
        path('editar/persona/<int:id>', views.editar_persona, name='editar_persona'),
        path('eliminar/persona/<int:id>', views.eliminar_persona, name='eliminar_persona'),
        
        path('crear/barrio', views.crear_barrio, name='crear_barrio'),
        path('editar/barrio/<int:id>', views.editar_barrio, name='editar_barrio'),
        path('eliminar/barrio/<int:id>', views.eliminar_barrio, name='eliminar_barrio'),

        path('crear/barrio', views.crear_barrio, name='crear_barrio'),
        path('editar/barrio/<int:id>', views.editar_barrio, name='editar_barrio'),
        path('eliminar/barrio/<int:id>', views.eliminar_barrio, name='eliminar_barrio'),

        path('crear/localCo', views.crear_local_comida, name='crear_local_comida'),
        path('editar/localCo/<int:id>', views.editar_local_comida, name='editar_local_comida'),
        path('eliminar/localCo/<int:id>', views.eliminar_local_comida, name='eliminar_local_comida'),


        path('crear/localRe', views.crear_local_repuesto, name='crear_localRe'),
        path('editar/localRe/<int:id>', views.editar_local_repuesto, name='editar_localRe'),
        path('eliminar/localRe/<int:id>', views.eliminar_local_repuesto, name='eliminar_localRe'),
 ]