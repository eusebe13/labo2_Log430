export default (sequelize, DataTypes) => {
  return sequelize.define('Magasin', {
    nom: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    region: {
      type: DataTypes.STRING,
      allowNull: false,
    },
  });
};