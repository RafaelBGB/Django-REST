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

const UserList = ({items}) => {
    if (items.results) {
        return (
            <div>
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
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
                    </tr>
                    </thead>
                    <tbody>
                    {items.results.map((user) => <UserItem user={user}/>)}
                    </tbody>
                </table>
            </div>
        )
    }
    return (
        <div>

        </div>
    )
}

export default UserList;
