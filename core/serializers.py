from django.db import models
from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone']


class VendedorSerializer(serializers.ModelSerializer):
    model = Vendedor
    fields = ['id', 'nome', 'num_registro']


class GrupoSerializer(serializers.ModelSerializer):
    model = Grupo
    fields = ['id', 'nome']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'valor', 'grupo']


class VendaSerializer(serializers.ModelSerializer):
    model = Venda
    fields = ['cliente', 'vendedor', 'data_venda', 'valor_total']


class ItensVendaSerializer(serializers.ModelSerializer):
    model = ItensVenda
    fields = ['venda', 'produto', 'quantidade', 'valor_item']


class VendaReportSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    vendedor = serializers.StringRelatedField()
    itens = serializers.StringRelatedField(many=True)

    class Meta:
        model = Venda
        fields = ['id', 'cliente', 'vendedor', 'data_venda', 'valor_total', 'itens']
