export default (sequelize, DataTypes) => {
  return sequelize.define('Vente', {
    date: {
      type: DataTypes.DATE,
      defaultValue: DataTypes.NOW,
    },
    quantite: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
    prix_total: {
      type: DataTypes.DECIMAL(10, 2),
      allowNull: false,
    },
  });
};