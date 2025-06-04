// src/routes/produitsRoutes.js
import express from 'express';
import { getAllProduits, addProduit } from '../controllers/produitController.js';

const router = express.Router();

router.get('/', getAllProduits);
router.post('/', addProduit);

export default router;
