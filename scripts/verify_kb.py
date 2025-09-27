#!/usr/bin/env python3
import json, glob, sys, os

ROOT = os.path.dirname(os.path.dirname(__file__))

def main():
    idx_path = os.path.join(ROOT, "docs/knowledge/index.json")
    with open(idx_path, "r") as f:
        idx = json.load(f)

    missing = []
    for col in idx.get("collections", []):
        for p in col.get("paths", []):
            matches = glob.glob(os.path.join(ROOT, p), recursive=True)
            if not matches:
                missing.append(p)

    if missing:
        print("Missing/empty paths:")
        for m in missing:
            print(" -", m)
        sys.exit(1)
    print("KB OK")

if __name__ == "__main__":
    main()
