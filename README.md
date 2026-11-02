# Konsultacje: kod z laboratoriów

**Projektowanie aplikacji webowych · SWPS · 2026/2027**

Aplikacja do rezerwacji konsultacji psychologicznych, którą budujemy krok po kroku na zajęciach.
Instrukcje, zadania i slajdy znajdziesz w repozytorium
👉 [kropiak/swps-aplikacje-www-materialy](https://github.com/kropiak/swps-aplikacje-www-materialy)

## Gałęzie

Każda gałąź zawiera kod w stanie **po zakończeniu** danego labu. Kolejne gałęzie zawierają wszystko z poprzednich.

| Gałąź | Stan po labie |
|---|---|
| [`lab-01`](../../tree/lab-01) | Środowisko: skrypt powitalny, `requirements.txt`, `.gitignore` |
| [`lab-02`](../../tree/lab-02) | Git i GitHub |
| [`lab-03`](../../tree/lab-03) | Projekt Django, pierwsze modele, panel admina |
| `lab-04` | Pełny model domeny, dostosowany admin, widoki i routing |
| `lab-05` | Szablony (Tailwind), formularz rezerwacji |
| `lab-06` | REST API (DRF), Swagger |
| `lab-07` | Logowanie, rejestracja, tokeny, uprawnienia |
| `extra-openspec` | (extra) Spec-Driven Development z OpenSpec |
| `extra-frontend` | (extra) Frontend Vue 3 + Vite w Dockerze |

## Jak z tego korzystać?

Aplikację piszesz **we własnym repozytorium**. To repozytorium służy do porównywania i ratunku:

- **podgląd:** wybierz gałąź na GitHubie (przycisk z nazwą gałęzi nad listą plików),
- **pobranie gałęzi jako ZIP:** wybierz gałąź → **Code → Download ZIP**,
- **sklonowanie gałęzi:** `git clone -b lab-04 https://github.com/kropiak/swps-aplikacje-www-labs.git lab-04`

## Uruchomienie gałęzi lokalnie

💻 Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

🍎 macOS (zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Od labu 3 dodatkowo:
```bash
python manage.py migrate
python manage.py runserver
```

## Koło ratunkowe: GitHub Codespaces

Jeśli instalacja na Twoim komputerze sprawia problemy, możesz pracować w przeglądarce:

1. Zaloguj się na GitHub i otwórz to repozytorium (albo swoje, jeśli skopiowałeś do niego folder `.devcontainer`).
2. Wybierz gałąź, potem **Code → Codespaces → Create codespace on …**
3. Po minucie–dwóch otworzy się VS Code w przeglądarce z gotowym Pythonem i zainstalowanymi bibliotekami.
4. Serwer Django uruchomiony poleceniem `python manage.py runserver` będzie dostępny przez zakładkę **Ports**
   (VS Code sam zaproponuje otwarcie w przeglądarce).

> Darmowy limit Codespaces to kilkadziesiąt godzin miesięcznie (więcej z [GitHub Education](https://education.github.com/pack)).
> Po pracy zatrzymaj codespace: **Code → Codespaces → … → Stop codespace**.
