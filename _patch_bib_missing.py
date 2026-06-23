#!/usr/bin/env python3
"""Ajout des 3 entrées bib manquantes dans Bibliography.bib"""

path = "/Users/remipaccou/PhD/Overleaf/Thesis/Bibliography.bib"
with open(path, "r", encoding="utf-8") as f:
    bib = f.read()

ENTRIES = """

% ─────────────────────────────────────────────────────────────────────────────
% Ajout 18 avril 2026 — clés manquantes pour Introduction.tex
% ─────────────────────────────────────────────────────────────────────────────

@book{helpman_general_1998,
  author    = {Helpman, Elhanan},
  title     = {General Purpose Technologies and Economic Growth},
  year      = {1998},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
}

@book{grubler_rise_1990,
  author    = {Gr{\\\"u}bler, Arnulf},
  title     = {The Rise and Fall of Infrastructures: Dynamics of Evolution and Technological Change in Transport},
  year      = {1990},
  publisher = {Physica-Verlag},
  address   = {Heidelberg},
}

@book{grubler_technology_1998,
  author    = {Gr{\\\"u}bler, Arnulf},
  title     = {Technology and Global Change},
  year      = {1998},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
}
"""

bib += ENTRIES

with open(path, "w", encoding="utf-8") as f:
    f.write(bib)

print(f"✅ 3 entrées ajoutées à Bibliography.bib ({len(bib)} chars)")
