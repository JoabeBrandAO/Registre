# Estrutura de Pastas do Projeto Registre

```
registre/
├── README.md
├── LICENSE
├── .gitignore
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── .env.example
├── docker-compose.yml
├── docker-compose.override.yml.example
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   ├── security-scan.yml
│   │   └── accessibility-test.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── security_report.md
│   └── PULL_REQUEST_TEMPLATE.md
│
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── security.md
│   ├── accessibility.md
│   ├── api/
│   │   ├── openapi.yml
│   │   └── endpoints.md
│   ├── deployment/
│   │   ├── development.md
│   │   ├── staging.md
│   │   └── production.md
│   ├── diagrams/
│   │   ├── architecture.png
│   │   ├── data-flow.png
│   │   └── threat-model.png
│   └── user-guides/
│       ├── installation.md
│       ├── configuration.md
│       └── no-code-interface.md
│
├── src/
│   ├── backend/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── records.py
│   │   │   │   ├── reports.py
│   │   │   │   └── admin.py
│   │   │   ├── middleware/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── cors.py
│   │   │   │   └── rate_limit.py
│   │   │   └── validators/
│   │   │       ├── __init__.py
│   │   │       ├── record_schemas.py
│   │   │       └── user_schemas.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user.py
│   │   │   ├── record.py
│   │   │   ├── field.py
│   │   │   └── collection.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── record_service.py
│   │   │   ├── ai_service.py
│   │   │   ├── report_service.py
│   │   │   └── email_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   ├── security.py
│   │   │   ├── logging.py
│   │   │   └── helpers.py
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sentiment_analysis.py
│   │   │   │   └── report_generator.py
│   │   │   ├── processors/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── data_processor.py
│   │   │   │   └── nlp_processor.py
│   │   │   └── training/
│   │   │       ├── datasets/
│   │   │       ├── models/
│   │   │       └── scripts/
│   │   ├── migrations/
│   │   │   └── versions/
│   │   ├── app.py
│   │   ├── config.py
│   │   └── requirements.txt
│   │
│   ├── frontend/
│   │   ├── public/
│   │   │   ├── index.html
│   │   │   ├── manifest.json
│   │   │   ├── robots.txt
│   │   │   └── icons/
│   │   │       ├── favicon.ico
│   │   │       └── logo.png
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── common/
│   │   │   │   │   ├── Header/
│   │   │   │   │   ├── Footer/
│   │   │   │   │   ├── Navigation/
│   │   │   │   │   └── Loading/
│   │   │   │   ├── forms/
│   │   │   │   │   ├── DynamicForm/
│   │   │   │   │   ├── FormBuilder/
│   │   │   │   │   └── FieldTypes/
│   │   │   │   ├── charts/
│   │   │   │   │   ├── BarChart/
│   │   │   │   │   ├── LineChart/
│   │   │   │   │   └── PieChart/
│   │   │   │   └── accessibility/
│   │   │   │       ├── SkipLinks/
│   │   │   │       ├── ScreenReaderOnly/
│   │   │   │       └── FocusTrap/
│   │   │   ├── pages/
│   │   │   │   ├── Dashboard/
│   │   │   │   ├── Records/
│   │   │   │   ├── Reports/
│   │   │   │   ├── Settings/
│   │   │   │   └── Auth/
│   │   │   ├── hooks/
│   │   │   │   ├── useAuth.js
│   │   │   │   ├── useApi.js
│   │   │   │   └── useAccessibility.js
│   │   │   ├── services/
│   │   │   │   ├── api.js
│   │   │   │   ├── auth.js
│   │   │   │   └── storage.js
│   │   │   ├── utils/
│   │   │   │   ├── accessibility.js
│   │   │   │   ├── validation.js
│   │   │   │   └── formatting.js
│   │   │   ├── styles/
│   │   │   │   ├── globals.css
│   │   │   │   ├── variables.css
│   │   │   │   ├── components/
│   │   │   │   └── accessibility.css
│   │   │   ├── assets/
│   │   │   │   ├── images/
│   │   │   │   ├── icons/
│   │   │   │   └── fonts/
│   │   │   ├── App.js
│   │   │   ├── index.js
│   │   │   └── setupTests.js
│   │   ├── package.json
│   │   ├── package-lock.json
│   │   └── .eslintrc.js
│   │
│   └── shared/
│       ├── types/
│       │   ├── user.ts
│       │   ├── record.ts
│       │   └── api.ts
│       ├── constants/
│       │   ├── api-endpoints.js
│       │   ├── validation-rules.js
│       │   └── accessibility-constants.js
│       └── utils/
│           ├── date-helpers.js
│           ├── validation.js
│           └── formatters.js
│
├── tests/
│   ├── backend/
│   │   ├── unit/
│   │   │   ├── models/
│   │   │   ├── services/
│   │   │   └── utils/
│   │   ├── integration/
│   │   │   ├── api/
│   │   │   └── database/
│   │   ├── fixtures/
│   │   │   ├── users.json
│   │   │   └── records.json
│   │   └── conftest.py
│   ├── frontend/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   ├── e2e/
│   │   │   ├── auth.spec.js
│   │   │   ├── records.spec.js
│   │   │   └── accessibility.spec.js
│   │   └── jest.config.js
│   ├── accessibility/
│   │   ├── axe-tests/
│   │   ├── lighthouse-tests/
│   │   └── screen-reader-tests/
│   ├── security/
│   │   ├── owasp-zap/
│   │   └── penetration-tests/
│   └── performance/
│       ├── load-tests/
│       └── stress-tests/
│
├── infrastructure/
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── database/
│   │   │   ├── compute/
│   │   │   ├── networking/
│   │   │   └── security/
│   │   ├── environments/
│   │   │   ├── development/
│   │   │   ├── staging/
│   │   │   └── production/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── versions.tf
│   ├── ansible/
│   │   ├── inventories/
│   │   │   ├── development/
│   │   │   ├── staging/
│   │   │   └── production/
│   │   ├── roles/
│   │   │   ├── common/
│   │   │   ├── database/
│   │   │   ├── webserver/
│   │   │   └── monitoring/
│   │   ├── playbooks/
│   │   │   ├── site.yml
│   │   │   ├── database.yml
│   │   │   └── security.yml
│   │   └── ansible.cfg
│   ├── docker/
│   │   ├── backend/
│   │   │   ├── Dockerfile
│   │   │   ├── Dockerfile.prod
│   │   │   └── .dockerignore
│   │   ├── frontend/
│   │   │   ├── Dockerfile
│   │   │   ├── Dockerfile.prod
│   │   │   └── .dockerignore
│   │   ├── nginx/
│   │   │   ├── Dockerfile
│   │   │   └── nginx.conf
│   │   └── monitoring/
│   │       ├── prometheus/
│   │       ├── grafana/
│   │       └── loki/
│   ├── kubernetes/
│   │   ├── base/
│   │   ├── overlays/
│   │   │   ├── development/
│   │   │   ├── staging/
│   │   │   └── production/
│   │   └── secrets/
│   └── helm/
│       ├── registre/
│       │   ├── templates/
│       │   ├── values.yaml
│       │   └── Chart.yaml
│       └── monitoring/
│
├── scripts/
│   ├── development/
│   │   ├── setup.sh
│   │   ├── start-dev.sh
│   │   └── reset-db.sh
│   ├── deployment/
│   │   ├── deploy.sh
│   │   ├── rollback.sh
│   │   └── health-check.sh
│   ├── database/
│   │   ├── migrate.py
│   │   ├── seed.py
│   │   └── backup.sh
│   ├── security/
│   │   ├── scan-vulnerabilities.sh
│   │   ├── update-secrets.sh
│   │   └── security-audit.py
│   └── ci/
│       ├── build.sh
│       ├── test.sh
│       └── quality-check.sh
│
├── monitoring/
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── rules/
│   │       ├── app-alerts.yml
│   │       └── infra-alerts.yml
│   ├── grafana/
│   │   ├── dashboards/
│   │   │   ├── application.json
│   │   │   ├── infrastructure.json
│   │   │   └── security.json
│   │   └── provisioning/
│   │       ├── datasources/
│   │       └── dashboards/
│   ├── loki/
│   │   └── loki-config.yml
│   └── alertmanager/
│       └── alertmanager.yml
│
├── config/
│   ├── development/
│   │   ├── app.yml
│   │   ├── database.yml
│   │   └── logging.yml
│   ├── staging/
│   │   ├── app.yml
│   │   ├── database.yml
│   │   └── logging.yml
│   ├── production/
│   │   ├── app.yml
│   │   ├── database.yml
│   │   └── logging.yml
│   └── defaults/
│       ├── security.yml
│       ├── accessibility.yml
│       └── ai-models.yml
│
├── data/
│   ├── migrations/
│   ├── seeds/
│   │   ├── users.json
│   │   ├── templates.json
│   │   └── sample-records.json
│   └── fixtures/
│       ├── test-data.json
│       └── demo-data.json
│
├── packages/
│   ├── ui-components/
│   │   ├── package.json
│   │   ├── src/
│   │   └── dist/
│   ├── form-builder/
│   │   ├── package.json
│   │   ├── src/
│   │   └── dist/
│   └── accessibility-tools/
│       ├── package.json
│       ├── src/
│       └── dist/
│
├── build/
│   ├── frontend/
│   ├── backend/
│   └── documentation/
│
└── tmp/
    ├── logs/
    ├── uploads/
    └── cache/
```

## Características Especiais da Estrutura:

### 🎯 **Foco em No-Code**
- `src/frontend/components/forms/FormBuilder/` - Interface visual para criação de formulários
- `src/frontend/components/forms/FieldTypes/` - Tipos de campo personalizáveis

### 🤖 **IA Integrada**
- `src/backend/ai/` - Módulos específicos para machine learning
- `src/backend/ai/training/` - Datasets e scripts de treino

### ♿ **Acessibilidade WCAG 2.2 AA**
- `src/frontend/components/accessibility/` - Componentes específicos de acessibilidade
- `tests/accessibility/` - Testes automatizados de acessibilidade
- `config/defaults/accessibility.yml` - Configurações de acessibilidade

### 🔒 **DevSecOps**
- `tests/security/` - Testes de segurança automatizados
- `scripts/security/` - Scripts de auditoria e vulnerabilidade
- `.github/workflows/security-scan.yml` - Pipeline de segurança

### 📊 **Observabilidade**
- `monitoring/` - Configurações completas de monitoramento
- `monitoring/grafana/dashboards/` - Dashboards específicos do projeto

### 🏗️ **Infraestrutura Moderna**
- `infrastructure/terraform/modules/` - Módulos reutilizáveis
- `infrastructure/kubernetes/` - Manifests Kubernetes
- `infrastructure/helm/` - Charts Helm para deploy

### 🧩 **Modularidade**
- `packages/` - Componentes reutilizáveis versionados independentemente
- `src/shared/` - Código compartilhado entre frontend e backend