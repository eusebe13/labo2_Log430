import { Sequelize, DataTypes } from 'sequelize';
import ProduitModel from './produit.js';
import VenteModel from './vente.js';
import MagasinModel from './magasin.js';

const sequelize = new Sequelize('magasin', 'user', 'password', {
  host: 'localhost',
  dialect: 'postgres',
});

const db = {
  Sequelize,
  sequelize,
  Produit: ProduitModel(sequelize, DataTypes),
  Vente: VenteModel(sequelize, DataTypes),
  Magasin: MagasinModel(sequelize, DataTypes),
};

db.Produit.hasMany(db.Vente);
db.Vente.belongsTo(db.Produit);

export default db;