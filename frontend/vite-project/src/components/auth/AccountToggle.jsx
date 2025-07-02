import React, { useState } from 'react';
import axios from 'axios';
import './auth.css';

const AccountToggle = () => {
  const [isActive, setIsActive] = useState(true);
  const [message, setMessage] = useState('');

  const handleToggle = () => {
    axios.post('/api/AccountDeactivationReactivation/', { is_active: !isActive }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
    })
    .then(res => {
      setIsActive(!isActive);
      setMessage(res.data.message);
    })
    .catch(() => setMessage('Failed to toggle account status'));
  };

  return (
    <div className="auth-form">
      <h2>Account {isActive ? 'Deactivate' : 'Reactivate'}</h2>
      <button onClick={handleToggle}>{isActive ? 'Deactivate' : 'Reactivate'}</button>
      {message && <p className="message">{message}</p>}
    </div>
  );
};

export default AccountToggle;