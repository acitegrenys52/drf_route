from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from app.views import UsersViewSet

router = SimpleRouter()

router.register('blaaa', UsersViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'', include(router.urls)),
]
