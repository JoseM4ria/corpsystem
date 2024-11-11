from rest_framework import viewsets, generics
from .serializers import *
from django_filters import rest_framework as filters
from django.shortcuts import render, redirect
from .models import *


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializers_class = GrupoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class ItensVendaViewSet(viewsets.ModelViewSet):
    queryset = ItensVenda.objects.all()
    serializer_class = ItensVendaSerializer


class VendaFilter(filters.FilterSet):
    data_inicio = filters.DateTimeFilter(field_name="data_venda", lookup_expr="gte")
    data_fim = filters.DateTimeFilter(field_name="data_venda", lookup_expr="lte")
    cliente = filters.CharFilter(field_name="cliente__nome", lookup_expr="icontains")
    vendedor = filters.CharFilter(field_name="vendedor__nome", lookup_expr="icontains")

    class Meta:
        model = Venda
        fields = ['data_inicio', 'data_fim', 'cliente', 'vendedor']


class VendaReportView(generics.ListAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaReportSerializer
    filterset_class = VendaFilter


def adicionar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        Cliente.objects.create(nome=nome, email=email, telefone=telefone)

        return redirect('adicionar_cliente')

    return render(request, 'core/add_cliente.html')


def adicionar_venda(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        vendedor_id = request.POST['vendedor']
        valor_total = request.POST['valor_total']

        # Obter instâncias de Cliente e Vendedor
        cliente = Cliente.objects.get(id=cliente_id)
        vendedor = Vendedor.objects.get(id=vendedor_id)

        # Criar uma nova venda
        Venda.objects.create(cliente=cliente, vendedor=vendedor, valor_total=valor_total)

        # Redirecionar após salvar a venda (pode ser para uma lista de vendas, por exemplo)
        return redirect('adicionar_venda')  # Redireciona para a mesma página

    # Obter todos os clientes e vendedores para exibir no formulário
    clientes = Cliente.objects.all()
    vendedores = Vendedor.objects.all()
    return render(request, 'core/add_venda.html', {'clientes': clientes, 'vendedores': vendedores})