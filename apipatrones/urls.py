"""
URL configuration for apipatrones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Rest framework imports
from rest_framework import routers

# Local imports
# Elimina o comenta las siguientes líneas si 'pedidos_cafe' no es parte de este proyecto:
# from pedidos_cafe.views import PedidoCafeViewSet 
from apiconos.views import PedidoConoViewSet # Importa el ViewSet para conos

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

# Elimina o comenta la siguiente línea si 'pedidos_cafe' no es parte de este proyecto:
# router.register(r"pedidos_cafe", PedidoCafeViewSet, basename="pedidos_cafe") 
router.register(r"pedidoconos", PedidoConoViewSet, basename="pedidosconos") # Endpoint para conos


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]