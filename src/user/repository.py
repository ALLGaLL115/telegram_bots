from user.model import Users
from utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model: Users