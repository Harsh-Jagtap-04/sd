import React from 'react';
import { useNavigate } from 'react-router-dom';
import UploadData from './UploadData';
const AdminDashboard = () => {
  const navigate = useNavigate();

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <button onClick={() => navigate('/admin/view-dashboard')}>View Dashboard</button>
      <UploadData />
    </div>
  );
};

export default AdminDashboard;
