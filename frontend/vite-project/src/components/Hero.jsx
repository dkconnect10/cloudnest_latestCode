import React from 'react';
import hospitalImage from '../assets/Hospital.jpg';
import './Hero.css';

const Hero = () => {
  return (
    <div className="hero-container" style={{ backgroundImage: `url(${hospitalImage})` }}>
      <div className="hero-overlay">
        <h1>Welcome to CloudNest Hospital</h1>
        <p>Advanced user and hospital management system</p>
        <a href="/register" className="hero-button">Get Started</a>
      </div>
    </div>
  );
};

export default Hero;
