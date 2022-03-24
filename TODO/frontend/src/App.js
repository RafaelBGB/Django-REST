import React from "react";
import axios from "axios";
import {BrowserRouter, Switch, Route} from "react-router-dom";

import './App.css';
import Menu from "./components/Main_menu";
import Footer from "./components/Footer";

import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import ProjectInfo from "./components/ProjectInfo";


const NotFound404 = () => {
    return (
        <div className={"d-flex flex-row align-items-center"}>
            <div className={"container"}>
                <div className={"col-md-12 text-center"}>
                    <span className={"display-1 d-block"}>404</span>
                    <div className={"md-4 lead"}>Страница не найдена!</div>
                    <a href={"/"} className={"btn btn-link"}>
                        Вернуться на главную
                    </a>
                </div>
            </div>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todo': []
        };
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
              const users = response.data
              this.setState(
                  {
                    'users': users
                  }
              )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
              const projects = response.data
              this.setState(
                  {
                    'projects': projects
                  }
              )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(response => {
              const todo = response.data
              this.setState(
                  {
                    'todo': todo
                  }
              )
        }).catch(error => console.log(error))


    }

    render() {
        return(
            <div>
                <BrowserRouter>
                    <header>
                        <Menu />
                    </header>
                    <div className={"main"}>
                        <Switch>
                            <Route exact path="/" component={() =>
                                <UserList items={this.state.users} />}
                            />
                            <Route exact path="/projects" component={() =>
                                <ProjectList items={this.state.projects} />}
                            />
                            <Route exact path="/todo" component={() =>
                                <ToDoList items={this.state.todo} />}
                            />
                            <Route exact path="/project/:uid" component={() =>
                                <ProjectInfo items={this.state.projects} todo={this.state.todo}/>}
                            />
                            <Route path={"*"} component={ NotFound404 } />
                        </Switch>
                    </div>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
}

export default App;
