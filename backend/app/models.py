import datetime
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, ForeignKey,
    Enum, Table, Boolean
)
from sqlalchemy.orm import relationship, declarative_base
import enum

Base = declarative_base()

# Enumération des rôles
class RoleEnum(enum.Enum):
    gestionnaire = "gestionnaire"
    employe = "employe"
    responsable = "responsable"

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    mot_de_passe = Column(String, nullable=False) # Mot de passe haché
    magasin_id = Column(Integer, ForeignKey('magasins.id'), nullable=True)
    is_maison_mere = Column(Boolean, default=False)

    magasin = relationship("Magasin", back_populates="utilisateurs")

class Magasin(Base):
    __tablename__ = 'magasins'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    region = Column(String, nullable=False)

    ventes = relationship("Vente", back_populates="magasin")
    reapprovisionnements = relationship("Reapprovisionnement", back_populates="magasin")
    utilisateurs = relationship("Utilisateur", back_populates="magasin")

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
    rapports = relationship("RapportTendance", secondary="rapport_product_assoc", back_populates="produits")
    stock_central = relationship("StockCentral", back_populates="produit")

class Vente(Base):
    __tablename__ = 'ventes'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    quantite = Column(Integer, nullable=False)
    prix_total = Column(Float, nullable=False)

    produit_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    magasin_id = Column(Integer, ForeignKey('magasins.id'))

    produit = relationship("Product", back_populates="ventes")
    magasin = relationship("Magasin", back_populates="ventes")

class Reapprovisionnement(Base):
    __tablename__ = 'reapprovisionnements'
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('products.id'))
    quantite = Column(Integer)
    magasin_id = Column(Integer, ForeignKey('magasins.id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    centre_id = Column(Integer, ForeignKey('centre_logistique.id'))

    produit = relationship("Product", back_populates="reapprovisionnements")
    magasin = relationship("Magasin", back_populates="reapprovisionnements")
    centre = relationship("CentreLogistique", back_populates="reapprovisionnements")

class AlerteRupture(Base):
    __tablename__ = 'alertes_rupture'
    id = Column(Integer, primary_key=True)
    niveau_stock = Column(Integer, nullable=False)
    date_alerte = Column(DateTime, default=datetime.datetime.utcnow)
    produit_id = Column(Integer, ForeignKey('products.id'))
    
    produit = relationship("Product", back_populates="alertes")

class RapportTendance(Base):
    __tablename__ = 'rapport_tendance'
    id = Column(Integer, primary_key=True)
    region = Column(String, nullable=False)
    periode = Column(String, nullable=False)
    total_ventes = Column(Float)
    croissance_hebdo = Column(Float)

    produits = relationship("Product", secondary="rapport_product_assoc", back_populates="rapports")

class CentreLogistique(Base):
    __tablename__ = 'centre_logistique'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    region = Column(String)

    reapprovisionnements = relationship("Reapprovisionnement", back_populates="centre")

class StockCentral(Base):
    __tablename__ = 'stock_central'
    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('products.id'))
    quantite = Column(Integer)

    produit = relationship("Product", back_populates="stock_central")

rapport_produit_assoc = Table(
    'rapport_product_assoc', Base.metadata,
    Column('rapport_id', Integer, ForeignKey('rapport_tendance.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)
