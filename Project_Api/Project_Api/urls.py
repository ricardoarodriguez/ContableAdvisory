from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'ciiu', views.CIIUViewSet)
router.register(r'tributos', views.TributosViewSet)
router.register(r'responsabilidad', views.ResponsabilidadFiscalViewSet)
router.register(r'estadoServicios', views.EstadoServicioViewSet)
router.register(r'gestionServicios', views.GestionServicioViewSet)
router.register(r'detalleServicio', views.DetalleServicioViewSet)

router.register(r'ciiu/<int:pk>', views.ClienteViewSet)
router.register(r'cliente/<int:pk>', views.ClienteViewSet)
router.register(r'tributos/<int:pk>', views.ClienteViewSet)
router.register(r'responsabilidad/<int:pk>', views.ClienteViewSet)
router.register(r'estadoServicios/<int:pk>', views.ClienteViewSet)
router.register(r'gestionServicios/<int:pk>', views.ClienteViewSet)
router.register(r'detalleServicio/<int:pk>', views.ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include('user.urls', namespace='user')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)


