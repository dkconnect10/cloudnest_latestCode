import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './auth.css';

const UpdateProfile = () => {
  const [form, setForm] = useState({ username: '', email: '' });
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(true);

  // Fetch profile on mount
  useEffect(() => {
    axios.get('/api/GetProfile/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
    .then(res => {
      setForm({ username: res.data.username || '', email: res.data.email || '' });
      setLoading(false);
    })
    .catch(err => {
      setMessage('Failed to load profile');
      setLoading(false);
    });
  }, []);

  // Handle form submit
  const handleSubmit = (e) => {
    e.preventDefault();

    axios.patch(`/api/UpdateProfile/${form.id || 1}/`, form, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`
      }
    })
    .then(res => {
      setMessage('Profile updated successfully');
    })
    .catch(err => {
      setMessage('Error updating profile');
    });
  };

  return (
    <div className="auth-form">
      <h2>Update Profile</h2>
      {loading ? (
        <p>Loading profile...</p>
      ) : (
        <>
          {message && <p className="message">{message}</p>}
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Username"
              value={form.username}
              onChange={e => setForm({ ...form, username: e.target.value })}
              required
            />
            <input
              type="email"
              placeholder="Email"
              value={form.email}
              onChange={e => setForm({ ...form, email: e.target.value })}
              required
            />
            <button type="submit">Update</button>
          </form>
        </>
      )}
    </div>
  );
};

export default UpdateProfile;
