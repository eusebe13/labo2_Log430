import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [choix, setChoix] = useState('');
  const [resultat, setResultat] = useState(null);

  const handleChoix = async (option) => {
    setChoix(option);
    setResultat(null);

    switch (option) {
      case '1': {
        const res = await fetch('/api/products');
        const produits = await res.json();
        setResultat(produits);
        break;
      }
      case '2': {
        const keyword = prompt('Mot-clé (nom ou catégorie) :');
        const res = await fetch(`/api/products/search?keyword=${keyword}`);
        const produits = await res.json();
        setResultat(produits);
        break;
      }
      case '3': {
        const ids = prompt('IDs des produits (séparés par virgule) :');
        const id_list = ids.split(',').map((id) => parseInt(id));
        const res = await fetch('/api/sales', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ ids: id_list })
        });
        const data = await res.json();
        setResultat(`Total = ${data.total}$`);
        break;
      }
      case '4': {
        const pid = prompt('ID du produit à retourner :');
        const res = await fetch(`/api/returns/${pid}`, { method: 'POST' });
        const data = await res.json();
        setResultat(data.success ? 'Produit retourné avec succès.' : "Échec du retour.");
        break;
      }
      case '5': {
        const pid = prompt("ID du produit (laisser vide pour tout):");
        const res = await fetch(pid ? `/api/stock/${pid}` : '/api/stock');
        const data = await res.json();
        setResultat(data);
        break;
      }
      case '7': {
        const storeId = prompt("ID du magasin :");
        const res = await fetch(`/api/stocks/${storeId}`);
        const data = await res.json();
        setResultat(data);
        break;
      }
      case '8': {
        const res = await fetch(`/api/stocks`);
        const data = await res.json();
        setResultat(data);
        break;
      }
      default:
        break;
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Menu - Maison Mere</h1>
      <div className="grid grid-cols-1 gap-2">
        {['Lister les produits', 'Rechercher un produit', 'Enregistrer une vente', 'Retourner un produit', 'Vérifier le stock', 'Voir le stock d’un magasin spécifique', 'Voir le stock de tous les magasins'].map((opt) => (
          <button
            key={opt}
            className="bg-blue-500 text-white p-2 rounded"
            onClick={() => handleChoix(opt)}
          >
            {opt}
          </button>
        ))}
      </div>
      <div className="mt-6">
        <h2 className="font-semibold">Résultat :</h2>
        <pre className="bg-gray-100 p-2 mt-2">
          {JSON.stringify(resultat, null, 2)}
        </pre>
      </div>
    </div>
  );
}

export default App;
