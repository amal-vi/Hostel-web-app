import React from 'react'
import {Link} from 'react-router-dom'
import styles from '../pages/Login.module.css'

function Login() {
  return (
    <>
  <div className={styles.login_container}>
    <h2>Login</h2>
    <form action="{{ url_for('auth.login') }}" method="POST">
      <input type="text" name="username" placeholder="Email" required="" />
      <input
        type="password"
        name="password"
        placeholder="Password"
        required=""
      />
      <button type="submit">Login</button>
    </form>
    <div className={styles.footer}>
        <Link to='/StudentReg'>Student Registration →</Link>
    </div>
    <div className={styles.footer}>
      <Link to='/WardenReg'>Warden Registration →</Link>
        
    </div>
  </div>
    </>
  )
}

export default Login