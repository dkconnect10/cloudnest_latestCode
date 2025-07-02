// src/components/auth/RegisterUser.jsx
import { useState } from 'react';
import api from '../../services/api';
import './auth.css';

export default function RegisterUser() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    full_name: '',
    phone: '',
    gender: '',
    avatar: null,
  });

  const handleChange = (e) => {
    const { name, value, type, files } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'file' ? files[0] : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      if (value !== null && value !== '') {
        data.append(key, value);
      }
    });

    try {
      const response = await api.post('RegisterUser/', data, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      alert(response.data.message || 'Registration successful!');
    } catch (error) {
      console.error(error.response?.data || error.message);
      alert('Registration failed');
    }
  };

  return (
    <div className="auth-form">
      <h2>Register</h2>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <input name="username" placeholder="Username" onChange={handleChange} required />
        <input name="email" placeholder="Email" onChange={handleChange} required />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
        <input name="full_name" placeholder="Full Name" onChange={handleChange} />
        <input name="phone" placeholder="Phone Number" onChange={handleChange} />
        <select name="gender" onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
        <input type="file" name="avatar" accept="image/*" onChange={handleChange} />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}
