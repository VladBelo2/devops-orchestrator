# 🚀 DevOps Orchestrator

A GitHub Actions-powered control plane for provisioning local and cloud infrastructure — from VMs to Docker containers, Kubernetes clusters, and cloud instances — using dynamic form inputs and full automation.

---

## 📦 Features

- 🧱 **Spin VMs locally** using Vagrant + VirtualBox (or Parallels for Apple Silicon)
- 🐳 **Launch Docker containers** via input-driven workflows
- ☸️ Future: Create Kubernetes clusters, pods, and nodes
- ☁️ Future: Spin cloud VMs in AWS, Azure, and GCP
- 🧪 Fully GitHub Actions-controlled with self-hosted runners
- 🧾 Dynamic `Run Workflow` input fields like:
  - VM Name, Memory, CPU
  - IP Mode (DHCP or Static)
  - Python + pip installation
  - Pip package list

---

## 🖥️ Local Runner Requirements

To use this project, you must have a **self-hosted GitHub Actions runner installed and running on your macOS**.

### Install GitHub Runner (macOS)

1. Go to your GitHub repository → **Settings > Actions > Runners**
2. Click **"New self-hosted runner"**
3. Follow instructions to download, configure, and start the runner:
   ```bash
   ./config.sh --url https://github.com/YOUR_USERNAME/devops-orchestrator --token YOUR_TOKEN
   ./run.sh

💡 You only need to do this once.

---

## 🚀 Spinning a Local VM

Once the runner is online:

1. Go to GitHub > Actions > "🚀 Spin Local VM"

2. Click "Run workflow"

3. Fill in the inputs, e.g.:

```bash
VM Name: devops-vm
Memory: 2048
CPUs: 2
IP Mode: dhcp
IP Address: (leave blank)
Install Python: true
Pip Packages: flask requests
```

4. ✅ Click Run workflow

5. 🖥️ The self-hosted runner will:

- Build a custom Vagrantfile

- Run vagrant up locally

- Provision Python and pip packages

⚠️ Note: VirtualBox is not supported on Apple Silicon Macs. This test will fail unless you use an Intel-based macOS or switch to Parallels.

---

## 📂 Project Structure

```text
devops-orchestrator/
├── .github/workflows/spin_vm.yml         # GitHub Actions workflow
├── scripts/
│   ├── build_vagrantfile.py              # Dynamically builds Vagrantfile from inputs
│   └── provision_vm.sh                   # Runs inside VM to install Python/pip/etc
├── vms/                                  # Auto-generated folders per VM
│   └── devops-vm/                        # Contains generated Vagrantfile
├── README.md
```

---

## 🔮 Coming Soon

- Docker container auto-launch from inputs

- Kubernetes pod/cluster/node orchestration

- Cross-cloud VM provisioning (Azure, AWS, GCP)

- Metrics, health checks, and teardown logic

---

## 🛠️ Author

Built by @vladbelo2
This is a forward-thinking DevOps lab project, designed to evolve toward full infrastructure orchestration from GitHub's UI.

