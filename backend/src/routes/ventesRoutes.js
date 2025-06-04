import express from 'express';
import db from '../models/index.js';

const router = express.Router();
const { Vente, Produit } = db;

router.post('/', async (req, res) => {
  try {
    const { produit_id, quantite } = req.body;
    const produit = await Produit.findByPk(produit_id);
    if (!produit) return res.status(404).json({ error: 'Produit non trouvé' });

    const prix_total = parseFloat(produit.prix_unitaire) * quantite;

    const vente = await Vente.create({ produitId: produit_id, quantite, prix_total });
    res.status(201).json(vente);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

router.get('/', async (req, res) => {
  try {
    const ventes = await Vente.findAll({ include: Produit });
    res.json(ventes);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

export default router;