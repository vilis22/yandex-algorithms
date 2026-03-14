from dataclasses import dataclass


@dataclass(order=True)
class Employee:
    salary: int
    name: str
