from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=13)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    num_registro = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vendas')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='vendedor')
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda {self.id} - Vendedor: {self.vendedor.nome}"


class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_venda')
    quantidade = models.PositiveIntegerField()
    valor_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item: {self.produto} (Venda {self.venda})"
