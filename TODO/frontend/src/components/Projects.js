import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${item.uid}`}>{item.name}</Link>
            </td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    if (items.results) {
        return (
            <div>
                <table className={"table table-striped"}>
                    <thead>
                    <tr>
                        <th>
                            Project's name
                        </th>
                    </tr>
                    </thead>
                    <tbody>
                    {items.results.map((item) => <ProjectItem item={item}/>)}
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
