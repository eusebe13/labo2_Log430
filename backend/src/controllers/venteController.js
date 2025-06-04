const { Vente, Produit } = require('../models');

exports.ajouterVente = async (req, res) => {
  const { produitId, quantite } = req.body;
  const produit = await Produit.findByPk(produitId);
  const prix_total = produit.prix_unitaire * quantite;
  const vente = await Vente.create({ produitId, quantite, prix_total });
  res.status(201).json(vente);
};