import React from "react"


const UserItem = ({user}) => {
    return(
        <tr>
            <td>
                {user.username}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
            <td>
                {user.email}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className={"table table-striped"}>
            <thead>
                <th>
                    Username
                </th>
                <th>
                    First name
                </th>
                <th>
                    Last name
                </th>
                <th>
                    Birthday year
                </th>
                <th>
                    Email
                </th>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user} />)}
            </tbody>
        </table>
    )
}

export default UserList;
