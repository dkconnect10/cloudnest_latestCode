import React, { useState } from 'react';
import axios from 'axios';
import './auth.css';

const AccountDeletion = () => {
  const [message, setMessage] = useState('');

  const handleDelete = () => {
    axios.post('/api/AccountDeletion/', {}, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
    })
    .then(res => setMessage(res.data.message))
    .catch(() => setMessage('Failed to delete account'));
  };

  return (
    <div className="auth-form">
      <h2>Delete Account</h2>
      <button className="danger" onClick={handleDelete}>Delete</button>
      {message && <p className="message">{message}</p>}
    </div>
  );
};

export default AccountDeletion;