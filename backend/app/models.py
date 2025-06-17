import datetime
import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Enumération des rôles
class RoleEnum(enum.Enum):
    gestionnaire = "gestionnaire"
    employe = "employe"
    responsable = "responsable"

# Association pour rapport <-> produit (many-to-many)
rapport_product_assoc = Table(
    'rapport_product_assoc', Base.metadata,
    Column('rapport_id', Integer, ForeignKey('rapport_tendance.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    mot_de_passe = Column(String, nullable=False)
    magasin_id = Column(Integer, ForeignKey('magasins.id'), nullable=True)
    is_maison_mere = Column(Boolean, default=False)

    magasin = relationship("Magasin", back_populates="utilisateurs")

class Magasin(Base):
    __tablename__ = 'magasins'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    region = Column(String, nullable=False)
    maison_mere_id = Column(Integer, ForeignKey('magasin_maison_mere.id'))

    ventes = relationship("Vente", back_populates="magasin")
    reapprovisionnements = relationship("Reapprovisionnement", back_populates="magasin")
    utilisateurs = relationship("Utilisateur", back_populates="magasin")
    maison_mere = relationship("MagasinMaisonMere", back_populates="magasins")

class MagasinMaisonMere(Base):
    __tablename__ = 'magasin_maison_mere'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    adresse = Column(String, nullable=False)

    magasins = relationship("Magasin", back_populates="maison_mere")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    ventes = relationship("Vente", back_populates="produit")
    reapprovisionnements = relationship("Reapprovisionnement", back_populates="produit")
    alertes = relationship("AlerteRupture", back_populates="produit")
    rapports = relationship("RapportTendance", secondary=rapport_product_assoc, back_populates="produits")
    stock_central = relationship("StockCentral", back_populates="produit", uselist=False)

class Vente(Base):
    __tablename__ = 'ventes'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    quantite = Column(Integer, nullable=False)
    prix_total = Column(Float, nullable=False)

    produit_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    magasin_id = Column(Integer, ForeignKey('magasins.id'), nullable=False)

    produit = relationship("Product", back_populates="ventes")
    magasin = relationship("Magasin", back_populates="ventes")

class RapportTendance(Base):
    __tablename__ = 'rapport_tendance'
    id = Column(Integer, primary_key=True)
    region = Column(String, nullable=False)
    total_ventes = Column(Float)

    produits = relationship("Product", secondary=rapport_product_assoc, back_populates="rapports")

class Reapprovisionnement(Base):
    __tablename__ = 'reapprovisionnements'
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    magasin_id = Column(Integer, ForeignKey('magasins.id'), nullable=False)
    quantite = Column(Integer, nullable=False)
    statut = Column(String, nullable=False)

    produit = relationship("Product", back_populates="reapprovisionnements")
    magasin = relationship("Magasin", back_populates="reapprovisionnements")

class AlerteRupture(Base):
    __tablename__ = 'alerte_rupture'
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    niveau_stock = Column(Integer, nullable=False)

    produit = relationship("Product", back_populates="alertes")

class StockCentral(Base):
    __tablename__ = 'stock_central'
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('products.id'), unique=True)
    quantite = Column(Integer, nullable=False)

    produit = relationship("Product", back_populates="stock_central")

