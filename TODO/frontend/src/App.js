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
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie/es6";


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
            'todo': [],
            'token': '',
            'username': ''
        };
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post(
            'http://127.0.0.1:8000/api-token-auth/',
            {'username': username, 'password': password}
        ).then(response => {
            this.setState(
                {
                    'token': 'Token ' + response.data.token
                }
            )
            this.setState({'username': username})
            this.set_token(this.state.token)
        }).catch(error => alert('Неверный логин или пароль'))


    }

    get_headers() {
        let headers = {'Content-Type': 'application/json'}
        if (this.is_authenticated()){
            headers['Authorization'] = this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            const users = response.data ? response.data: [{}]
            this.setState(
                {
                    'users': users
                }
            )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
            const projects = response.data
            this.setState(
                {
                    'projects': projects
                }
            )
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(response => {
            const todo = response.data ? response.data: [{}]
            this.setState(
                {
                    'todo': todo
                }
            )
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <header>
                        <Menu is_authentication={() => this.is_authenticated()}
                              logout={() => this.logout()}
                              username = {this.state.username}
                        />
                    </header>
                    <div className={"main"}>
                        <Switch>
                            <Route exact path="/login" component={() =>
                                <LoginForm get_token={
                                    (username, password) =>
                                        this.get_token(username, password)
                                }/>}
                            />
                            <Route exact path="/" component={() =>
                                <UserList items={this.state.users}/>}
                            />
                            <Route exact path="/projects" component={() =>
                                <ProjectList items={this.state.projects}/>}
                            />
                            <Route exact path="/todo" component={() =>
                                <ToDoList items={this.state.todo}/>}
                            />
                            <Route exact path="/project/:uid" component={() =>
                                <ProjectInfo items={this.state.projects}
                                             todo={this.state.todo}/>}
                            />
                            <Route path={"*"} component={NotFound404}/>
                        </Switch>
                    </div>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
