"""Bangun paket produk digital siap jual.

    python build.py                 # semua paket
    python build.py sidang_skripsi  # satu paket
    python build.py --fast          # tanpa PDF/mockup (cek cepat .pptx saja)

Hasil di dist/<paket>/:
    <Nama>-v<versi>.zip   -> file untuk pembeli (PPTX + PDF + panduan)
    marketing/            -> mockup foto produk, PDF pratinjau, deskripsi jualan
"""
from __future__ import annotations

import argparse
import importlib
import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image

from templategen import mockup, render
from templategen.slides import Builder
from templategen.themes import THEMES

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"


def packages():
    return sorted(p.name for p in (ROOT / "paket").iterdir()
                  if (p / "package.py").exists())


def build_package(slug, fast=False):
    pkg = importlib.import_module(f"paket.{slug}.package").PACKAGE
    content = importlib.import_module(f"paket.{slug}.content")
    out = DIST / slug
    shutil.rmtree(out, ignore_errors=True)
    prod = out / pkg["folder"]
    mk = out / "marketing"
    tmp = out / "_render"
    for d in (prod, mk, tmp):
        d.mkdir(parents=True)

    renders = {}  # (deck, theme) -> list[PIL.Image]
    for deck_name, _label, specs, meta in content.DECKS:
        for t in THEMES:
            folder = prod / f"Tema {t.label}"
            folder.mkdir(exist_ok=True)
            pptx = folder / f"{deck_name}_{t.key}.pptx"
            Builder(t, meta).build(specs, pptx)
            print("  ✓", pptx.relative_to(out))
            if fast:
                continue
            pdf = render.to_pdf(pptx, folder)
            pngs = render.to_png(pdf, tmp / f"{deck_name}_{t.key}", dpi=110)
            renders[(deck_name, t.key)] = [Image.open(p).convert("RGB") for p in pngs]

    for name, body in pkg["docs"].items():
        (prod / name).write_text(body.strip() + "\n", encoding="utf-8")

    if fast:
        return
    main_deck = content.DECKS[0][0]
    covers = [renders[(main_deck, t.key)][0] for t in THEMES]
    mockup.cover_square(pkg, covers, mk / "01-foto-utama.jpg")
    mockup.banner(pkg, covers, mk / "02-banner-gumroad.jpg")
    picks = pkg["showcase"]
    for i, t in enumerate(THEMES):
        slides = renders[(main_deck, t.key)]
        mockup.theme_square(pkg, t, [slides[j] for j in picks[:3]],
                            mk / f"{i + 3:02d}-tema-{t.key}.jpg")
    grid = [[renders[(main_deck, t.key)][j] for j in pkg["grid"]] for t in THEMES]
    mockup.contents_square(pkg, grid, mk / f"{len(THEMES) + 3:02d}-isi-paket.jpg")
    mockup.preview_pdf([[renders[(main_deck, t.key)][j] for j in pkg["preview"]] for t in THEMES],
                       [t.label for t in THEMES], mk / f"Pratinjau-{pkg['folder']}.pdf",
                       pkg["title"])
    (mk / "deskripsi-jualan.md").write_text(pkg["description"].strip() + "\n", encoding="utf-8")
    shutil.rmtree(tmp)

    # salinan mockup di repo supaya bisa dilihat langsung di GitHub
    pv = ROOT / "preview" / slug
    shutil.rmtree(pv, ignore_errors=True)
    pv.mkdir(parents=True)
    for f in mk.iterdir():
        shutil.copy(f, pv / f.name)

    zpath = out / f"{pkg['folder']}-v{pkg['version']}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(prod.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(out))
    print("  ZIP", zpath.relative_to(ROOT), f"{zpath.stat().st_size / 1e6:.1f} MB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paket", nargs="*")
    ap.add_argument("--fast", action="store_true")
    a = ap.parse_args()
    for slug in a.paket or packages():
        print(f"[{slug}]")
        build_package(slug, a.fast)


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    main()
