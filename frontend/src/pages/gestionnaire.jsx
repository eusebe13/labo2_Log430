import { useState } from 'react';

const Gestionnaire = () => {
  const [output, setOutput] = useState('');

  const ajouterProduit = () => {
    setOutput("Entrez les détails du produit à ajouter (nom, prix, stock) :");
  };

  const supprimerProduit = () => {
    setOutput("Entrez l'ID du produit à supprimer :");
  };

  const consulterProduits = async () => {
    setOutput("Chargement des produits...");
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Interface Gestionnaire</h2>
      <div className="space-x-4 mb-4">
        <button onClick={ajouterProduit} className="bg-green-600 text-white px-4 py-2 rounded">Ajouter un produit</button>
        <button onClick={supprimerProduit} className="bg-red-500 text-white px-4 py-2 rounded">Supprimer un produit</button>
        <button onClick={consulterProduits} className="bg-blue-500 text-white px-4 py-2 rounded">Voir les produits</button>
      </div>
      <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">{output}</pre>
    </div>
  );
};
  
  export default Gestionnaire;
  