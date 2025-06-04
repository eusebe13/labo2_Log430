import db from '../models/index.js';
const { Produit } = db;

export const getAllProduits = async (req, res) => {
  try {
    const produits = await Produit.findAll();
    res.json(produits);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

export const addProduit = async (req, res) => {
  try {
    const { nom, categorie, prix_unitaire } = req.body;
    const produit = await Produit.create({ nom, categorie, prix_unitaire });
    res.status(201).json(produit);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};