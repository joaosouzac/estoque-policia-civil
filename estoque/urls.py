from rest_framework.routers import DefaultRouter

from .api import viewsets

app_name = "estoque"

router = DefaultRouter(trailing_slash=False)
router.register(r'objetos', viewsets.ObjetoViewSet)
router.register(r'armas', viewsets.ArmaViewSet)
router.register(r'municoes', viewsets.MunicaoViewSet)

urlpatterns = router.urls