#!/usr/bin/env python3
"""Replace old D5 with new D5 in Chapter02.tex"""
import os

base = os.path.dirname(os.path.abspath(__file__))
ch02_path = os.path.join(base, 'Chapters', 'Chapter02.tex')
new_d5_path = os.path.join(base, 'Chapters', 'd5_v2_complete.tex')

# Read files
with open(ch02_path, 'r', encoding='utf-8') as f:
    content = f.read()

with open(new_d5_path, 'r', encoding='utf-8') as f:
    new_d5_raw = f.read()

# Extract just the D5 content from d5_v2_complete.tex (skip comment headers)
start_marker = r'\subsection{Demande, préférences et élasticité}'
new_start = new_d5_raw.find(start_marker)
new_end = new_d5_raw.rfind(r'\clearpage') + len(r'\clearpage')
new_d5 = new_d5_raw[new_start:new_end] + '\n\n'

# Find old D5 boundaries in Chapter02.tex
d5_start = content.find(start_marker)
d6_marker = r'\subsection{Signal de prix et structure des marchés}'
d6_start = content.find(d6_marker)

if d5_start == -1:
    print("ERROR: Could not find D5 start")
    exit(1)
if d6_start == -1:
    print("ERROR: Could not find D6 start")
    exit(1)

old_d5 = content[d5_start:d6_start]
print(f"Old D5: {len(old_d5)} chars")
print(f"New D5: {len(new_d5)} chars")

# Backup
backup_path = ch02_path + '.pre_d5_rewrite'
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Backup saved to {backup_path}")

# Replace
result = content[:d5_start] + new_d5 + content[d6_start:]
with open(ch02_path, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"Done. Chapter02.tex updated ({len(result)} chars)")
print(f"Old D5 had 'deux manières': {'deux manières' in old_d5}")
print(f"New D5 has 'trois manières': {'trois manières' in new_d5}")
print(f"New D5 has 'H-D5.3': {'H-D5.3' in new_d5}")
print(f"New D5 has 'Duranton': {'duranton' in new_d5}")
