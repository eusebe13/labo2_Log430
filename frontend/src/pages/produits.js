import React, { useEffect, useState } from 'react';
import { getProduits, addProduit } from '../api/produits';

function Produits() {
  const [produits, setProduits] = useState([]);
  const [nom, setNom] = useState("");
  const [categorie, setCategorie] = useState("");
  const [prix, setPrix] = useState("");

  useEffect(() => {
    getProduits().then(res => setProduits(res.data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addProduit({ nom, categorie, prix_unitaire: prix });
    const updated = await getProduits();
    setProduits(updated.data);
  };

  return (
    <div>
      <h1>Produits</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Nom" value={nom} onChange={e => setNom(e.target.value)} />
        <input placeholder="Catégorie" value={categorie} onChange={e => setCategorie(e.target.value)} />
        <input placeholder="Prix" type="number" value={prix} onChange={e => setPrix(e.target.value)} />
        <button type="submit">Ajouter</button>
      </form>

      <ul>
        {produits.map(p => (
          <li key={p.id}>{p.nom} - {p.categorie} - {p.prix_unitaire} €</li>
        ))}
      </ul>
    </div>
  );
}

export default Produits;
