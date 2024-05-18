from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    name: str
    email: str
    password: str


class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    password_hash: str