---
name: thesis-dimension-writing
description: Guide de rédaction, relecture et blindage académique pour les dimensions du chapitre 2 de la thèse DIGICLIM. Appliquer ce skill dès que Rémi travaille sur une section dimensionnelle (D1 à D10) du chapitre 2, qu'il s'agisse de rédiger, relire, restructurer ou corriger le ton. Déclencher aussi quand il dit 'relecture dimension', 'même traitement que D1', 'appliquer le skill', 'corriger le ton', 'on fait comme D1', ou quand il uploade un PDF annoté portant sur le chapitre 2. Ce skill encode les leçons de D1 ET les critiques de quatre reviewers externes pour produire des dimensions robustes dès le premier jet. DISTINCT de scientific-interlocutor (jugement intellectuel) et se-academic-writing (style prose). Ce skill porte sur la STRUCTURE, le STATUT ÉPISTÉMIQUE et le BLINDAGE ACADÉMIQUE.
---

# Rédaction des dimensions — Chapitre 2

Leçons extraites de la relecture de D1, des retours de quatre reviewers externes, et des corrections appliquées (mai 2026). S'applique à D1–D10.


## 1. Architecture d'une dimension

Séquence fixe. Ne pas mélanger les étapes.

1. **Le champ** — Question économique que la dimension ouvre. Définitions en questions simples. Ancrage littérature. Si la catégorie centrale est large, le reconnaître et expliquer où réside le pouvoir discriminant (dans les caractéristiques appliquées aux couches, pas dans la catégorie elle-même).
2. **Grille / table** — AVANT les mécanismes. Colonnes simples (définition en question + variation entre couches ou sous-catégories). Pas de colonne « cadre théorique » redondante avec le texte. Forcer `[!ht]`.
3. **Ce que le matériau révèle** — Régularités observées, posées comme constats AVANT d'être nommées comme mécanismes. Le lecteur voit les patterns, puis on les formalise. C'est ici que le travail d'analyse est montré au lecteur.
4. **Mécanismes** — Chacun suit la progression interne (§2). Chacun se termine par une hypothèse numérotée isolée. Signaler les interactions entre mécanismes quand elles existent.
5. **Test contemporain** — Chaque paragraphe ouvre par « Pour M1 (H-DX.1) ». Données chiffrées, sourcées, datées. Sobre.
6. **Fait stylisé** — Court. Chaque point renvoie à l'hypothèse H-DX.Y. Pas de re-listing des références.


## 2. Progression interne d'un mécanisme

C'est le point critique. La progression OBSERVATION → THÉORIE → HYPOTHÈSE, jamais l'inverse.

1. **Observation** — Ce qu'on voit dans le matériau historique ou contemporain. Concret, daté, sourcé. Le lecteur a un ancrage avant toute théorie.
2. **Pourquoi c'est intéressant économiquement** — Cadre théorique, JUSTIFIÉ par le problème posé (quel problème ce cadre résout, quelle est sa limite, pourquoi on l'étend). Pas de name-drop.
3. **Ce qui est nouveau** — Phénomène contemporain qui rend le cadre existant insuffisant. Nommer la technologie, dater son émergence (ex : « les modèles de fondation à grande échelle à partir de GPT-3 en 2020 »), sourcer avec des données chiffrées.
4. **Formulation du mécanisme** — Proposition de la thèse, statut épistémique explicite.
5. **Hypothèse isolée** — `\paragraph{Hypothèse H-DX.Y}` + `\emph{}` + conditions d'activation + renvoi au test (sans mentionner de numéro de chapitre).


## 3. Ton et verbes

### Faire
- « L'analyse historique suggère que... » — inférence à partir de cas
- « X et Y montrent que... » — résultat empirique publié
- « X et Y établissent que... » — résultat formel
- « Dans une lecture néoclassique — par exemple Arrow... » — introduction d'une école
- « L'hypothèse propre à cette thèse est que... » — proposition testable
- « C'est une question ouverte, pas un résultat » — point non tranché
- « Le matériau historique est cohérent avec... » — lien prudent entre cas et théorie

### Ne pas faire
- « Le chapitre X montre / testera... » → nommer le contenu (« l'analyse historique », « la modélisation », « l'analyse énergétique », « les scénarios »)
- « La voie néoclassique traite... » → trop propriétaire, on n'est pas porte-parole d'une école
- « Les conditions d'activation sont précises » → qui a dit ça ? Reformuler
- « Le matériau confirme que... » → un cas ne confirme rien de général ; « suggère » ou « est cohérent avec »
- « Trois mécanismes émergent » sans avoir montré le travail d'analyse avant
- « depuis 2020 » ou « le régime contemporain » sans nommer ni dater la technologie


## 4. Statut épistémique — trois catégories à ne jamais mélanger

| Catégorie | Exemple | Verbe |
|---|---|---|
| **Établi** | Résultat empirique publié (Juhász, Kaplan, Haskel-Westlake) | « montrent », « établissent » |
| **Observation propre** | Régularité extraite du croisement matériau × grille | « l'analyse révèle », « la confrontation fait apparaître » |
| **Hypothèse propre** | Proposition testable formulée par la thèse | Paragraphe dédié, italique, numéroté H-DX.Y |

Toute phrase qui mélange deux catégories doit être décomposée. Ex : « La non-rivalité produit une tension qui s'active de manière hétérogène » mélange un fait établi (non-rivalité → tension, Arrow) et une hypothèse propre (hétérogénéité intra-bien). Séparer.


## 5. Blindage académique

### 5.1 Revendiquer ce qui est à nous
- Quand on fait une **synthèse** à partir de plusieurs auteurs (ex : tripartition des architectures d'excluabilité), le dire explicitement : « cette tripartition est notre synthèse à partir de... — aucun de ces auteurs ne la propose sous cette forme ».
- Quand on **étend** un cadre (ex : putty-clay multi-couches à partir de Johansen), distinguer ce qui vient de l'auteur original et ce qui est notre extension.
- Ne pas masquer l'originalité derrière une note de renvoi. Si c'est un outil qu'on construit, le revendiquer dans le texte principal.

### 5.2 Citer les précurseurs, resserrer l'originalité
- Ne jamais revendiquer qu'une idée est absente de la littérature sans avoir vérifié. Nommer les précurseurs et préciser en quoi notre contribution est distincte.
- Formulation-type : « L'idée de X n'est pas sans précédent : A (année) propose Y, B (année) propose Z. Ce qui est propre à l'approche ici développée, c'est [contribution précise]. »

### 5.3 Ancrage théorique honnête
- Ne pas revendiquer une filiation théorique quand l'emprunt est seulement méthodologique (même structure formelle, pas même théorie). Le dire : « L'emprunt est méthodologique : [ce qu'on prend]. »
- Si le cadre qu'on utilise est plus proche d'un auteur B que de l'auteur A qu'on cite, le dire (ex : « L'usage ici est plus proche de Rosen que de Lancaster »).

### 5.4 Distinguer les niveaux de propriété
- Les caractéristiques ou variables d'un cadre ne sont pas toutes de même nature. Exemples de niveaux : propriété physique du bien, propriété cognitive du savoir, propriété institutionnelle du régime d'accès, propriété systémique de l'architecture, propriété temporelle du processus.
- Les caractéristiques ne sont généralement pas indépendantes : elles interagissent (la codifiabilité influence l'excluabilité technique, le régime temporel dépend de la complémentarité). Si la grille n'est pas un espace orthogonal, le dire.

### 5.5 Précision des revendications quantitatives
- Un ratio extrême n'est pas forcément sans précédent inter-sectoriel. Ce qui peut être spécifique, c'est la *conjonction* du ratio avec d'autres conditions. Préciser.
- Tout chiffre doit être sourcé : référence académique ou base de données identifiée (Epoch AI, IEA, etc.), avec année des données.
- Pas de « plusieurs centaines de millions » sans source. Pas de « croissance rapide » sans taux.

### 5.6 Interactions entre mécanismes
- Les mécanismes d'une même dimension peuvent interagir (ex : M3 rigidifie M1). Le signaler, même brièvement, et renvoyer à la section d'intégration si le développement relève d'un autre niveau d'analyse.
- Les mécanismes de dimensions différentes peuvent aussi interagir : le noter quand c'est évident pour préparer la section 2.2 (boucles de rétroaction).

### 5.7 Termes inventés — protocole obligatoire
Pour chaque terme nouveau :
1. **Reconnaître la tension** avec le sens technique existant du mot si applicable (ex : « compression » au sens de Shannon ≠ usage ici). Ne pas contourner la tension, la reconnaître.
2. **Argument positif** — ce que le mot capture que les alternatives ne capturent pas. Pas seulement « les autres ne marchent pas » mais « voici ce que ce mot désigne positivement ».
3. **Passer en revue les candidats existants** — au moins 3-4, avec pour chacun une phrase sur pourquoi il ne convient pas.
4. **Signaler explicitement** que c'est une proposition de la thèse, pas un concept établi.
5. **Ne pas réifier** — si le terme désigne une opération économique, ne pas glisser vers une ontologie (ex : un modèle ne « contient » pas du savoir comprimé, il encode une distribution statistique utile).

### 5.8 Catégories larges
- Si une catégorie centrale est volontairement large, le reconnaître et localiser le pouvoir discriminant (dans les caractéristiques/couches, pas dans la catégorie).
- Formulation-type : « La catégorie est volontairement large : [objets très différents] n'obéissent pas aux mêmes dynamiques, mais participent du même système. Le pouvoir discriminant réside dans [outil d'analyse], pas dans la catégorie elle-même. »

### 5.9 Prudence épistémologique (Polanyi, cognition)
- Si on mobilise un concept philosophique (tacite/explicite, savoir/capacité fonctionnelle), préciser ce qui reste dans chaque catégorie et quelles sont les conséquences économiques de la distinction.
- Ne pas se contenter de « X reste valide » : dire pourquoi, et ce que ça implique concrètement (révisabilité, transférabilité, coût de modification).


## 6. Données et sources

### Principes
- Tout chiffre dans le texte doit avoir une source entre parenthèses ou en footnote.
- Préférer les bases de données systématiques (Epoch AI, IEA, OWID) aux chiffres isolés de presse.
- Dater les données : « en 2024 » ou « depuis 2010 », pas « actuellement ».
- Nommer les modèles, les entreprises, les technologies : pas « les modèles récents » mais « GPT-4, Gemini Ultra, Llama 3 ».
- Epoch AI est la référence pour le compute, les coûts d'entraînement, les tailles de modèles. Clé bib : `cottier_rising_2025` pour les coûts ; base Notable AI Models pour les tendances.

### Footnotes vs. texte
- Un chiffre qui fait partie de l'argument → dans le texte avec source.
- Une source qui documente systématiquement un phénomène sans être citée pour un résultat précis → en footnote (ex : « Epoch AI documente systématiquement ces trajectoires dans sa base Notable AI Models »).
- Une précision méthodologique ou une justification de choix terminologique → en footnote si elle dépasse deux phrases.


## 7. Références aux chapitres

Ne jamais écrire « le chapitre X ». Nommer le contenu :
- « L'analyse historique » (ch. 1)
- « L'analyse énergétique » / « les trajectoires énergétiques » (ch. 3)
- « La modélisation » / « les scénarios » (ch. 4)
- « L'analyse institutionnelle » (ch. 3 volet gouvernance)


## 8. Tables

- Définitions en questions simples : « Un agent qui utilise le bien empêche-t-il un autre de l'utiliser ? »
- Pas de colonne redondante avec le texte
- Table des mécanismes : Mécanisme | Caractéristiques mobilisées | Conditions d'activation | Hypothèse
- Forcer `[!ht]`
- Caption courte, sans phrases assertives (pas « les trois mécanismes structurels qui émergent de l'articulation... »)


## 9. Checklist avant validation

### Structure
- [ ] Progression de chaque mécanisme : observation → théorie → hypothèse
- [ ] Hypothèses isolées en `\paragraph{Hypothèse H-DX.Y}` + `\emph{}`
- [ ] « Ce que le matériau révèle » AVANT les mécanismes
- [ ] Test contemporain et fait stylisé renvoient aux H-DX.Y
- [ ] Interactions entre mécanismes signalées

### Ton
- [ ] Aucune référence à « chapitre X »
- [ ] Verbes calibrés sur le statut épistémique (montrent / suggèrent / l'hypothèse est que)
- [ ] Pas de « confirme » avec un seul cas
- [ ] Lectures en mode ouvert (« dans une lecture X — par exemple Y... »)

### Blindage
- [ ] Précurseurs cités, originalité resserrée sur la contribution réelle
- [ ] Synthèses propres revendiquées comme telles
- [ ] Niveaux de propriété distingués si les caractéristiques sont hétérogènes
- [ ] Termes inventés : protocole complet (tension reconnue + argument positif + candidats écartés + statut signalé)
- [ ] Catégories larges reconnues, pouvoir discriminant localisé
- [ ] Emprunt méthodologique ≠ filiation théorique : distingué
- [ ] Revendications quantitatives sourcées et nuancées (conjonction vs. ratio seul)

### Données
- [ ] Tout chiffre a une source
- [ ] Technologies nommées et datées
- [ ] Tables avec définitions simples et caption sobre
