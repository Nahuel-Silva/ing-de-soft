from rest_framework import routers
from .views import UsuarioViewSet

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = router.urls