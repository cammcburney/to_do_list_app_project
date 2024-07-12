from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    username: str
    password: str
    passcode: Optional[List[str]] = None