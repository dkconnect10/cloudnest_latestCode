// src/components/auth/LoginUser.jsx
import { useState } from 'react';
import api from '../../services/api'; 
import './auth.css';

export default function LoginUser() {
  const [formData, setFormData] = useState({ email: '', password: '' });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('loginUser/', formData);
      const { access_token, refresh_Token, message, user } = response.data;

      // Store in localStorage
      localStorage.setItem('access_token', access_token);
      localStorage.setItem('refresh_token', refresh_Token);

      alert(`${message} — Welcome ${user}`);
    } catch (error) {
      console.error(error);
      alert(error.response?.data?.error || 'Login failed');
    }
  };

  return (
    <div className="auth-form">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input name="email" placeholder="Email" onChange={handleChange} required />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
