import React from "react";
import axios from "axios";
import {useLocation} from "react-router-dom";


function getPageUrl(url) {
    axios.get(url).then(response => {
        const items = response.data
        let location = window.location.pathname.replace(/\//g, '')
        console.log(url)

        if (!location) location = 'users'
        this.setState(
            {
                location: items
            }
        )
    }).catch(error => console.log(error))
    return window.location.pathname
}

const PaginationArea = ({items}) => {
    // let location = useLocation()
    // console.log(location.pathname)
    if (!items.next && !items.previous){
        return null
    }
    return (
        <nav aria-label={"Page navigation"}>
            <ul className={"pagination"}>
                <li className={`page-item ${!items.previous && "disabled"}`}>
                    <a className={"page-link"} href={getPageUrl(items.previous)}>
                        Назад
                    </a>
                </li>
                <li className={`page-item ${!items.next && "disabled"}`}>
                    <a className={"page-link"} href={getPageUrl(items.next)}>
                        Вперед
                    </a>
                </li>
            </ul>
        </nav>
    )
}

export default PaginationArea
