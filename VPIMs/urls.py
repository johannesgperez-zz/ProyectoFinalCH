from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    # path('Login/', include('Login.urls')),
    # path('Mensajeria/', include('Mensajeria.urls')),
    # path('Perfiles/', include('Perfiles.urls')),
    # path('Registro/', include('Registro.urls')),
]
