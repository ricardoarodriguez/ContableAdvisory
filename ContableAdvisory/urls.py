from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'ciiu', views.CIIUViewSet)
router.register(r'tributos', views.TributosViewSet)
router.register(r'responsabilidad', views.ResponsabilidadFiscalViewSet)
router.register(r'estadoServicios', views.EstadoServicioViewSet)
router.register(r'gestionServicios', views.GestionServicioViewSet)
router.register(r'detalleServicio', views.DetalleServicioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include('user.urls', namespace='user')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


