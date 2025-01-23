import React, { useState } from 'react';

export default function ManageBorrowings() {
    const [borrowings, setBorrowings] = useState([]);

    const addBorrowing = (e) => {
        e.preventDefault();
        const borrowingID = document.getElementById("BorrowingID").value;
        const memberID = document.getElementById("BorrowingMemberID").value;
        const bookID = document.getElementById("BorrowingBookID").value;

        if (borrowingID && memberID && bookID) {
            setBorrowings([...borrowings, { borrowingID, memberID, bookID, status: "pending" }]);
            document.getElementById("borrowingsForm").reset();
        } else {
            alert("Please fill in all fields.");
        }
    };

    const updateStatus = (index, newStatus) => {
        const updatedBorrowings = [...borrowings];
        updatedBorrowings[index].status = newStatus;
        setBorrowings(updatedBorrowings);
    };

    const deleteBorrowing = (index) => {
        setBorrowings(borrowings.filter((_, i) => i !== index));
    };

    return (
        <div id="borrowings" className="tab-content active">
            <h2>Manage Borrowings</h2>
            <form id="borrowingsForm" onSubmit={addBorrowing}>
                <label htmlFor="BorrowingID">Borrowing ID</label>
                <input type="text" id="BorrowingID" placeholder="Enter Borrowing ID" />
                <label htmlFor="BorrowingMemberID">Member ID</label>
                <input type="text" id="BorrowingMemberID" placeholder="Enter Member ID" />
                <label htmlFor="BorrowingBookID">Book ID</label>
                <input type="text" id="BorrowingBookID" placeholder="Enter Book ID" />
                <button type="submit">Add Borrowing</button>
            </form>
            <div>
                <h3>Filter Borrowings by Status</h3>
                <label htmlFor="statusFilter">Select Status:</label>
                <select id="statusFilter" onChange={(e) => filterBorrowingsByStatus(e.target.value)}>
                    <option value="all">All</option>
                    <option value="pending">Borrowed</option>
                    <option value="returned">Returned</option>
                    <option value="overdue">Active</option>
                    <option value="overdue">Pending</option>
                </select>
            </div>
            <h3>Borrowings List</h3>
            <table border="1" width="100%">
                <thead>
                    <tr>
                        <th>Borrowing ID</th>
                        <th>Member ID</th>
                        <th>Book ID</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {borrowings.map((borrowing, index) => (
                        <tr key={index}>
                            <td>{borrowing.borrowingID}</td>
                            <td>{borrowing.memberID}</td>
                            <td>{borrowing.bookID}</td>
                            <td>{borrowing.status}</td>
                            <td>
                                <button onClick={() => updateStatus(index, 'active')}>Active</button>
                                <button onClick={() => updateStatus(index, 'returned')}>Returned</button>
                                <button onClick={() => deleteBorrowing(index)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
