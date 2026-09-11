import React, { useState } from 'react'
import './login_register.css'


const Login_register = () => {

const [action,setAction] = useState("Register");

  return (
    <div className='container'>
      <div className="header">
        <div className="text">Register</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        <div className="input">
          <img src="" alt="" />
          <input type="text" placeholder="Name" />
        </div>

        <div className="input">
          <img src="" alt="" />
          <input type="email" placeholder= "Email" />
        </div>

        <div className="input">
          <img src="" alt="" />
          <input type="password" placeholder= "Password" />
        </div>
      </div>

      <div className="forgot-password"> Lost Password? <span>Click Here</span></div>

      <div className='submit-container'>
        <div className="submit">Login</div>
        <div className="submit">Register</div>
      </div>
    </div>
  )
}

export default Login_register