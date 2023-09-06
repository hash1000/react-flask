import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Fetch data from your Flask API
    axios.get('http://127.0.0.1:5000/users')
      .then(response => {
        setUsers(response.data);
        console.log(users);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h2>User List</h2>
      
    </div>
  );
}

export default UserList;
