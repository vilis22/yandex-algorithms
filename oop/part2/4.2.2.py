from dataclasses import dataclass


@dataclass
class User:
    username: str
    is_active: bool = True
    level: int = 1
