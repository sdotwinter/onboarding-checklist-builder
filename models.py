from dataclasses import dataclass

@dataclass
class ChecklistItem:
    id: int
    title: str
    owner: str
    completed: int
