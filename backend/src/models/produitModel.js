import { pool } from '../db.js';

export const getAllProduits = async () => {
  const res = await pool.query('SELECT * FROM produits');
  return res.rows;
};

export const getProduitById = async (id) => {
  const res = await pool.query('SELECT * FROM produits WHERE id = $1', [id]);
  return res.rows[0];
};

export const createProduit = async ({ nom, categorie, prix_unitaire }) => {
  const res = await pool.query(
    'INSERT INTO produits (nom, categorie, prix_unitaire) VALUES ($1, $2, $3) RETURNING *',
    [nom, categorie, prix_unitaire]
  );
  return res.rows[0];
};

export const deleteProduit = async (id) => {
  await pool.query('DELETE FROM produits WHERE id = $1', [id]);
};
