from rest_framework import routers
from quotes.api import AuthorViewSet, QuoteViewSet

router = routers.DefaultRouter()
router.register(r'autors', AuthorViewSet)
router.register(r'quotes', QuoteViewSet)
urlpatterns = router.urls

