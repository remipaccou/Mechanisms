#!/usr/bin/env python3
"""Replace D10 section in Chapter02.tex with v0.3 content."""
import re, os

REPO = os.path.dirname(os.path.abspath(__file__))
CH2 = os.path.join(REPO, 'Chapters', 'Chapter02.tex')
D10 = os.path.join(REPO, 'Chapters', 'd10_innovation_v03.tex')

with open(CH2, 'r', encoding='utf-8') as f:
    content = f.read()

with open(D10, 'r', encoding='utf-8') as f:
    new_d10 = f.read()

# Find D10 section: starts with \clearpage + \subsection{Trajectoires d'innovation
# Ends just before % ====\n\clearpage\n\section{Mécanismes structurels}
start_pattern = r'% =+\n\\clearpage\n\\subsection\{Trajectoires d\'innovation et dépendance de sentier\}'
end_pattern = r'% =+\n\\clearpage\n\\section\{Mécanismes structurels\}'

start_match = re.search(start_pattern, content)
end_match = re.search(end_pattern, content)

if not start_match:
    print("ERROR: D10 section start not found")
    exit(1)
if not end_match:
    print("ERROR: Mécanismes structurels section not found")
    exit(1)

start_idx = start_match.start()
end_idx = end_match.start()

print(f"Old D10: chars {start_idx}-{end_idx} ({end_idx - start_idx} chars)")
print(f"New D10: {len(new_d10)} chars")

# Build new content
new_content = content[:start_idx] + new_d10 + '\n\n\n' + content[end_idx:]

# Backup
backup = CH2 + '.bak_d10_v01'
if not os.path.exists(backup):
    with open(backup, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Backup written to {backup}")

with open(CH2, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Chapter02.tex updated: {len(content)} -> {len(new_content)} chars")
print("Done.")
