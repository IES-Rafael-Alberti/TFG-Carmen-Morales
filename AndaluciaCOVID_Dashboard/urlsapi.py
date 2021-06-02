from . import views
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    # api
    path('api-documentacion', views.apiOverview, name="api-overview"),
    path('provincia-lista', views.provinceList, name="province-list"),
    path('distrito-lista', views.districtList, name="district-list"),
    path('municipio-lista', views.townshipList, name="township-list"),
    path('region-historico-detalle/<int:pk>/', views.regionHistoricDetail, name="region-historic-detail"),     
    path('municipio-historico-detalle/<int:pk>/', views.townshipHistoricDetail, name="township-historic-detail"),
    path('provincia-historico-detalle/<int:pk>/', views.provinceHistoricDetail, name="province-historic-detail"),
    path('region-acumulado/', views.regionAccumulatedAll, name="region-acumulated-all"),
    path('provincia-acumulado', views.provinceAccumulatedAll, name="province-acumulated-all")   
]