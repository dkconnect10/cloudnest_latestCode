// src/components/Navbar.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="navbar-brand">🏥 CloudNest</div>
      <ul className="nav-links">
        <li className={location.pathname === '/' ? 'active' : ''}><Link to="/">Home</Link></li>
        <li className={location.pathname === '/register' ? 'active' : ''}><Link to="/register">Register</Link></li>
        <li className={location.pathname === '/login' ? 'active' : ''}><Link to="/login">Login</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
