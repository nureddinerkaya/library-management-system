import React, { useState, useEffect } from 'react';

export default function ManageMembers() {
    const [members, setMembers] = useState([
        { name: "John", lastName: "Doe", id: "M001", department: "IT" },
        { name: "Jane", lastName: "Smith", id: "M002", department: "HR" },
        { name: "Alice", lastName: "Johnson", id: "M003", department: "Marketing" },
        { name: "Bob", lastName: "Brown", id: "M004", department: "Finance" },
    ]);
    const [editingIndex, setEditingIndex] = useState(null);

    const addMember = (e) => {
        e.preventDefault();
        const name = document.getElementById("MemberName").value;
        const lastName = document.getElementById("MemberLastName").value;
        const id = document.getElementById("MemberID").value;
        const department = document.getElementById("MemberDepartment").value;

        if (name && lastName && id && department) {
            setMembers([...members, { name, lastName, id, department }]);
            document.getElementById("membersForm").reset();
        } else {
            alert("Please fill in all fields.");
        }
    };

    const editMember = (index) => {
        const member = members[index];
        document.getElementById("MemberName").value = member.name;
        document.getElementById("MemberLastName").value = member.lastName;
        document.getElementById("MemberID").value = member.id;
        document.getElementById("MemberDepartment").value = member.department;
        setEditingIndex(index);
    };

    const saveMember = (e) => {
        e.preventDefault();
        const name = document.getElementById("MemberName").value;
        const lastName = document.getElementById("MemberLastName").value;
        const id = document.getElementById("MemberID").value;
        const department = document.getElementById("MemberDepartment").value;

        if (name && lastName && id && department) {
            const updatedMembers = [...members];
            updatedMembers[editingIndex] = { name, lastName, id, department };
            setMembers(updatedMembers);
            setEditingIndex(null);
            document.getElementById("membersForm").reset();
        } else {
            alert("Please fill in all fields.");
        }
    };

    const deleteMember = (index) => {
        setMembers(members.filter((_, i) => i !== index));
    };

    return (
        <div id="members" className="tab-content active">
            <h2>Manage Members</h2>
            <form id="membersForm" onSubmit={editingIndex === null ? addMember : saveMember}>
                <label htmlFor="MemberName">Member Name:</label>
                <input type="text" id="MemberName" placeholder="Enter User Name" />
                <label htmlFor="MemberLastName">Member Last Name:</label>
                <input type="text" id="MemberLastName" placeholder="Enter User Last Name" />
                <label htmlFor="MemberID">Member ID:</label>
                <input type="text" id="MemberID" placeholder="Enter User ID" />
                <label htmlFor="MemberDepartment">Member Department:</label>
                <input type="text" id="MemberDepartment" placeholder="Enter User Department" />
                <button type="submit">{editingIndex === null ? "Add Member" : "Save Changes"}</button>
                {editingIndex !== null && <button type="button" onClick={() => setEditingIndex(null)}>Cancel Edit</button>}
            </form>
            <div>
                <h3>Search Members</h3>
                <label htmlFor="searchCriteria">Search By:</label>
                <select id="searchCriteria">
                    <option value="name">Name</option>
                    <option value="lastName">Last Name</option>
                    <option value="id">ID</option>
                    <option value="department">Department</option>
                </select>
                <input type="text" id="searchBox" placeholder="Enter search term" />
            </div>
            <div id="membersList">
                <h3>Members List</h3>
                <table border="1" width="100%">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Last Name</th>
                            <th>ID</th>
                            <th>Department</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {members.map((member, index) => (
                            <tr key={index}>
                                <td>{member.name}</td>
                                <td>{member.lastName}</td>
                                <td>{member.id}</td>
                                <td>{member.department}</td>
                                <td>
                                    <button onClick={() => editMember(index)}>Edit</button>
                                    <button onClick={() => deleteMember(index)}>Delete</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
