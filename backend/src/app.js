import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import db from './models/index.js';
import produitsRoutes from './routes/produitsRoutes.js';
import ventesRoutes from './routes/ventesRoutes.js';

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.use('/api/produits', produitsRoutes);
app.use('/api/ventes', ventesRoutes);

db.sequelize.sync().then(() => {
  app.listen(port, () => console.log(`Serveur en écoute sur http://localhost:${port}`));
});