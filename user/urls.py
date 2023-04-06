from django.urls import path, include
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserViewSet
from rest_framework import routers

app_name = 'user'

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('getUser/', include(router.urls), name="get_user")
]