from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='clientes')
router.register(r'vendedor', views.VendedorViewSet, basename='vendedor')
router.register(r'grupo', views.GrupoViewSet, basename='grupo')
router.register(r'produtos', views.ProdutoViewSet, basename='produtos')
router.register(r'venda', views.VendaViewSet, basename='venda')
router.register(r'itensvenda', views.ItensVendaViewSet, basename='itensvenda'),

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('relatorio-vendas/', views.VendaReportView.as_view(), name='relatorio-vendas'),
    path('adicionar-cliente/', views.adicionar_cliente, name='adicionar_cliente'),
    path('adicionar-venda/', views.adicionar_venda, name='adicionar_venda'),
]

