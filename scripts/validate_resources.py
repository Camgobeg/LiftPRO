#!/usr/bin/env python3
"""Validate resource JSON files before the Forge build."""
import json
from pathlib import Path

root = Path("src/main/resources")
files = sorted(root.rglob("*.json")) if root.exists() else []
for path in files:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Invalid resource JSON: {path}: {exc}") from exc

print(f"Validated {len(files)} resource JSON file(s).")
