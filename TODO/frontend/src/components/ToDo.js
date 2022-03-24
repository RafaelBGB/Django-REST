import React from "react";


const ToDoItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.name_todo}
            </td>
            <td>
                {item.author}
            </td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    if (items.results) {
        return (
            <div className={"container"}>
                <table className={"table table-striped"}>
                    <thead>
                    <th>
                        ToDo's name
                    </th>
                    <th>
                        author
                    </th>
                    </thead>
                    <tbody>
                    {items.results.map((item) => <ToDoItem item={item}/>)}
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

export default ToDoList
