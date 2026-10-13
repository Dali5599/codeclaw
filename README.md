# ⚡ CodeClaw - Autonomous AI Code Generation & Refactoring Engine

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![Built by Requin](https://img.shields.io/badge/Built%20by-Requin%20Finisher-orange.svg)]()

> **CodeClaw** est un agent autonome de développement logiciel inspiré de Claude Code, OpenHands et Aider.
> Il combine un analyseur AST de code source, une boucle cognitive ReAct, un gestionnaire de patchs unifiés (diffs), une sandbox de commandes sécurisée, une CLI interactive Rich et un serveur Web / WebSocket pour piloter l'ingénierie logicielle en toute autonomie.

---

## 🎯 Fonctionnalités Clés
- 🧠 **Boucle ReAct Autonome** : Analyse, planification, implémentation et auto-guérison guidée par les tests unitaires.
- 🌳 **Indexation AST & Recherche de Symboles** : Compréhension instantanée des classes, fonctions, exports et dépendances.
- 🛡️ **Sandbox de Commandes Sécurisée** : Exécution de builds, tests et commandes bash avec isolation des timeouts.
- 📝 **Diff Engine Robuste** : Génération et application de patchs Git unifiés sans perte de données.
- 🖥️ **Double Interface** : CLI élégante (Rich Terminal) & Dashboard Web interactif (FastAPI + WebSocket).
- 🧪 **Quality Gate Strict** : Zéro régression acceptée, validation continue des suites de tests avant validation git.

---

## 🚀 Démarrage Rapide

```bash
# Installation
git clone https://github.com/Dali5599/codeclaw.git
cd codeclaw
pip install -e .

# Lancement du diagnostic
codeclaw doctor

# Afficher la version
codeclaw version
```

---

## 🗺️ Roadmap de Développement Autonome (50 Étapes)
Voir le fichier [`ROADMAP.md`](ROADMAP.md) pour suivre en temps réel l'avancement de chaque fonctionnalité développée par Requin Finisher.

---

## 📜 Licence
MIT License © 2026 Dali5599 & Requin.
