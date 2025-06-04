export default (sequelize, DataTypes) => {
  return sequelize.define('Produit', {
    nom: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    categorie: {
      type: DataTypes.STRING,
    },
    prix_unitaire: {
      type: DataTypes.DECIMAL(10, 2),
      allowNull: false,
    },
  });
};