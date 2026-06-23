#!/usr/bin/env python3
"""Fusionne les petits .bib orphelins dans Bibliography.bib.

Usage:
    python3 _merge_bib.py --dry-run   # rapport seul, aucune écriture
    python3 _merge_bib.py             # fusion + sauvegarde Bibliography.bib.bak

Comportement sur les conflits (même clé, contenu différent) :
la version de Bibliography.bib est conservée, l'autre est ignorée
et listée dans _bib_conflicts.txt pour arbitrage manuel.

AMiede_Publications.bib n'est PAS traité : c'est la biblio personnelle
livrée avec le template classicthesis, à examiner séparément.
"""

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
TARGET = ROOT / "Bibliography.bib"

SOURCES = [
    "d1_bib_entries.bib",
    "d2_bib_entries.bib",
    "d6_bib_entries.bib",
    "lectures_25mars.bib",
    "longo_kittler_refs.bib",
]

ENTRY_START = re.compile(r"^\s*@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


def parse_entries(text):
    """Retourne [(key, type, raw_entry)] en équilibrant les accolades.

    Ignore @comment, @string, @preamble (pas des entrées bibliographiques).
    """
    entries = []
    for match in ENTRY_START.finditer(text):
        etype = match.group(1).lower()
        if etype in ("comment", "string", "preamble"):
            continue
        start = match.start()
        key = match.group(2)
        depth = 0
        i = start
        while i < len(text):
            c = text[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    entries.append((key, etype, text[start : i + 1]))
                    break
            i += 1
    return entries


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target_text = TARGET.read_text(encoding="utf-8")
    target_entries = {k: raw for k, _, raw in parse_entries(target_text)}
    print(f"Bibliography.bib : {len(target_entries)} entrées indexées\n")

    to_append = []
    duplicates = []
    conflicts = []
    seen_in_sources = set()

    for src_name in SOURCES:
        src = ROOT / src_name
        if not src.exists():
            print(f"  ⚠ {src_name} : absent du repo")
            continue
        src_text = src.read_text(encoding="utf-8")
        src_entries = parse_entries(src_text)
        new_count = 0
        for key, etype, raw in src_entries:
            if key in target_entries:
                if normalize(target_entries[key]) == normalize(raw):
                    duplicates.append((src_name, key))
                else:
                    conflicts.append((src_name, key, target_entries[key], raw))
            elif key in seen_in_sources:
                duplicates.append((src_name, key))
            else:
                to_append.append((src_name, key, etype, raw))
                seen_in_sources.add(key)
                new_count += 1
        print(f"  {src_name} : {len(src_entries)} entrées, {new_count} nouvelles")

    print()
    print(f"À ajouter         : {len(to_append)}")
    print(f"Doublons exacts   : {len(duplicates)}")
    print(f"Conflits          : {len(conflicts)}")

    if conflicts:
        report = ROOT / "_bib_conflicts.txt"
        with report.open("w", encoding="utf-8") as f:
            f.write(f"# {len(conflicts)} conflits — clé identique, contenu différent\n")
            f.write("# La version de Bibliography.bib est conservée par défaut.\n\n")
            for src, key, existing, new in conflicts:
                f.write(f"=== {key} (source: {src}) ===\n\n")
                f.write("--- Bibliography.bib (gardé) ---\n")
                f.write(existing + "\n\n")
                f.write("--- Source (ignoré) ---\n")
                f.write(new + "\n\n\n")
        print(f"\nDétail des conflits écrit dans {report.name}")

    if args.dry_run:
        print("\n[DRY RUN] Aucun fichier modifié.")
        return

    if to_append:
        backup = TARGET.with_name("Bibliography.bib.bak")
        shutil.copy2(TARGET, backup)
        print(f"\nSauvegarde : {backup.name}")

        block = "\n\n% " + "─" * 75 + "\n"
        block += f"% Fusion automatique des .bib orphelins ({len(to_append)} entrées)\n"
        block += "% " + "─" * 75 + "\n"
        current_src = None
        for src, key, etype, raw in to_append:
            if src != current_src:
                block += f"\n% --- depuis {src} ---\n\n"
                current_src = src
            block += raw + "\n\n"
        with TARGET.open("a", encoding="utf-8") as f:
            f.write(block)
        print(f"✓ {len(to_append)} entrées ajoutées à Bibliography.bib")

    print("\nAprès compilation réussie, suppression suggérée :")
    for src in SOURCES:
        if (ROOT / src).exists():
            print(f"  git rm {src}")
    print("  git rm _patch_bib_missing.py        # script ad-hoc déjà exécuté")
    print("  git rm _bib_hilbert_spreng.txt      # fusion d'avril")
    print("  git rm ch1_s03_calcul_new_refs.bib  # marqué obsolète par toi-même")
    print(
        "\nÀ examiner séparément : AMiede_Publications.bib"
        " (biblio André Miede, template classicthesis)"
    )


if __name__ == "__main__":
    main()
