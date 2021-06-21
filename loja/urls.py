from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),#rota da aplicao normal
    path('api/', include('app_loja_api.urls', namespace='app_loja_api')), #rota da api
    path('', include("app_loja.urls", namespace='app_loja')),

]
