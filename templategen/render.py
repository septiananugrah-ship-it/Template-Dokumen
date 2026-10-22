"""Konversi .pptx -> PDF -> PNG memakai LibreOffice dan Poppler."""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path


def soffice_bin():
    for name in ("soffice", "libreoffice"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("LibreOffice (soffice) tidak ditemukan")


def to_pdf(pptx: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [soffice_bin(), f"-env:UserInstallation=file://{profile}", "--headless",
             "--convert-to", "pdf", "--outdir", str(outdir), str(pptx)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    return outdir / (pptx.stem + ".pdf")


def to_png(pdf: Path, outdir: Path, dpi=110, first=None, last=None) -> list[Path]:
    outdir.mkdir(parents=True, exist_ok=True)
    prefix = outdir / pdf.stem
    cmd = ["pdftoppm", "-png", "-r", str(dpi)]
    if first:
        cmd += ["-f", str(first)]
    if last:
        cmd += ["-l", str(last)]
    subprocess.run(cmd + [str(pdf), str(prefix)], check=True)
    return sorted(outdir.glob(pdf.stem + "-*.png"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
