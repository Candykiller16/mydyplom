from django.contrib import admin
from django.urls import path, include
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    path('members/', include('django.contrib.auth.urls')), # этот Пакет django попытается использовать для аутентификации
    path('members/', include('members.urls')), # А если не получиться, или мы будем использовать свои странички, то используй это
    # <!-- Нам не нужно прописывать url для logout, т.к. она уже прописана в django.auto -->

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)