import React, { useState } from 'react'
import './login_register.css'

import { RiLockPasswordFill } from "react-icons/ri";
import { MdEmail } from "react-icons/md";
import { IoPersonSharp } from "react-icons/io5";

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
          <IoPersonSharp />
          <input type="text" placeholder="Name" />
        </div>

        <div className="input">
          <MdEmail />
          <input type="email" placeholder= "Email" />
        </div>

        <div className="input">
          <RiLockPasswordFill className="icon" />
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