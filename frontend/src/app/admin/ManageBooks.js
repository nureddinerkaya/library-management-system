import React, { useState } from 'react';

export default function ManageBooks() {
    const [books, setBooks] = useState([]);

    const addBook = () => {
        const title = document.getElementById('bookTitle').value;
        const author = document.getElementById('bookAuthor').value;
        const stock = document.getElementById('bookStock').value;

        if (title && author && stock) {
            setBooks([...books, { title, author, stock }]);
            document.getElementById('addBookForm').reset();
        } else {
            alert('Please fill all fields.');
        }
    };

    const deleteBook = (index) => {
        setBooks(books.filter((_, i) => i !== index));
    };

    return (
        <div id="books" className="tab-content active">
            <h2>Manage Books</h2>
            <form id="addBookForm">
                <label htmlFor="UploadImage">Upload Image</label>
                <input type="file" id="UploadImage" placeholder="upload upload image" />
                <label htmlFor="bookTitle">Book Title</label>
                <input type="text" id="bookTitle" placeholder="Enter book title" />
                <label htmlFor="bookAuthor">Author</label>
                <input type="text" id="bookAuthor" placeholder="Enter author name" />
                <label htmlFor="bookStock">Stock</label>
                <input type="number" id="bookStock" placeholder="Enter stock amount" />
                <button type="button" onClick={addBook}>Add Book</button>
            </form>
            <table id="booksTable">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Stock</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {books.map((book, index) => (
                        <tr key={index}>
                            <td>{book.title}</td>
                            <td>{book.author}</td>
                            <td>{book.stock}</td>
                            <td><button onClick={() => deleteBook(index)}>Delete</button></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
