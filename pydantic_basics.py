# {
#   "id": "string",
#   "type": "UNSPECIFIED",
#   "status": "UNSPECIFIED",
#   "balance": 0
from pydantic import BaseModel

class AccountSchema(BaseModel):
    id: str
    type: str
    status: str
    balance: float