"""
Management command para criar o superusuário padrão do sistema.

Uso:
    python manage.py create_admin

Este comando é idempotente: se o usuário já existir, apenas exibe uma
mensagem informativa sem causar erro.
"""
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	help = 'Cria o superusuário admin.univesp com credenciais padrão'

	# Credenciais padrão (podem ser sobrescritas por variáveis de ambiente)
	DEFAULT_USERNAME = 'admin.univesp'
	DEFAULT_EMAIL = '1701253@aluno.univesp.br'
	DEFAULT_PASSWORD = 'A123456b!'

	def handle(self, *args, **options):
		username = os.environ.get('ADMIN_USERNAME', self.DEFAULT_USERNAME)
		email = os.environ.get('ADMIN_EMAIL', self.DEFAULT_EMAIL)
		password = os.environ.get('ADMIN_PASSWORD', self.DEFAULT_PASSWORD)

		if User.objects.filter(username=username).exists():
			self.stdout.write(
				self.style.WARNING(
					f'Superusuário "{username}" já existe. Nenhuma ação necessária.'
				)
			)
			return

		User.objects.create_superuser(
			username=username,
			email=email,
			password=password,
		)

		self.stdout.write(
			self.style.SUCCESS(
				f'Superusuário "{username}" criado com sucesso! '
				f'Email: {email}'
			)
		)
