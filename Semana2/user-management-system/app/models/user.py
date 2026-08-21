from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class RoleType(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

@dataclass
class Role:
    name: RoleType
    permissions: list[str]

@dataclass
class User:
    id: int
    username: str
    email: str
    role: Role
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)