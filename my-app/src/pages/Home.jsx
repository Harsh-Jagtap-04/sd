import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <h1>Welcome to Test Management System</h1>
      <div className="options">
        <div className="option" onClick={() => navigate('/user')}>
          <h2>User</h2>
        </div>
        <div className="option" onClick={() => navigate('/admin')}>
          <h2>Admin</h2>
        </div>
      </div>
    </div>
  );
};

export default Home;
