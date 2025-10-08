#!/usr/bin/env python3
"""
Script para coletar métricas DORA do projeto Registre
"""
import requests
import json
from datetime import datetime, timedelta
import os

class DORAMetrics:
    def __init__(self, repo_owner, repo_name, token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_deployment_frequency(self, days=30):
        """Calcula frequência de deploys"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/deployments"
        params = {
            "since": start_date.isoformat(),
            "until": end_date.isoformat()
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        deployments = response.json()
        
        frequency = len(deployments) / days
        return {
            "metric": "deployment_frequency",
            "value": frequency,
            "unit": "deployments_per_day",
            "period_days": days
        }

    def get_lead_time_for_changes(self, days=30):
        """Calcula lead time para mudanças"""
        url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/pulls"
        params = {
            "state": "closed",
            "per_page": 100
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        prs = response.json()
        
        lead_times = []
        for pr in prs:
            if pr['merged_at']:
                created = datetime.fromisoformat(pr['created_at'].replace('Z', '+00:00'))
                merged = datetime.fromisoformat(pr['merged_at'].replace('Z', '+00:00'))
                lead_time = (merged - created).total_seconds() / 3600  # horas
                lead_times.append(lead_time)
        
        avg_lead_time = sum(lead_times) / len(lead_times) if lead_times else 0
        
        return {
            "metric": "lead_time_for_changes",
            "value": avg_lead_time,
            "unit": "hours",
            "sample_size": len(lead_times)
        }

    def get_change_failure_rate(self, days=30):
        """Calcula taxa de falhas"""
        # Implementar baseado em issues marcadas como bugs
        url = f"{self.base_url}/repos/{self.repo_owner}/{self.repo_name}/issues"
        params = {
            "labels": "bug,hotfix",
            "state": "all",
            "per_page": 100
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        issues = response.json()
        
        total_deployments = self.get_deployment_frequency(days)["value"] * days
        failure_count = len([i for i in issues if "bug" in [l["name"] for l in i["labels"]]])
        
        failure_rate = (failure_count / total_deployments * 100) if total_deployments > 0 else 0
        
        return {
            "metric": "change_failure_rate",
            "value": failure_rate,
            "unit": "percentage",
            "failures": failure_count,
            "total_deployments": total_deployments
        }

    def collect_all_metrics(self):
        """Coleta todas as métricas DORA"""
        metrics = {
            "collected_at": datetime.now().isoformat(),
            "repository": f"{self.repo_owner}/{self.repo_name}",
            "metrics": [
                self.get_deployment_frequency(),
                self.get_lead_time_for_changes(),
                self.get_change_failure_rate()
            ]
        }
        
        # Salvar em arquivo JSON
        with open("dora_metrics.json", "w") as f:
            json.dump(metrics, f, indent=2)
        
        return metrics

if __name__ == "__main__":
    # Usar variáveis de ambiente para configuração
    repo_owner = os.getenv("GITHUB_REPOSITORY_OWNER")
    repo_name = os.getenv("GITHUB_REPOSITORY_NAME")
    token = os.getenv("GITHUB_TOKEN")
    
    collector = DORAMetrics(repo_owner, repo_name, token)
    metrics = collector.collect_all_metrics()
    
    print("Métricas DORA coletadas:")
    print(json.dumps(metrics, indent=2))
