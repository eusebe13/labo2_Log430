import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const consulterProduits = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/produits`);
    return await response.json();
  } catch (error) {
    console.error("Erreur lors de la récupération des produits :", error);
    return [];
  }
};

export const acheterProduits = async (ids) => {
  try {
    const response = await axios.post(`${BASE_URL}/acheter`, ids);
    return response.data.total;
  } catch (error) {
    console.error("Erreur lors de l'achat des produits :", error);
    return null;
  }
};

export const verifierStock = async (produitId = null) => {
  try {
    const response = await axios.get(`${BASE_URL}/stock`, {
      params: produitId ? { produit_id: produitId } : {},
    });
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la vérification du stock :", error);
    return null;
  }
};
