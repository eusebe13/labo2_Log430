from database import SessionLocal
from models import Product, Vente


def list_products():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

def register_sale(product_ids):
    session = SessionLocal()
    total = 0
    for pid in product_ids:
        product = session.query(Product).get(pid)
        if product and product.stock > 0:
            product.stock -= 1
            total += product.price
    sale = Vente(total=total)
    session.add(sale)
    session.commit()
    session.close()
    return total

def search_products(keyword):
    session = SessionLocal()
    results = session.query(Product).filter(
        (Product.name.ilike(f"%{keyword}%")) |
        (Product.category.ilike(f"%{keyword}%"))
    ).all()
    session.close()
    return results

def return_product(product_id):
    session = SessionLocal()
    product = session.query(Product).get(product_id)
    if product:
        product.stock += 1
        session.commit()
    session.close()
    return product is not None

def check_stock(product_id=None):
    session = SessionLocal()
    if product_id:
        product = session.query(Product).get(product_id)
        session.close()
        return f"{product.name}: {product.stock} unités" if product else "Produit introuvable"
    else:
        products = session.query(Product).all()
        session.close()
        return [f"{p.name}: {p.stock} unités" for p in products]

def initialize_products():
    session = SessionLocal()
    existing = session.query(Product).count()
    if existing == 0:
        for i in range(20):
            product = Product(
                name=f"Produit{i+1}",
                category="CatégorieA" if i % 2 == 0 else "CatégorieB",
                price=10.0 + i,
                stock=(i + 1) * 2
            )
            session.add(product)
        session.commit()
    session.close()
