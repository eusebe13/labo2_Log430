CREATE TABLE ventes (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL DEFAULT NOW(),
    produit_id INT REFERENCES produits(id),
    quantite INT NOT NULL,
    prix_total DECIMAL(10,2) NOT NULL
);