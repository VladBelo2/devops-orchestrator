#!/usr/bin/env python3
import os
import argparse
import sys

TEMPLATE = """
services:
  {name}:
    container_name: {name}
    image: {image}
    ports:
      - "{port}:80"
    command: >
      bash -c "
      {provision_cmd}
      tail -f /dev/null
      "
"""

def validate_port(port):
    try:
        port = int(port)
        if 1 <= port <= 65535:
            return port
        else:
            raise ValueError
    except ValueError:
        print(f"[ERROR] ❌ Invalid port: {port}. Must be between 1–65535.")
        sys.exit(1)

def build_provision_command(install_python, install_nodejs, install_golang, pip_packages):
    commands = []

    if install_python:
        commands.append("apt-get update && apt-get install -y python3 python3-pip || true")

    if pip_packages:
        commands.append(f"pip install {pip_packages} || true")

    if install_nodejs:
        commands.append("curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs || true")

    if install_golang:
        commands.append("apt-get update && apt-get install -y golang-go || true")

    # Final keep-alive
    commands.append("tail -f /dev/null")

    return " && ".join(commands)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--container-name", required=True)
    parser.add_argument("--base-image", required=True)
    parser.add_argument("--install-python", required=False, default="false")
    parser.add_argument("--install-node", required=False, default="false")
    parser.add_argument("--install-go", required=False, default="false")
    parser.add_argument("--pip-packages", required=False, default="")
    parser.add_argument("--expose-port", required=False, default="8080")

    args = parser.parse_args()
    port = validate_port(args.expose_port)

    container_dir = f"containers/{args.container_name}"
    os.makedirs(container_dir, exist_ok=True)

    provision_cmd = build_provision_command(args)

    content = TEMPLATE.format(
        name=args.container_name,
        image=args.base_image,
        port=port,
        provision_cmd=provision_cmd
    )

    compose_path = os.path.join(container_dir, "docker-compose.yml")
    with open(compose_path, "w") as f:
        f.write(content)

    print(f"[OK] ✅ Docker Compose file created at: {compose_path}")

if __name__ == "__main__":
    main()
