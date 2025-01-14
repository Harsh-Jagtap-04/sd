import React, { useState } from 'react';
import axios from '../../utils/api';

const UploadData = () => {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/admin/upload', formData);
      alert(response.data.message);
    } catch (error) {
      alert('Error uploading file');
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Test Data</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default UploadData;
