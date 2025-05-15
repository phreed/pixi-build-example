import python_rich
from python_rich import Person
from rich.console import Console
from rich.table import Table


def main() -> None:
    console = Console()

    people = [
        Person("John Doe", 30, "New York"),
        Person("Jane Smith", 25, "Los Angeles"),
        Person("Tim de Jager", 35, "Utrecht"),
    ]
    
    table = Table()

    table = python_rich.show_fields(table)
    table = python_rich.add_rows(people, table)

    console.print(table)
    