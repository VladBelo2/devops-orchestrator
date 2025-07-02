#!/usr/bin/env bash
set -e

CLUSTER_NAME="$1"
INSTALL_DASHBOARD="$2"
DEPLOY_TEST_APP="$3"

echo "────────────────────────────────────────"
echo "[STEP] ☸️ Installing K3s Cluster: $CLUSTER_NAME"
echo "────────────────────────────────────────"

if command -v k3s &>/dev/null; then
  echo "[INFO] ✅ K3s is already installed."
else
  echo "[INFO] 📥 Installing K3s via official script..."
  curl -sfL https://get.k3s.io | sh -
fi

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

echo "[INFO] ⏳ Waiting for node readiness..."
kubectl wait node --all --for=condition=Ready --timeout=60s

if [[ "$INSTALL_DASHBOARD" == "true" ]]; then
  echo "────────────────────────────────────────"
  echo "[STEP] 🧭 Installing Kubernetes Dashboard"
  echo "────────────────────────────────────────"
  kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
fi

if [[ "$DEPLOY_TEST_APP" == "true" ]]; then
  echo "────────────────────────────────────────"
  echo "[STEP] 🧪 Deploying Test NGINX Pod"
  echo "────────────────────────────────────────"
  kubectl create deployment nginx --image=nginx || echo "[INFO] Deployment already exists."
  kubectl expose deployment nginx --port=80 --type=ClusterIP || true
fi

echo "────────────────────────────────────────"
echo "[DONE] ✅ K3s Cluster Provisioned"
kubectl get nodes
kubectl get pods -A
