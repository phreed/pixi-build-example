from dataclasses import dataclass, fields
from typing import List
from rich.table import Table
import cpp_math

__all__ = [
    "add_columns",
    "add_rows",
]

@dataclass
class Person:
    name: str
    age: int
    city: str


def add_columns(table: Table) -> Table:
    for column in fields(Person):
        table.add_column(column.name)
    return table


def add_rows(table: Table, people: List[Person]) -> Table:
    for person in people:
        updated_age = cpp_math.add(person.age, 10)
        table.add_row(person.name, str(updated_age), person.city)
    return table

    