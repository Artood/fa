from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    inn: str
    contract_number: str | None = None
    contact_person: str | None = None
    external_prefix: str | None = None
    ip_dmz: str | None = None
    ip_inside: str | None = None

class ClientResponse(ClientCreate):
    id: int

    class Config:
        from_attributes = True

