"""Skrypt powitalny: sprawdza, czy środowisko działa."""

import sys

from rich.console import Console
from rich.table import Table

console = Console()

SPECIALISTS = [
    ("Anna", "Nowak", "Terapia poznawczo-behawioralna", "online"),
    ("Piotr", "Wiśniewski", "Psychologia dziecięca", "stacjonarnie"),
    ("Maria", "Zielińska", "Terapia par", "online"),
    ("Ewa", "Lis", "Psychoterapia psychodynamiczna", "stacjonarnie"),
]


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    console.print(f"[bold green]Działa![/] Python {sys.version.split()[0]}")
    if in_venv:
        console.print("Środowisko wirtualne: [green]aktywne[/] ✅")
    else:
        console.print("Środowisko wirtualne: [red]nieaktywne[/] ❌")

    table = Table(title="Nasi specjaliści (dane fikcyjne)")
    table.add_column("Imię")
    table.add_column("Nazwisko")
    table.add_column("Specjalizacja")
    table.add_column("Forma", style="cyan")
    for first_name, last_name, specialization, mode in SPECIALISTS:
        table.add_row(first_name, last_name, specialization, mode)

    console.print(table)


if __name__ == "__main__":
    main()
