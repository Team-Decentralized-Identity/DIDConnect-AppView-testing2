<style>
   .button-group {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column; /* Stack buttons vertically */
    gap: 20px; /* Space between buttons */
  }

  .button {
    font-size: 18px;
    padding: 15px 60px;
    margin-top: 5px; 
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    text-decoration: none; /* Remove underline from links */
  }

  #signUp {
    background-color: #b8d8be;
    color: black; /* Text color for buttons */
    text-decoration: none; /* Remove underline from links */
    margin-top: 30px;
  }

  #signIn {
    background-color: #b8d8be;
    color: black; /* Text color for buttons */
    text-decoration: none; /* Remove underline from links */
  }

  #signUp:hover, #signIn:hover {
    filter: brightness(85%);
  }

  .logo {
    display: block; /* Change this to block to allow margin auto to center */
    margin: 150px auto 60px auto; /* Center horizontally and add margin bottom */
    max-height: 400px; /* Maximum size to maintain aesthetics */
  }

  .footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    text-align: center;
    font-size: 12px;
    padding: 10px 0;
  }

  .logo-name {
    display: block; /* Add this to center the text */
    text-align: center; /* Center the text */
    font-size: 4rem; /* Adjusted font size for logo name */
    font-weight: bold;
    margin-top: -140px; /* Adjust if necessary to align with the logo */
    color: #fbf5eb;
  }

</style>

<template>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sign In & Sign Up</title>
  <link rel="icon" type="image/png" href="src/assets/Filled_DIDConnect_Logo.png">
</head>
<body>

<div class="content">
  <img src="src/assets/Filled_DIDConnect_Logo.png" alt="DIDConnect Logo" class="logo">
  <span class="logo-name">DIDConnect</span> <!-- Centered logo name -->
  <div class="button-group">
    <a id="signUp" class="button">Sign Up</a>
    <a href="/login" @click.prevent="$router.push('/login')" id="signIn" class="button">Sign In</a>
  </div>
</div>

</body>
</html>
</template>