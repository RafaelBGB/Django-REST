import React from "react";
import {Link} from "react-router-dom";


class Menu extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className={"header clearfix"}>
                <Link to="/">
                    <img className={"logo"}
                         src={"https://img.icons8.com/ios/50/000000/checklist--v1.png"}
                         alt={"логотип"}
                    />
                </Link>
                <ul className="menu">
                    <li>
                        <Link to="/">пользователи</Link>
                    </li>
                    <li>
                        <Link to="/projects/">проекты</Link>
                    </li>
                    <li>
                        <Link to="/todo/">заметки</Link>
                    </li>
                    <li>
                        {this.props.is_authentication() ?
                            <div>
                                <span>
                                    {this.props.username}
                                </span>
                                <Link to="/" onClick={() => this.props.logout()}>logout</Link>
                            </div>
                            : <Link to="/login/" >войти</Link>}

                    </li>
                </ul>
            </div>
        )
    }


}

export default Menu;
