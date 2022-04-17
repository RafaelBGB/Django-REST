import React from "react";
import {Link} from "react-router-dom";


const ToDoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>
                {item.name_todo}
            </td>
            <td>
                {item.author}
            </td>
            <td>
                {item.status}
            </td>
            <td>
                <button onClick={() => deleteTodo(item.uid)} type="button">
                    Удалить
                </button>
            </td>
        </tr>
    )
}

const ToDoList = ({items, deleteTodo}) => {
    if (items.results) {
        return (
            <div className={"container"}>
                <Link to="/todo/create">Создать проект</Link>
                <table className={"table table-striped"}>
                    <thead>
                    <th>
                        Название заметки
                    </th>
                    <th>
                        Автор
                    </th>
                    <th>
                        Статус
                    </th>
                    <th>

                    </th>
                    </thead>
                    <tbody>
                    {items.results.map((item) => <ToDoItem
                        item={item}
                        deleteTodo={deleteTodo}
                    />)}
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
