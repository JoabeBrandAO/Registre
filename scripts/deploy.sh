#!/bin/bash
set -e

ENVIRONMENT=${1:-staging}
VERSION=${2:-latest}

echo "🚀 Iniciando deploy para $ENVIRONMENT..."

# Build das imagens
echo "🔨 Building imagens..."
docker-compose -f docker-compose.prod.yml build

# Tag das imagens
echo "🏷️ Tagging imagens com versão $VERSION..."
docker tag registre-frontend:latest ghcr.io/your-org/registre-frontend:$VERSION
docker tag registre-backend:latest ghcr.io/your-org/registre-backend:$VERSION

# Push para registry
echo "📤 Push para registry..."
docker push ghcr.io/your-org/registre-frontend:$VERSION
docker push ghcr.io/your-org/registre-backend:$VERSION

# Deploy usando Terraform
echo "🏗️ Deploy da infraestrutura..."
cd infra/terraform
terraform init
terraform plan -var="environment=$ENVIRONMENT" -var="app_version=$VERSION"
terraform apply -auto-approve -var="environment=$ENVIRONMENT" -var="app_version=$VERSION"

# Verificar health check
echo "🔍 Verificando saúde da aplicação..."
sleep 30
curl -f http://your-app-url/health || (echo "❌ Health check falhou" && exit 1)

echo "✅ Deploy concluído com sucesso!"
