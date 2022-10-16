import React from 'react';
import { GoogleLogin } from 'react-google-login';
import Router from 'next/router';

const client_id = "247747261514-8k1qikhl0urh29oema81jeuod9g5kc37.apps.googleusercontent.com";

function GoogleLoginButton() {
    const onSuccess = (res) => {
        console.log("Successful login! Current user: ", res.profileObj);

        setTimeout(() => {
         Router
        .push('/')
        .catch(console.error);
        }, 4500);

    }

    const onFailure = (res) => {
        console.log("Failed login: ", res);
    }

  return (
    <div id="login">
        <GoogleLogin
        client_id={client_id}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={'single_host_origin'}
        isSignedIn={true}
        >
        </GoogleLogin>
    </div>
  )
}

export default GoogleLoginButton