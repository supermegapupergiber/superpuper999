import React, { useEffect, useState } from 'react';

function Profile() {
  const [profiles, setProfiles] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/profiles')
      .then((response) => response.json())
      .then((data) => setProfiles(data));
  }, []);

  return (
    <div>
      <h2>Profiles</h2>
      <ul>
        {profiles.map((profile) => (
          <li key={profile.id}>{profile.username} - Rating: {profile.rating}</li>
        ))}
      </ul>
    </div>
  );
}

export default Profile;
