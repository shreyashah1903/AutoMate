import React from 'react'
import { GoogleLogout } from 'react-google-login';

const client_id = "247747261514-8k1qikhl0urh29oema81jeuod9g5kc37.apps.googleusercontent.com";

function GoogleLogoutButton() {

    const onSuccess = () => {
        console.log("Logout successful!");
    }

  return (
    <div id="signOutButton">
        <GoogleLogout
            client_id={client_id}
            buttonText={"Logout"}
            onLogoutSuccess={onSuccess}
        />
    </div>
  )
}

export default GoogleLogoutButton