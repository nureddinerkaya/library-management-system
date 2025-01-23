import React, { useState } from 'react';

export default function ManageCopies() {
    const [copies, setCopies] = useState([]);

    const addCopy = (e) => {
        e.preventDefault();
        const id = document.getElementById('CopyID').value;
        const name = document.getElementById('CopyName').value;
        const author = document.getElementById('CopyAuthor').value;
        const status = document.getElementById('CopyStatus').value;

        if (id && name && author && status) {
            setCopies([...copies, { id, name, author, status }]);
            document.getElementById('copiesForm').reset();
        } else {
            alert('Please fill in all fields.');
        }
    };

    const deleteCopy = (copyId) => {
        setCopies(copies.filter(copy => copy.id !== copyId));
    };

    return (
        <div id="copies" className="tab-content active">
            <h2>Manage Copies</h2>
            <form id="copiesForm" onSubmit={addCopy}>
                <label htmlFor="CopyID">Copy ID:</label>
                <input type="text" id="CopyID" placeholder="Enter Copy ID" />
                <label htmlFor="CopyName">Copy Name:</label>
                <input type="text" id="CopyName" placeholder="Enter Copy Name" />
                <label htmlFor="CopyAuthor">Copy Author:</label>
                <input type="text" id="CopyAuthor" placeholder="Enter Copy Author" />
                <label htmlFor="CopyStatus">Copy Status:</label>
                <input type="text" id="CopyStatus" placeholder="Enter Copy Status" />
                <button type="submit">Add Copy</button>
            </form>
            <table id="copiesTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Author</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {copies.map((copy, index) => (
                        <tr key={index}>
                            <td>{copy.id}</td>
                            <td>{copy.name}</td>
                            <td>{copy.author}</td>
                            <td>{copy.status}</td>
                            <td><button onClick={() => deleteCopy(copy.id)}>Delete</button></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
