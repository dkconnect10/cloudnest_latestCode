import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './auth.css';

const UpdateProfile = ({ userId }) => {
  const [form, setForm] = useState({ username: '', email: '' });
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('/api/GetProfile/', {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
    })
    .then(res => setForm({ username: res.data.username, email: res.data.email }))
    .catch(() => setMessage('Failed to load profile'));
  }, []);

  const handleSubmit = e => {
    e.preventDefault();
    axios.patch(`/api/UpdateProfile/${userId}/`, form, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
    })
    .then(() => setMessage('Profile updated successfully'))
    .catch(() => setMessage('Error updating profile'));
  };

  return (
    <div className="auth-form">
      <h2>Update Profile</h2>
      {message && <p className="message">{message}</p>}
      <form onSubmit={handleSubmit}>
        <input type="text" value={form.username} placeholder="Username" onChange={e => setForm({ ...form, username: e.target.value })} />
        <input type="email" value={form.email} placeholder="Email" onChange={e => setForm({ ...form, email: e.target.value })} />
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default UpdateProfile;