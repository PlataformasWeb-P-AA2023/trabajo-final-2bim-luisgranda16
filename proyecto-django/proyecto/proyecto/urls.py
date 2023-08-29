from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from rest_framework import routers
from proyecapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'personas', views.PersonsaViewSet)
router.register(r'barrios', views.BarrioViewSet)
router.register(r'localCo', views.LocalComidaViewSet)
router.register(r'localRe', views.LocalRepuestoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('proyecapp.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()