import { useState } from 'react';

const Responsable = () => {
  const [output, setOutput] = useState('');

  const voirRapportsVente = async () => {
    setOutput("Chargement des rapports de vente...");
  };

  const voirProduitsCritiques = async () => {
   setOutput("Chargement des produits en stock critique...");
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Bienvenue Responsable</h1>
      <h2 className="text-xl font-bold mb-4">Interface Responsable</h2>
      <div className="space-x-4 mb-4">
        <button onClick={voirRapportsVente} className="bg-indigo-600 text-white px-4 py-2 rounded">Voir les rapports de vente</button>
        <button onClick={voirProduitsCritiques} className="bg-orange-500 text-white px-4 py-2 rounded">Produits en stock critique</button>
      </div>
      <pre className="bg-gray-100 p-4 rounded whitespace-pre-wrap">{output}</pre>
    </div>
  );
};
  
  export default Responsable;
  