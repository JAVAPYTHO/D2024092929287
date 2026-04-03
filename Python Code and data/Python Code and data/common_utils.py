from pathlib import Path
from typing import Iterable
import pandas as pd


def project_root_from(start: Path, marker: str = "D2024092929287.pdf") -> Path:
    current = start.resolve()
    for p in [current, *current.parents]:
        if (p / marker).exists():
            return p
    return current.parent


def read_csv_auto(file_path: Path, encodings: Iterable[str] = ("utf-8", "ISO-8859-1", "GBK", "latin1")) -> pd.DataFrame:
    last_err = None
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except UnicodeDecodeError as e:
            last_err = e
    if last_err:
        raise last_err
    raise FileNotFoundError(f"无法读取文件: {file_path}")


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path
