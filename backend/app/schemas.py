# app/schemas.py
from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int

    class Config:
        orm_mode = True


class ProductCreateSchema(BaseModel):
    name: str
    category: str
    price: float
    stock: int


class VenteSchema(BaseModel):
    id: int
    total: float

    class Config:
        orm_mode = True


class RapportSchema(BaseModel):
    id: int
    region: str
    periode: str
    total_ventes: float

    class Config:
        orm_mode = True


class UpdateProductSchema(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


class ReapprovisionnementSchema(BaseModel):
    produit_id: int
    quantite: int
    magasin_id: int
    centre_id: int
