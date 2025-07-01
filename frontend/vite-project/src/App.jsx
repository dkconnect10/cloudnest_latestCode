import React from 'react';
import RegisterUser from './components/auth/RegisterUser.jsx';
import LoginUser from './components/auth/LoginUser.jsx';
import Profile from './components/auth/Profile.jsx';
import UpdateProfile from './components/auth/UpdateProfile.jsx';
import ResetPassword from './components/auth/ResetPassword.jsx';
import ForgotPassword from './components/auth/ForgotPassword.jsx';
import AccountToggle from './components/auth/AccountToggle.jsx';
import AccountDeletion from './components/auth/AccountDeletion.jsx';
import LogoutUser from './components/auth/LogoutUser.jsx';
import './App.css';

function App() {
  return (
    <div className="hospital-bg">
      <div className="header">
        <h1 className="animated-title">🏥 CloudNest Hospital Portal</h1>
        <p className="subtitle">Secure and Smart User Management System</p>
      </div>

      <div className="auth-section">
        <RegisterUser />
        <LoginUser />
        <Profile />
        <UpdateProfile userId={1} />
        <ResetPassword />
        <ForgotPassword />
        <AccountToggle />
        <AccountDeletion />
        <LogoutUser />
      </div>
    </div>
  );
}

export default App;
