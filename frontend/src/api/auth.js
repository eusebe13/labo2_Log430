export const mockLogin = async (username, password) => {
    const users = [
      { username: "employe", password: "1234", role: "employe" },
      { username: "gestionnaire", password: "abcd", role: "gestionnaire" },
      { username: "responsable", password: "admin", role: "responsable" },
    ];
  
    const user = users.find(u => u.username === username && u.password === password);
    return new Promise(resolve => setTimeout(() => resolve(user), 500)); // Simule un délai réseau
  };
  