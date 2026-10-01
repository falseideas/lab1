import json
import os
import platform
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path


def collect_os_info():
    system = platform.system()

    if system == "Windows":
        os_name = "Windows"
    elif system == "Darwin":
        os_name = "macOS"
    elif system == "Linux":
        os_name = "Linux"
    else:
        os_name = system

    info = {
        "operating_system": {
            "name": os_name,
            "system": system,
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
        },
        "python": {
            "version": platform.python_version(),
            "implementation": platform.python_implementation(),
            "executable": sys.executable,
        },
        "computer": {
            "hostname": socket.gethostname(),
            "cpu_count": os.cpu_count(),
        },
        "environment": {
            "current_directory": str(Path.cwd()),
            "home_directory": str(Path.home()),
        },
        "collection": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
        }
    }

    return info


def main():
    data = collect_os_info()

    output_file = Path("os_info.json")

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"ОС: {data['operating_system']['name']}")
    print(f"Результат сохранён в: {output_file.resolve()}")


if __name__ == "__main__":
    main()
