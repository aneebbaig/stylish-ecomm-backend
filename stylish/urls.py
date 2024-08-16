
from django.contrib import admin
from django.urls import path, include
from .settings import base
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls'))
] + static(base.MEDIA_URL,document_root = base.MEDIA_ROOT)
