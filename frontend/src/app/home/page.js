"use client";

import React, { useState } from 'react';
import './page.css';

const books = [
    { "image": "https://via.placeholder.com/100", "title": "Book 1", "author": "Author 1", "stock": 10, "category": "Fiction" },
    { "image": "https://via.placeholder.com/100", "title": "Book 2", "author": "Author 2", "stock": 0, "category": "Non-fiction" },
    { "image": "https://via.placeholder.com/100", "title": "Book 3", "author": "Author 3", "stock": 5, "category": "Science" },
    { "image": "https://via.placeholder.com/100", "title": "Book 4", "author": "Author 4", "stock": 2, "category": "History" },
    { "image": "https://via.placeholder.com/100", "title": "Book 5", "author": "Author 5", "stock": 8, "category": "Biography" },
    { "image": "https://via.placeholder.com/100", "title": "Book 6", "author": "Author 6", "stock": 3, "category": "Fantasy" },
    { "image": "https://via.placeholder.com/100", "title": "Book 7", "author": "Author 7", "stock": 1, "category": "Mystery" },
];

export default function HomePage() {
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [popupBook, setPopupBook] = useState(null);
    const [showAccountPopup, setShowAccountPopup] = useState(false);
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const filteredBooks = selectedCategory ? books.filter(book => book.category === selectedCategory) : books;

    const handleCategoryClick = (category) => {
        setSelectedCategory(category);
    };

    const handleBookClick = (book) => {
        setPopupBook(book);
    };

    const handleReserve = () => {
        alert("Book reserved successfully!");
        setPopupBook(null);
    };

    const handlePasswordChange = () => {
        if (!newPassword || !confirmPassword) {
            alert("Please fill out both fields.");
            return;
        }

        if (newPassword !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        alert("Password changed successfully!");
        setShowAccountPopup(false);
    };

    return (
        <div>
            <header>
                <h1>Library Management System</h1>
                <div className="account-info" onClick={() => setShowAccountPopup(true)}>
                    John Doe (123456)
                </div>
            </header>
            <div className="main-container">
                <div className="sidebar">
                    <h3>Categories</h3>
                    <ul>
                        {['Fiction', 'Non-fiction', 'Science', 'History', 'Biography', 'Fantasy', 'Mystery'].map(category => (
                            <li key={category}>
                                <a href="#" onClick={() => handleCategoryClick(category)}>{category}</a>
                            </li>
                        ))}
                    </ul>
                </div>
                <div className="container">
                    <button className="back-button" onClick={() => window.location.href = "home.html"}>Go Back</button>
                    <h2>Available Books</h2>
                    <div className="books-grid">
                        {filteredBooks.map(book => (
                            <div className="book" key={book.title} onClick={() => handleBookClick(book)}>
                                <img src={book.image} alt="Book Cover" />
                                <h4>{book.title}</h4>
                                <p><strong>Author:</strong> {book.author}</p>
                                <p><strong>Stock:</strong> {book.stock}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {popupBook && (
                <div className="popup-overlay" onClick={() => setPopupBook(null)}>
                    <div className="popup" onClick={(e) => e.stopPropagation()}>
                        <img src={popupBook.image} alt="Book Cover" />
                        <h4>{popupBook.title}</h4>
                        <p><strong>Author:</strong> {popupBook.author}</p>
                        <p><strong>Stock:</strong> {popupBook.stock}</p>
                        <button onClick={handleReserve} disabled={popupBook.stock === 0}>Reserve</button>
                        <button onClick={() => setPopupBook(null)}>Close</button>
                    </div>
                </div>
            )}

            {showAccountPopup && (
                <div className="popup-overlay" onClick={() => setShowAccountPopup(false)}>
                    <div className="account-popup" onClick={(e) => e.stopPropagation()}>
                        <h4>Change Password</h4>
                        <input type="password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} placeholder="Enter new password" />
                        <input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} placeholder="Confirm new password" />
                        <button onClick={handlePasswordChange}>Change Password</button>
                        <button onClick={() => setShowAccountPopup(false)}>Cancel</button>
                    </div>
                </div>
            )}
        </div>
    );
}
