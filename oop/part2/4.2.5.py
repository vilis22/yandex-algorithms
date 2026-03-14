from dataclasses import dataclass, field


@dataclass()
class Team:
    name: str
    members: list[str] = field(default_factory=list)
