"""Bangun paket produk digital siap jual.

    python build.py                 # semua paket
    python build.py sidang_skripsi  # satu paket
    python build.py --fast          # tanpa PDF/mockup (cek cepat file sumber saja)

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
    mod = importlib.import_module(f"paket.{slug}.package")
    pkg = mod.PACKAGE
    out = DIST / slug
    shutil.rmtree(out, ignore_errors=True)
    prod = out / pkg["folder"]
    mk = out / "marketing"
    tmp = out / "_render"
    for d in (prod, mk, tmp):
        d.mkdir(parents=True)
    if pkg.get("kind") == "docs":
        build_docs(slug, mod, pkg, out, prod, mk, tmp, fast)
    else:
        build_slides(slug, pkg, out, prod, mk, tmp, fast)
    finish(slug, pkg, out, prod, mk, tmp, fast)


def build_docs(slug, mod, pkg, out, prod, mk, tmp, fast):
    """Paket dokumen (Word): package.make(prod) -> [(label, aksen, [file, ...]), ...]."""
    groups = mod.make(prod)
    renders = []
    for label, accent, files in groups:
        pages = []
        for f in files:
            print("  ✓", f.relative_to(out))
            if fast:
                continue
            pdf = render.to_pdf(f, f.parent)
            pages += [Image.open(p).convert("RGB")
                      for p in render.to_png(pdf, tmp / f.stem, dpi=110)]
        renders.append((label, accent, pages))
    if fast:
        return
    for name, body in pkg["docs"].items():
        (prod / name).write_text(body.strip() + "\n", encoding="utf-8")
    firsts = [pages[0] for _, _, pages in renders]
    mockup.doc_cover_square(pkg, firsts, mk / "01-foto-utama.jpg")
    mockup.doc_banner(pkg, firsts, mk / "02-banner-gumroad.jpg")
    for i, (label, accent, pages) in enumerate(renders):
        mockup.doc_design_square(pkg, label, accent, pages,
                                 mk / f"{i + 3:02d}-desain-{i + 1}.jpg")
    rows = [[pages[j] for _, _, pages in renders] for j in range(len(renders[0][2]))]
    mockup.doc_contents_square(pkg, rows, mk / f"{len(renders) + 3:02d}-isi-paket.jpg")
    mockup.doc_preview_pdf([(label, pages) for label, _, pages in renders],
                           mk / f"Pratinjau-{pkg['folder']}.pdf", pkg["title"])


def build_slides(slug, pkg, out, prod, mk, tmp, fast):
    content = importlib.import_module(f"paket.{slug}.content")

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

    if fast:
        return
    for name, body in pkg["docs"].items():
        (prod / name).write_text(body.strip() + "\n", encoding="utf-8")
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


def finish(slug, pkg, out, prod, mk, tmp, fast):
    if fast:
        return
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
