# 📚 TERMINOLOGY.md – DevOps Orchestrator Naming Standards

This document defines precise, standardized terminology to be used throughout the `devops-orchestrator` project (in code, UI, logs, and documentation).

---

## 🧱 Virtual Machines (VMs)

| Context | Preferred Terms |
|--------|------------------|
| Creating a VM | ✅ `Create VM`, `Provision VM`, `Launch VM` |
| Starting an existing VM | ✅ `Start VM`, `Resume VM` |
| Informal (UI, log titles) | ✅ `Spin up VM` (acceptable) |

---

## 🐳 Docker Containers & Images

| Context | Preferred Terms |
|--------|------------------|
| Create Image | ✅ `Build Image` |
| Run Container | ✅ `Start Container`, `Deploy Container` |
| Stop Container | ✅ `Stop`, `Terminate`, `Remove Container` |
| Informal | ✅ `Spin up Container` (OK in logs/UI) |
| ⚠️ Avoid | ❌ `Spin image` |

---

## ☸️ Kubernetes Resources

| Resource | Preferred Action Verbs |
|----------|------------------------|
| Cluster | `Install Cluster`, `Provision Cluster`, ✅ `Spin up Cluster` |
| Node | `Register Node`, `Join Cluster`, `Provision Node` |
| Pod | `Deploy Pod`, `Create Pod` (❌ avoid "spin up pod") |
| Service | `Expose`, `Deploy`, `Create` |
| Ingress | `Configure`, `Apply`, `Deploy` |
| Dashboard | `Enable`, `Install`, `Access` |

---

## 💬 General Guidelines

- Use **accurate terms** in documentation and logging (e.g., "Deploy container", not "spin container").
- Use **"Spin up"** only in:
  - GitHub Action names (`spin_vm.yml`)
  - Workflow UI titles
  - User-facing documentation where casual terminology aids understanding

For all scripts, manifests, and output logs, default to precision and technical correctness.

---
