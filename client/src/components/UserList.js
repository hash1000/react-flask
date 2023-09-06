import React, { useEffect } from 'react';
import axios from 'axios';

function UserList() {

  useEffect(() => {
    // Fetch data from your Flask API
    axios.get('http://127.0.0.1:5000/users')
      .then(response => {
        console.log(response.data);
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
