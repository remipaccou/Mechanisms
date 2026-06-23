#!/usr/bin/env python3
"""Fusionne les .bib orphelins dans Bibliography.bib — politique v2.

Différence avec _merge_bib.py :
    v1 : Bibliography.bib gagne tous les conflits.
    v2 : version la plus enrichie gagne (mesure : nombre de champs structurés).
         En cas d'égalité de champs, source gagne (travaillée plus récemment).

Usage:
    python3 _merge_bib_v2.py --dry-run   # rapport seul
    python3 _merge_bib_v2.py             # applique + sauvegarde .bak2

AMiede_Publications.bib n'est PAS traité (template André Miede, à part).
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


def count_fields(entry):
    """Nombre de champs structurés (lignes 'champ = valeur')."""
    return len(re.findall(r"^\s+\w+\s*=", entry, re.MULTILINE))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    target_text = TARGET.read_text(encoding="utf-8")
    target_entries = {k: raw for k, _, raw in parse_entries(target_text)}
    print(f"Bibliography.bib : {len(target_entries)} entrées indexées\n")

    # Détecter les clés dupliquées dans Bibliography.bib (doublons natifs)
    all_keys_in_target = [k for k, _, _ in parse_entries(target_text)]
    from collections import Counter
    target_key_counts = Counter(all_keys_in_target)
    native_dups = {k: c for k, c in target_key_counts.items() if c > 1}
    if native_dups:
        print(f"⚠ Doublons natifs dans Bibliography.bib (à nettoyer manuellement) :")
        for k, c in native_dups.items():
            print(f"    {k} ({c}× présent)")
        print()

    to_append = []
    duplicates = []
    replacements = []  # remplacer dans target
    target_wins = []   # target plus riche, on garde
    seen_in_sources = set()

    for src_name in SOURCES:
        src = ROOT / src_name
        if not src.exists():
            print(f"  ⚠ {src_name} : absent")
            continue
        src_text = src.read_text(encoding="utf-8")
        src_entries = parse_entries(src_text)
        new_count = 0
        replace_count = 0
        keep_count = 0
        for key, etype, raw in src_entries:
            if key in target_entries:
                if normalize(target_entries[key]) == normalize(raw):
                    duplicates.append((src_name, key))
                else:
                    # Conflit : politique "le plus enrichi gagne"
                    n_target = count_fields(target_entries[key])
                    n_src = count_fields(raw)
                    target_compact = n_target == 0  # tout sur une ligne
                    if n_src > n_target or (n_src == n_target and n_src > 0) or (target_compact and n_src > 0):
                        if key in native_dups:
                            print(f"  ⚠ skip {key} (doublon natif dans target)")
                        else:
                            replacements.append((src_name, key, target_entries[key], raw))
                            replace_count += 1
                    else:
                        target_wins.append((src_name, key))
                        keep_count += 1
            elif key in seen_in_sources:
                duplicates.append((src_name, key))
            else:
                to_append.append((src_name, key, etype, raw))
                seen_in_sources.add(key)
                new_count += 1
        print(f"  {src_name:30s} : {len(src_entries):3d} entrées | "
              f"{new_count:3d} nouvelles | {replace_count:3d} remplacements | "
              f"{keep_count:3d} target gardé")

    print()
    print(f"À ajouter (nouvelles)        : {len(to_append)}")
    print(f"Remplacements dans target    : {len(replacements)}")
    print(f"Target plus riche, gardée    : {len(target_wins)}")
    print(f"Doublons exacts (ignorés)    : {len(duplicates)}")

    if args.dry_run:
        print("\n[DRY RUN] Aucun fichier modifié.")
        return

    if not replacements and not to_append:
        print("\nRien à modifier.")
        return

    # Sauvegarde
    backup = TARGET.with_name("Bibliography.bib.bak2")
    shutil.copy2(TARGET, backup)
    print(f"\nSauvegarde : {backup.name}")

    # Appliquer les remplacements via str.replace (avec vérification d'unicité)
    modified = target_text
    failed = []
    for src_name, key, old_raw, new_raw in replacements:
        count = modified.count(old_raw)
        if count == 1:
            modified = modified.replace(old_raw, new_raw, 1)
        else:
            failed.append((key, count))

    if failed:
        print(f"\n⚠ {len(failed)} remplacements échoués (non unique) :")
        for k, c in failed:
            print(f"    {k} ({c} occurrences)")

    # Ajouter les nouvelles entrées en bloc à la fin
    if to_append:
        block = "\n\n% " + "─" * 75 + "\n"
        block += f"% Fusion v2 — {len(to_append)} nouvelles entrées\n"
        block += "% " + "─" * 75 + "\n"
        current_src = None
        for src, key, etype, raw in to_append:
            if src != current_src:
                block += f"\n% --- depuis {src} ---\n\n"
                current_src = src
            block += raw + "\n\n"
        modified += block

    TARGET.write_text(modified, encoding="utf-8")
    n_replaced = len(replacements) - len(failed)
    print(f"✓ {n_replaced} entrées remplacées, {len(to_append)} ajoutées")
    print(f"Taille : {len(target_text):,} → {len(modified):,} chars")

    print("\nAprès compilation réussie, suppression suggérée :")
    for src in SOURCES:
        if (ROOT / src).exists():
            print(f"  git rm {src}")
    print("  git rm ch1_s03_calcul_new_refs.bib  # déjà vide (commentaire seul)")
    print("  git rm _test_write.tex              # fichier test maladroit, à nettoyer")
    print("\nÀ examiner séparément : AMiede_Publications.bib (template, laissé à part)")


if __name__ == "__main__":
    main()
