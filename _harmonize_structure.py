#!/usr/bin/env python3
"""Harmonise la structure des sous-sections du chapitre 2.

Quatre opérations mécaniques :
1. Corrige deux labels mal numérotés (D3 et D4)
2. Renomme "Le test contemporain" → "Test contemporain" (D2)
3. Renomme "Confrontation à l'évidence" → "Test contemporain" (D3, D6, D7, D8, D9, D10)
4. Supprime les sous-sections "Le champ..." dupliquées (D6, D9, D10)
   — artefact où le titre est répété après un bloc de commentaires draft

Usage:
    python3 _harmonize_structure.py --dry-run
    python3 _harmonize_structure.py
"""

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent
TARGET = ROOT / "Chapters" / "Chapter02.tex"

REPLACEMENTS = [
    # (old, new, expected_count)
    (r"\label{sec:d4-travail}", r"\label{sec:d3-travail}", 1),
    (r"\label{sec:d2-reseau}",  r"\label{sec:d4-reseau}",  1),
    (r"\subsubsection{Le test contemporain}",
     r"\subsubsection{Test contemporain}", 1),
    (r"\subsubsection{Confrontation à l'évidence}",
     r"\subsubsection{Test contemporain}", 6),
]

DUPLICATE_TITLES = [
    "\\subsubsection{Le champ~: les conditions structurelles de la coordination par les prix}",
    "\\subsubsection{Le champ~: un angle mort réciproque}",
    "\\subsubsection{Le champ~: les conditions de production du changement technique}",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not TARGET.exists():
        print(f"ERREUR : {TARGET} introuvable", file=sys.stderr)
        sys.exit(1)

    text = TARGET.read_text(encoding="utf-8")
    original_len = len(text)
    print(f"Avant : {original_len:,} caractères\n")

    # Étape 1 : remplacements
    for old, new, expected in REPLACEMENTS:
        count = text.count(old)
        mark = "✓" if count == expected else "✗"
        short = old.replace("\\subsubsection", "sub").replace("\\label", "lbl")
        print(f"  {mark} {short[:55]:55s} : {count} occ. (attendu {expected})")
        if count != expected:
            print(f"\nARRÊT : comptage inattendu pour '{old}'", file=sys.stderr)
            sys.exit(1)
        text = text.replace(old, new)

    print()

    # Étape 2 : suppression des sous-sections dupliquées
    for line in DUPLICATE_TITLES:
        first = text.find(line)
        if first == -1:
            print(f"  ✗ introuvable : {line[:60]}")
            continue
        second = text.find(line, first + len(line))
        if second == -1:
            print(f"  ✗ pas de doublon : {line[:60]}")
            continue
        end = second + len(line)
        if end < len(text) and text[end] == "\n":
            end += 1
        text = text[:second] + text[end:]
        print(f"  ✓ doublon supprimé : ...{line[35:80]}")

    print()
    print(f"Après : {len(text):,} caractères (delta {len(text) - original_len:+,})")

    if args.dry_run:
        print("\n[DRY RUN] Aucun fichier modifié.")
        return

    backup = TARGET.with_suffix(".tex.bak")
    shutil.copy2(TARGET, backup)
    TARGET.write_text(text, encoding="utf-8")
    print(f"\n✓ Sauvegarde : {backup.name}")
    print(f"✓ Chapter02.tex mis à jour")


if __name__ == "__main__":
    main()
