import { useState } from 'react';
import { consulterProduits, acheterProduits, verifierStock } from '../api/employe';

const Employe = () => {
  const [output, setOutput] = useState('Testez les fonctionnalités ci-dessous');

  const afficher = async () => {
    try {
      const response = await fetch("http://localhost:8000/produits");
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`);
      }
  
      const produits = await response.json();
  
      if (produits.length > 0) {
        setOutput(
          produits
            .map(p => `${p.id} - ${p.name} (${p.category}) : ${p.price}$, Stock: ${p.stock}`)
            .join('\n')
        );
      } else {
        setOutput("Aucun produit disponible.");
      }
    } catch (error) {
      console.error("Erreur lors de l'appel à l'API:", error);
      setOutput("Erreur lors de la récupération des produits.");
    }
  };

  const acheter = async () => {
    const ids = prompt("IDs des produits séparés par une virgule :");
    const idList = ids.split(',').map(id => parseInt(id.trim(), 10));
    const total = await acheterProduits(idList);
    setOutput(`Vente enregistrée. Total = ${total}$`);
  };

  const verifier = async () => {
    const id = prompt("Entrez l'ID du produit (ou laissez vide pour tout voir) :");
    const stock = await verifierStock(id ? parseInt(id, 10) : null);
    if (Array.isArray(stock)) {
      setOutput(stock.map(s => `${s.id} - ${s.name} : ${s.stock} en stock`).join('\n'));
    } else {
      setOutput(`${stock.name} : ${stock.stock} en stock`);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Bienvenue Employé</h1>
      <div className="space-x-4 mb-4">
        <button onClick={afficher} className="bg-blue-500 text-white px-4 py-2 rounded">
          Afficher les produits
        </button>
        <button onClick={acheter} className="bg-green-500 text-white px-4 py-2 rounded">
          Acheter un produit
        </button>
        <button onClick={verifier} className="bg-yellow-500 text-black px-4 py-2 rounded">
          Vérifier le stock
        </button>
      </div>
      <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">{output}</pre>
    </div>
  );
};
  
  export default Employe;
  