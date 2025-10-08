#!/bin/bash
set -e

echo "🚀 Configurando ambiente de desenvolvimento Registre..."

# Verificar dependências
check_dependency() {
    if ! command -v $1 &> /dev/null; then
        echo "❌ $1 não encontrado. Por favor instale antes de continuar."
        exit 1
    fi
    echo "✅ $1 encontrado"
}

echo "📋 Verificando dependências..."
check_dependency "docker"
check_dependency "docker-compose"
check_dependency "node"
check_dependency "python3"
check_dependency "git"

# Copiar arquivo de ambiente
if [ ! -f .env ]; then
    echo "📄 Copiando arquivo de configuração..."
    cp .env.example .env
    echo "⚠️  Configure o arquivo .env com suas variáveis"
fi

# Setup backend
echo "🐍 Configurando backend Python..."
cd src/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Executar migrações
echo "💾 Executando migrações de banco..."
python manage.py migrate

cd ../..

# Setup frontend
echo "⚛️ Configurando frontend..."
cd src/frontend
npm install
cd ../..

# Executar testes
echo "🧪 Executando testes iniciais..."
docker-compose run --rm backend pytest
docker-compose run --rm frontend npm test -- --run

# Inicializar base de dados com dados de exemplo
echo "🗄️ Populando base de dados..."
docker-compose run --rm backend python manage.py loaddata fixtures/initial_data.json

echo "✅ Setup completo! Execute 'docker-compose up' para iniciar a aplicação."
echo "🌐 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📊 Grafana: http://localhost:3001"
echo "📈 Prometheus: http://localhost:9090"
