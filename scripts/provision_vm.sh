#!/usr/bin/env bash
set -e

INSTALL_PYTHON="$1"
PIP_PACKAGES="$2"

echo "[INFO] 📦 Running Provisioning Script"
sudo apt-get update -y
sudo apt-get install -y curl git vim

if [[ "$INSTALL_PYTHON" == "true" ]]; then
  echo "[INFO] 🐍 Installing Python + pip"
  sudo apt-get install -y python3 python3-pip
  pip3 install --upgrade pip setuptools wheel
  [[ -n "$PIP_PACKAGES" ]] && pip3 install $PIP_PACKAGES
fi

echo "[DONE] ✅ VM Provisioned"
