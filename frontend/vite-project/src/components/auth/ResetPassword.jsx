import { useState } from 'react';
import axios from 'axios';

export default function ResetPassword() {
  const [form, setForm] = useState({ uid: '', token: '', new_password: '', confirm_password: '' });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/api/auth/forgotPassword/', form);
      alert(res.data.message);
    } catch (err) {
      alert('Reset failed');
    }
  };

  return (
    <div className="auth-form">
      <h2>Reset Password</h2>
      <form onSubmit={handleSubmit}>
        <input name="uid" placeholder="UID" onChange={handleChange} required />
        <input name="token" placeholder="Token" onChange={handleChange} required />
        <input name="new_password" placeholder="New Password" type="password" onChange={handleChange} required />
        <input name="confirm_password" placeholder="Confirm Password" type="password" onChange={handleChange} required />
        <button type="submit">Reset</button>
      </form>
    </div>
  );
}