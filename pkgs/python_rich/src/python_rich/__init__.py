from dataclasses import dataclass, fields
from rich.table import Table


@dataclass
class Person:
    name: str
    age: int
    city: str


def add_columns_fields(table: Table) -> Table:
    for column in fields(Person):
        table.add_column(column.name)
    return table


def add_rows(table: Table, people) -> Table:
    for person in people:
        table.add_row(person.name, str(person.age), person.city)
    return table

    