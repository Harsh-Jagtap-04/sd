import React from 'react';
import { useLocation } from 'react-router-dom';

const UserDashboard = () => {
  const { state } = useLocation();
  const { userData } = state || {};

  return (
    <div>
      <h2>User Dashboard</h2>
      {userData ? (
        <pre>{JSON.stringify(userData, null, 2)}</pre>
      ) : (
        <p>No data available</p>
      )}
    </div>
  );
};

export default UserDashboard;
