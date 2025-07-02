#!/usr/bin/env python3
import os
import argparse

def generate_vagrantfile(vm_name, vm_memory, vm_cpus, ip_mode, ip_address):
    # Define networking configuration block
    if ip_mode.lower() == "dhcp":
        network_config = 'config.vm.network "private_network", type: "dhcp"'
    elif ip_mode.lower() == "static" and ip_address:
        network_config = f'config.vm.network "private_network", ip: "{ip_address}"'
    else:
        raise ValueError("Invalid IP configuration: Must provide IP address when using static mode.")

    # Generate final Vagrantfile content
    return f"""Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.hostname = "{vm_name}"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "{vm_memory}"
    vb.cpus = {vm_cpus}
  end

  {network_config}

  config.vm.synced_folder ".", "/vagrant", type: "virtualbox", rsync__exclude: [".venv/"]

  config.vm.provision "shell", path: "../../scripts/provision_vm.sh"
end
"""

def main():
    parser = argparse.ArgumentParser(description="Generate Vagrantfile for VM provisioning.")
    parser.add_argument("--vm-name", required=True, help="VM name and folder")
    parser.add_argument("--vm-memory", required=True, help="Memory in MB")
    parser.add_argument("--vm-cpus", required=True, help="Number of virtual CPUs")
    parser.add_argument("--ip-mode", required=True, choices=["dhcp", "static"], help="IP mode")
    parser.add_argument("--ip-address", required=False, help="Static IP (required if ip-mode=static)")

    args = parser.parse_args()

    vm_dir = f"vms/{args.vm_name}"
    os.makedirs(vm_dir, exist_ok=True)

    try:
        content = generate_vagrantfile(
            args.vm_name,
            args.vm_memory,
            args.vm_cpus,
            args.ip_mode,
            args.ip_address
        )
    except ValueError as e:
        print(f"[ERROR] ❌ {e}")
        exit(1)

    vagrantfile_path = os.path.join(vm_dir, "Vagrantfile")
    with open(vagrantfile_path, "w") as f:
        f.write(content)

    print(f"[OK] ✅ Vagrantfile created at {vagrantfile_path}")

if __name__ == "__main__":
    main()
