"use client";

import React, { useState } from 'react';
import './page.css';
import ManageBooks from './ManageBooks';
import ManageCopies from './ManageCopies';
import ManageMembers from './ManageMembers';
import ManageBorrowings from './ManageBorrowings';

export default function AdminPage() {
    const [activeTab, setActiveTab] = useState('books');

    const showTab = (tabId) => {
        setActiveTab(tabId);
    };

    return (
        <div>
            <header>
                <h1>Library Management System - Admin Panel</h1>
            </header>
            <div className="sidebar">
                <ul>
                    <li><a href="#" onClick={() => showTab('books')}>Manage Books</a></li>
                    <li><a href="#" onClick={() => showTab('copies')}>Manage Copies</a></li>
                    <li><a href="#" onClick={() => showTab('members')}>Manage Members</a></li>
                    <li><a href="#" onClick={() => showTab('borrowings')}>Manage Borrowings</a></li>
                </ul>
            </div>
            <div className="main">
                {activeTab === 'books' && <ManageBooks />}
                {activeTab === 'copies' && <ManageCopies />}
                {activeTab === 'members' && <ManageMembers />}
                {activeTab === 'borrowings' && <ManageBorrowings />}
            </div>
        </div>
    );
}