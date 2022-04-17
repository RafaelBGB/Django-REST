import React, {useState} from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({item, deleteProject}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${item.uid}`}>{item.name}</Link>
            </td>
            <td>
                <button onClick={() => deleteProject(item.uid)} type="button">
                    Удалить
                </button>
            </td>
        </tr>
    )
}


const ProjectList = ({items, deleteProject}) => {
    const [name, setName] = useState('')
    const re = new RegExp(".{0,}" + name)

    function handleChange (event) {
        setName(event.target.value)
    }

    if (items.results) {

        console.log(items.results.filter((item) => item.name.match(re)))
        return (
            <div>
                <Link to="/projects/create">Создать проект</Link>
                <input type="text" className="form-control" name="search"
                       placeholder="Поиск по названию"
                        onChange={(event) =>
                            handleChange(event)}
                />
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
                        <th>
                            Название проекта
                        </th>
                        <th>

                        </th>
                    </tr>
                    </thead>
                    <tbody>
                    {items.results.filter((item) => item.name.match(re)).map((item) =>
                        <ProjectItem
                            item={item}
                            deleteProject={deleteProject}
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

export default ProjectList
