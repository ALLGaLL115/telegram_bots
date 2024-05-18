from sqlalchemy import String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

from user.shcemas import UserDTO
class Users(Base):
    __tablename__="users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30),  nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    def convert_to_model(self) -> UserDTO:
        return UserDTO(
            id = self.id,
            name = self.name,
            email = self.email,
            password_hash = self.password_hash,            
        )