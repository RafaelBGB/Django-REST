import React from "react";
import {useParams} from "react-router-dom";

const ProjectInfo = ({items, todo}) => {

    let {uid} = useParams()
    if (items.results && todo.results) {
        let project = items.results.filter((item) => item.uid === uid)[0]
        let project_todo = todo.results.filter((item) => item.project ===  (`http://127.0.0.1:8000/api/projects/${uid}/` ))
        return (
            <div>
                <div>
                    <b>Название проекта</b>
                            <p>{project.name}</p>
                            <a href={project.url_on_repo}>Ссылка на репозиторий</a>
                </div>
                <br/>

                <p className={"text-center"}>
                    <strong>Список участников проекта</strong>
                </p>

                <ul className={"list-group"}>
                    {project.users.map(user => {
                        return (
                            <li className={"list-group-item"}>{user}</li>
                        )
                    })}
                </ul>

                <p className={"text-center"}>
                    <strong>Список заметок в проекте</strong>
                </p>

                <ul className={"list-group"}>
                    {project_todo.map(item => {
                        return (
                            <li className={"list-group-item"}>{item.name_todo}</li>
                        )
                    })}
                </ul>

            </div>
        )
    }
    return (
        <div>

        </div>
    )
}

export default ProjectInfo
