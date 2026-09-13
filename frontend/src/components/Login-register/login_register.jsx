import { useState } from 'react'
import './login_register.css'

import { RiLockPasswordFill } from "react-icons/ri";
import { MdEmail } from "react-icons/md";
import { IoPersonSharp } from "react-icons/io5";

import { signup } from '../../api/auth.js';

const Login_register = () => {

const [action,setAction] = useState("Register");
const [name, setName] = useState('');
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [msg, setMsg] = useState('');

  const onRegister = async () => {
    setMsg('');
    try {
      const data = await signup(name.trim(), email.trim(), password);
      setMsg(data.msg || 'Registered!');
      setName('');
      setEmail('');
      setPassword('');
    } catch (err) {
      setMsg(err.message);
    }
  };

  const onLogin = () => {
    setMsg('Login is not available yet. Please register first.');
  };

  return (
    <div className='container'>
      <div className="header">
        <div className="text">Register</div>
        <div className="underline"></div>
      </div>

      <div className="inputs">
        <div className="input">
          <IoPersonSharp />
          <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} minLength={4} maxLength={20} required />
        </div>

        <div className="input">
          <MdEmail />
          <input type="email" placeholder= "Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>

        <div className="input">
          <RiLockPasswordFill className="icon" />
          <input type="password" placeholder= "Password" value={password} onChange={(e) => setPassword(e.target.value)} minLength={8} maxLength={20} required />
        </div>
      </div>

      <div className="forgot-password"> Lost Password? <span>Click Here</span></div>

      <div className='submit-container'>
        <div className="submit" onClick={onLogin}>Login</div>
        <div className="submit" onClick={onRegister}>Register</div>
      </div>
      {msg && <div className="msg">{msg}</div>}
    </div>
  )
}

export default Login_register