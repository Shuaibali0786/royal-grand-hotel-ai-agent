from pydantic import BaseModel

class MyDataOutPut(BaseModel):
    is_hotel_sannata_query: bool
    is_hotel_sannata_account_or_tax_query: bool
    reason: str
