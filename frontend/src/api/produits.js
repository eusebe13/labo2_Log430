import axios from 'axios';
const BASE_URL = 'http://localhost:3000/api/produits';

export const getProduits = () => axios.get(BASE_URL);
export const addProduit = (data) => axios.post(BASE_URL, data);
