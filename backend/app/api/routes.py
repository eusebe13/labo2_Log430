# app/router.py
from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.employe import acheter_product, consulter_product, verifier_stock
from app.gestionnaire import afficher_rapports, generer_rapport, mettre_a_jour_produit
from app.responsable import consulter_stock, reapprovisionner
from app.schemas import ProductSchema, RapportSchema, ReapprovisionnementSchema, UpdateProductSchema

router = APIRouter()

# Employé
@router.get("/produits", response_model=List[ProductSchema])
def get_produits():
    return consulter_product()

@router.post("/acheter")
def post_acheter(ids: List[int]):
    if not ids:
        raise HTTPException(status_code=400, detail="Liste d'IDs vide")
    total = acheter_product(ids)
    return {"total": total}

@router.get("/stock")
def get_stock(produit_id: Optional[int] = None):
    return verifier_stock(produit_id)

# Gestionnaire
@router.get("/rapports", response_model=List[RapportSchema])
def get_rapports():
    return afficher_rapports()

@router.get("/rapport", response_model=List[RapportSchema])
def get_rapport(region: Optional[str] = None):
    return generer_rapport(region)

@router.put("/produit/{produit_id}")
def update_produit(produit_id: int, modifs: UpdateProductSchema):
    success = mettre_a_jour_produit(produit_id, modifs.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return {"message": "Produit mis à jour"}

# Responsable
@router.get("/stocks", response_model=List[ProductSchema])
def get_tous_stock():
    return consulter_stock()

@router.post("/reapprovisionner")
def post_reappro(reappro: ReapprovisionnementSchema):
    reapprovisionner(**reappro.dict())
    return {"message": "Produit réapprovisionné"}
