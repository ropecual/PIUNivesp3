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
- ☁️ **Infraestrutura em nuvem** com Docker e banco gerenciado via **Neon Postgres (Serverless)**.
- 🧪 **Testes unitários** e **CI/CD** com GitHub Actions.

---

## ✅ Requisitos UNIVESP Atendidos

| Requisito UNIVESP                | Implementação                                                     | Status |
|----------------------------------|-------------------------------------------------------------------|--------|
| **Framework Web**                | Django 6 com arquitetura MVT e Class-Based Views                  | ✅     |
| **Banco de Dados Relacional**    | SQLite local (dev) / **Neon Postgres (prod)** via `dj-database-url` | ✅     |
| **Script Web (JavaScript)**      | Chart.js integrado no Dashboard via JSON do backend               | ✅     |
| **Acessibilidade**               | AdminLTE v4 (Bootstrap 5) com tags semânticas e atributos ARIA    | ✅     |
| **Controle de Versão**           | Repositório Git no GitHub com histórico de commits                | ✅     |
| **Integração Contínua (CI)**     | GitHub Actions (`.github/workflows/django.yml`)                  | ✅     |
| **Testes Unitários**             | `django.test.TestCase` para models e views do app `gestao`        | ✅     |
| **Nuvem / Deploy**               | Docker + `docker-compose.yml` + integração **Neon Postgres**    | ✅     |
| **Requisito Específico**         | **Análise de Dados** — processamento e visualização com Chart.js  | ✅     |
| **Problema de Negócio**          | Landing Page + Backoffice de Gestão                               | ✅     |

---

## 🏗️ Arquitetura do Sistema

```
PIUNivesp3/
├── core/               # Configuração central do projeto Django
├── gestao/             # App do Backoffice (área restrita)
├── website/            # App da Landing Page (área pública)
├── templates/          # Templates HTML (AdminLTE v4)
├── static/             # CSS, JS, Imagens
├── docs/               # Documentação do projeto
├── nginx/              # Configuração do Proxy Nginx
├── Dockerfile          # Imagem Docker otimizada (Python 3.12 slim)
├── docker-compose.yml  # Ambiente com Nginx + Gunicorn
├── .env                # Variáveis de ambiente (Neon Database URL)
├── requirements.txt    # Dependências (psycopg[binary])
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

O projeto está configurado com um **reverse proxy Nginx** rodando na porta **8585**.

```bash
# 1. Clone o repositório
git clone https://github.com/ropecual/PIUNivesp3.git
cd PIUNivesp3

# 2. Inicie o ambiente (reconstrói a imagem com Nginx e Neon config)
docker-compose up --build

# 3. Acesse em: http://localhost:8585
```

> **Nota:** O `entrypoint.sh` executará automaticamente o `migrate`, `collectstatic` e criará o superusuário padrão.

---

## ⚙️ Variáveis de Ambiente (`.env`)

| Variável            | Descrição                                      | Padrão (dev)              |
|---------------------|------------------------------------------------|---------------------------|
| `SECRET_KEY`        | Chave secreta do Django                        | Valor insecure de dev     |
| `DEBUG`             | Modo debug (`True`/`False`)                    | `True`                    |
| `ALLOWED_HOSTS`     | Hosts permitidos (separados por vírgula)       | `*`                       |
| `DATABASE_URL`      | URL de conexão **Neon Postgres**               | —                         |

> ⚠️ **Nunca versione o arquivo `.env` com secrets reais.** O `.gitignore` já está configurado para ignorá-lo.

---

## 🛠️ Stack Tecnológica

| Camada           | Tecnologia                 |
|------------------|----------------------------|
| Backend          | Python 3.12 + Django 6     |
| Frontend         | AdminLTE v4 + Bootstrap 5  |
| Gráficos         | Chart.js                   |
| Formulários      | django-crispy-forms + crispy-bootstrap5 |
| Banco (dev/prod) | **Neon Postgres Serverless** via dj-database-url |
| Containerização  | Docker + Nginx + Gunicorn  |
| CI/CD            | GitHub Actions             |
| Servidor (prod)  | Gunicorn                   |

---

## 👥 Equipe

Projeto desenvolvido por alunos do curso da **UNIVESP** como requisito parcial da disciplina de Projeto Integrador III.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos. Todos os direitos reservados.
