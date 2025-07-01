import React from 'react';


const LogoutUser = () => {
  const handleLogout = () => {
    localStorage.removeItem('access_token');
    alert('Logged out successfully');
  };

  return (
    <div className="auth-form">
      <h2>Logout</h2>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default LogoutUser;