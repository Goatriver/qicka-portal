from django.contrib import admin
from django.urls import path, include
from data_logger_api.urls import router
from homepage import urls as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'', include(home.urls))
]
