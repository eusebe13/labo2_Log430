import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { mockLogin } from '../api/auth';

const Connexion = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    const user = await mockLogin(username, password);
    if (user) {
      navigate(`/${user.role}`);
    } else {
      setError("Nom d'utilisateur ou mot de passe incorrect.");
    }
  };

  return (
    <div className="p-6 max-w-md mx-auto mt-20 bg-white rounded-xl shadow-md">
      <h1 className="text-xl font-bold mb-4">Connexion</h1>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="block w-full p-2 mb-4 border rounded"
        />
        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="block w-full p-2 mb-4 border rounded"
        />
        {error && <p className="text-red-500 mb-2">{error}</p>}
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Se connecter
        </button>
      </form>
    </div>
  );
};

export default Connexion;
