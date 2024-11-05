import React, { useState, useEffect } from 'react';
import axios from 'axios';
import mongoose from 'mongoose';

const config = require('./config');

interface Data {
  // Define the structure of your data here
  _id: string;
  name: string;
  // ... other fields
}

const MyComponent = () => {
  const [data, setData] = useState<Data[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        await mongoose.connect(config.mongoURI);
        const response = await axios.get('http://localhost:3000/api/data'); // Replace with your API endpoint
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        mongoose.disconnect();
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {data.map((item) => (
        <div key={item._id}>{item.name}</div>
      ))}
    </div>
  );
};

export default MyComponent;