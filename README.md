# 🌬️ Essences Ar-Condicionados — Sistema Web de Gestão e Captação

> **Projeto Integrador III — UNIVESP**  
> Cliente real: **Maurício Jachetto** (Essences Ar-Condicionados)

---

## 📋 Sobre o Projeto

Este repositório contém o **sistema web completo** desenvolvido como Projeto Integrador para a UNIVESP. A aplicação atende a um prestador de serviços autônomo de ar-condicionado e resolve dois problemas reais identificados:

1. **Falta de organização operacional**: nenhum sistema formal para gerenciar clientes, serviços e estoque de materiais.
2. **Falta de presença digital**: nenhum canal online para captação de novos clientes.

**A solução entregue:**
- 🔐 **Backoffice privado** (AdminLTE v4 + Django) com CRUD completo de Clientes, Serviços e Materiais.
- 📊 **Dashboard analítico** com gráficos dinâmicos (Chart.js) mostrando o status dos serviços.
- 🌐 **Landing Page pública** para captação de leads/orçamentos diretamente no banco.
- ☁️ **Infraestrutura em nuvem** com Docker e banco gerenciado via Cloudflare.
- 🧪 **Testes unitários** e **CI/CD** com GitHub Actions.

---

## ✅ Requisitos UNIVESP Atendidos

| Requisito UNIVESP                | Implementação                                                     | Status |
|----------------------------------|-------------------------------------------------------------------|--------|
| **Framework Web**                | Django 6 com arquitetura MVT e Class-Based Views                  | ✅     |
| **Banco de Dados Relacional**    | SQLite local (dev) / Cloudflare D1 via `dj-database-url` (prod)  | ✅     |
| **Script Web (JavaScript)**      | Chart.js integrado no Dashboard via JSON do backend               | ✅     |
| **Acessibilidade**               | AdminLTE v4 (Bootstrap 5) com tags semânticas e atributos ARIA    | ✅     |
| **Controle de Versão**           | Repositório Git no GitHub com histórico de commits                | ✅     |
| **Integração Contínua (CI)**     | GitHub Actions (`.github/workflows/django.yml`)                  | ✅     |
| **Testes Unitários**             | `django.test.TestCase` para models e views do app `gestao`        | ✅     |
| **Nuvem / Deploy**               | Docker + `docker-compose.yml` + integração Cloudflare             | ✅     |
| **Requisito Específico**         | **Análise de Dados** — processamento e visualização com Chart.js  | ✅     |
| **Problema de Negócio**          | Landing Page + Backoffice de Gestão                               | ✅     |

---

## 🏗️ Arquitetura do Sistema

```
PIUNivesp3/
├── core/               # Configuração central do projeto Django
│   ├── settings.py     # Configurações (env vars, dj-database-url)
│   └── urls.py         # Roteamento principal
│
├── gestao/             # App do Backoffice (área restrita)
│   ├── models.py       # Modelos: Cliente, Servico, Material
│   ├── views.py        # CBVs: Dashboard, CRUD completo
│   ├── urls.py         # Rotas do backoffice (/gestao/...)
│   └── tests.py        # Testes unitários (models + views)
│
├── website/            # App da Landing Page (área pública)
│   ├── views.py        # LandingPageView (CreateView)
│   ├── forms.py        # ContatoForm (ModelForm de Cliente)
│   └── urls.py         # Rota raiz (/)
│
├── templates/          # Templates HTML (AdminLTE v4)
│   ├── gestao/         # Templates do backoffice
│   └── website/        # Template da landing page
│
├── static/             # CSS, JS, Imagens
├── docs/               # Documentação do projeto
│
├── Dockerfile          # Imagem Docker otimizada (Python 3.12 slim)
├── docker-compose.yml  # Ambiente de desenvolvimento local
├── .env                # Variáveis de ambiente (não versionado)
├── requirements.txt    # Dependências Python
└── .github/
    └── workflows/
        └── django.yml  # Pipeline CI/CD do GitHub Actions
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/) e Docker Compose instalados
- **ou** Python 3.12+ e pip

### Opção 1: Via Docker (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/PIUNivesp3.git
cd PIUNivesp3

# 2. Inicie o ambiente
docker-compose up --build

# 3. Em outro terminal, execute as migrações
docker-compose exec web python manage.py migrate

# 4. Crie um superusuário para acessar o backoffice
docker-compose exec web python manage.py createsuperuser

# 5. Acesse em: http://localhost:8000
```

### Opção 2: Via Python puro

```bash
# 1. Clone e entre na pasta
git clone https://github.com/SEU_USUARIO/PIUNivesp3.git
cd PIUNivesp3

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env .env.local  # ajuste conforme necessário

# 5. Execute as migrações e inicie o servidor
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🌐 URLs do Sistema

| URL                      | Descrição                                   | Acesso       |
|--------------------------|---------------------------------------------|--------------|
| `/`                      | Landing Page — captação de orçamentos       | Público      |
| `/gestao/`               | Dashboard analítico                         | Login req.   |
| `/gestao/clientes/`      | Gerenciar clientes                          | Login req.   |
| `/gestao/servicos/`      | Gerenciar serviços/orçamentos               | Login req.   |
| `/gestao/materiais/`     | Gerenciar estoque de materiais              | Login req.   |
| `/contas/login/`         | Login do backoffice                         | Público      |
| `/admin/`                | Admin nativo do Django                      | Superuser    |

---

## 🧪 Rodando os Testes

```bash
# Localmente
python manage.py test

# Via Docker
docker-compose exec web python manage.py test
```

Os testes cobrem:
- Criação e `__str__` dos models `Cliente`, `Servico` e `Material`
- Status HTTP das views protegidas pelo `LoginRequiredMixin`
- Conteúdo retornado pelas listagens (ListView)

---

## ⚙️ Variáveis de Ambiente (`.env`)

| Variável            | Descrição                                      | Padrão (dev)              |
|---------------------|------------------------------------------------|---------------------------|
| `SECRET_KEY`        | Chave secreta do Django                        | Valor insecure de dev     |
| `DEBUG`             | Modo debug (`True`/`False`)                    | `True`                    |
| `ALLOWED_HOSTS`     | Hosts permitidos (separados por vírgula)       | `*`                       |
| `DATABASE_URL`      | String de conexão do banco (dj-database-url)   | `sqlite:///db.sqlite3`    |
| `CLOUDFLARE_ID`     | Account ID da Cloudflare                       | —                         |
| `CLOUDFLARE_DB`     | UUID do banco D1 na Cloudflare                 | —                         |
| `CLOUDFLARE_TOKEN`  | API Token da Cloudflare                        | —                         |

> ⚠️ **Nunca versione o arquivo `.env` com secrets reais.** O `.gitignore` já está configurado para ignorá-lo.

---

## 🛠️ Stack Tecnológica

| Camada           | Tecnologia                 |
|------------------|----------------------------|
| Backend          | Python 3.12 + Django 6     |
| Frontend         | AdminLTE v4 + Bootstrap 5  |
| Gráficos         | Chart.js                   |
| Formulários      | django-crispy-forms + crispy-bootstrap5 |
| Banco (dev)      | SQLite                     |
| Banco (prod)     | Cloudflare D1 via dj-database-url |
| Containerização  | Docker + Docker Compose    |
| CI/CD            | GitHub Actions             |
| Servidor (prod)  | Gunicorn                   |

---

## 👥 Equipe

Projeto desenvolvido por alunos do curso de **Tecnólogo em Ciência de Dados** da **UNIVESP** como requisito parcial da disciplina de Projeto Integrador III.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos. Todos os direitos reservados.
