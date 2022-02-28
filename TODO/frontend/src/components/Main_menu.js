import React from "react";


const Menu = () => {
    return (
        <div className={"header clearfix"}>
            <a href={"#"} className={"logo"}></a>
            <ul className={"menu"}>
                <li>
                    <a href={"#"}>домой</a>
                </li>
                <li>
                    <a href={"#"}>пользователи</a>
                </li>
                <li>
                    <a href={"#"}>войти</a>
                </li>
            </ul>
        </div>
    )
}

export default Menu;
