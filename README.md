# python-tdd-basics

Übungsprojekt zum Einstieg in Test-Driven Development (TDD) mit Python und pytest.

## Inhalt

- `rechner.py` – einfache Rechner-Funktionen (Addition, Division)
- `test_rechner.py` – zugehörige Tests nach dem Red/Green/Refactor-Prinzip

## Konzept

TDD folgt dem Zyklus:
1. **Red** – Test schreiben, der fehlschlägt
2. **Green** – minimalen Code schreiben, der den Test besteht
3. **Refactor** – Code aufräumen, Tests bleiben grün

## Setup
```bash
pip install pytest pytest-cov
pytest --cov=rechner
```
