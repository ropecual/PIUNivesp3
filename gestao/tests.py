from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cliente, Material, Servico

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Mauricio Jachetto",
            telefone="11999999999",
            email="mauricio@essences.com",
            endereco="Rua Teste, 123"
        )

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, "Mauricio Jachetto")
        self.assertEqual(str(self.cliente), "Mauricio Jachetto")

class MaterialModelTest(TestCase):
    def setUp(self):
        self.material = Material.objects.create(
            nome="Tubo de Cobre",
            custo_unitario=50.00,
            estoque_atual=10
        )

    def test_material_creation(self):
        self.assertEqual(self.material.estoque_atual, 10)
        self.assertEqual(str(self.material), "Tubo de Cobre")

class ServicoModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Cliente Teste",
            telefone="11888888888"
        )
        self.servico = Servico.objects.create(
            cliente=self.cliente,
            tipo="INST",
            descricao="Instalação de Ar Condicionado",
            status="PEND",
            valor_mao_de_obra=200.00
        )

    def test_servico_creation(self):
        self.assertEqual(self.servico.tipo, "INST")
        self.assertEqual(str(self.servico), "Instalação - Cliente Teste")

class ViewsTest(TestCase):
    def setUp(self):
        # Cria um usuário e faz login (necessário para as views protegidas)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Dados fake
        self.cliente = Cliente.objects.create(nome="João", telefone="123")
        self.material = Material.objects.create(nome="Gás R22", custo_unitario=150.00, estoque_atual=5)
        self.servico = Servico.objects.create(cliente=self.cliente, tipo="MAN", descricao="Manutenção preventiva")

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_cliente_list_view(self):
        response = self.client.get(reverse('cliente_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "João")

    def test_material_list_view(self):
        response = self.client.get(reverse('material_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gás R22")

    def test_servico_list_view(self):
        response = self.client.get(reverse('servico_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manutenção")
