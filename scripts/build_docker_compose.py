#!/usr/bin/env python3
import os, argparse

TEMPLATE = """
version: "3.9"
services:
  {name}:
    container_name: {name}
    image: {image}
    ports:
      - "{port}:80"
    command: >
      bash -c "
      {'apt-get update && apt-get install -y python3 python3-pip &&' if install_python else ''}
      pip install {packages} &&
      tail -f /dev/null
      "
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--container-name", required=True)
    parser.add_argument("--base-image", required=True)
    parser.add_argument("--install-python", required=True)
    parser.add_argument("--pip-packages", required=False)
    parser.add_argument("--expose-port", required=False, default="8080")

    args = parser.parse_args()
    container_dir = f"containers/{args.container_name}"
    os.makedirs(container_dir, exist_ok=True)

    content = TEMPLATE.format(
        name=args.container_name,
        image=args.base_image,
        port=args.expose_port,
        install_python=args.install_python.lower() == "true",
        packages=args.pip_packages or ""
    )

    compose_path = os.path.join(container_dir, "docker-compose.yml")
    with open(compose_path, "w") as f:
        f.write(content)

    print(f"[OK] ✅ Docker Compose file created at {compose_path}")
