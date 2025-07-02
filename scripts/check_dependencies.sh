#!/bin/bash
set -e

OS_TYPE=$(uname | tr '[:upper:]' '[:lower:]')

# ─────────────────────────────────────────────
# 🛠️ Install Homebrew on macOS (if missing)
# ─────────────────────────────────────────────
install_brew_if_needed() {
  if ! command -v brew &>/dev/null; then
    echo "[INFO] 🍺 Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)" || eval "$(/usr/local/bin/brew shellenv)"
  else
    echo "[OK] ✅ Homebrew is already installed."
  fi
}

# ─────────────────────────────────────────────
# 📦 Install VirtualBox
# ─────────────────────────────────────────────
install_virtualbox() {
  echo "[INFO] 🔍 Checking VirtualBox..."
  if ! command -v VBoxManage &>/dev/null; then
    echo "[INFO] 📦 VirtualBox not found. Installing..."
    if [[ "$OS_TYPE" == "darwin" ]]; then
      install_brew_if_needed
      brew install --cask virtualbox
    elif [[ "$OS_TYPE" == "linux" ]]; then
      sudo apt update && sudo apt install -y virtualbox
    elif [[ "$OS_TYPE" == msys* || "$OS_TYPE" == cygwin* ]]; then
      choco install virtualbox -y
    else
      echo "[ERROR] ❌ Unsupported OS: $OS_TYPE"
      exit 1
    fi
  else
    echo "[OK] ✅ VirtualBox is already installed."
  fi
}

# ─────────────────────────────────────────────
# 📦 Install Vagrant
# ─────────────────────────────────────────────
install_vagrant() {
  echo "[INFO] 🔍 Checking Vagrant..."
  if ! command -v vagrant &>/dev/null; then
    echo "[INFO] 📦 Vagrant not found. Installing..."
    if [[ "$OS_TYPE" == "darwin" ]]; then
      install_brew_if_needed
      brew install --cask vagrant
    elif [[ "$OS_TYPE" == "linux" ]]; then
      sudo apt update && sudo apt install -y vagrant
    elif [[ "$OS_TYPE" == msys* || "$OS_TYPE" == cygwin* ]]; then
      choco install vagrant -y
    else
      echo "[ERROR] ❌ Unsupported OS: $OS_TYPE"
      exit 1
    fi
  else
    echo "[OK] ✅ Vagrant is already installed."
  fi
}

# ─────────────────────────────────────────────
# ✅ Run Installers
# ─────────────────────────────────────────────
install_virtualbox
install_vagrant
