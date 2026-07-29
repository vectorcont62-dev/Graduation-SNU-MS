from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path


def main() -> None:
    source = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    rows = []
    with zipfile.ZipFile(source) as zf:
        for info in sorted(zf.infolist(), key=lambda item: item.filename):
            data = zf.read(info.filename)
            rows.append(
                {
                    "path": info.filename,
                    "size": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                }
            )
    output.write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"parts={len(rows)}")


if __name__ == "__main__":
    main()
