"use client";

import React, { useState } from 'react';
import './page.css';

export default function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
        if (username === 'admin' && password === '1234') {
            window.location.href = '/admin';
        } else if (username === 'user' && password === '2345') {
            window.location.href = '/home';
        } else {
            alert('Invalid username or password. Please try again.');
        }
    };

    return (
        <div className="login-container">
            <h1>Library Login</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        placeholder="Enter your username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                        type={showPassword ? 'text' : 'password'}
                        id="password"
                        name="password"
                        placeholder="Enter your password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <div className="show-password">
                        <input
                            type="checkbox"
                            id="showPassword"
                            checked={showPassword}
                            onChange={() => setShowPassword(!showPassword)}
                        /> Show Password
                    </div>
                </div>
                <button type="submit" className="login-button">Login</button>
            </form>
        </div>
    );
}