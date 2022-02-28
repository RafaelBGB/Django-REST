import React from "react";
import axios from "axios";
import './App.css';
import UserList from "./components/Users";
import Menu from "./components/Main_menu";
import Footer from "./components/Footer";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          'users': []
        };
    }

    componentDidMount() {
        document.title = 'Пользователи'
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
              const users = response.data
              this.setState(
                  {
                    'users': users
                  }
              )
        }).catch(error => console.log(error))
    }

    render() {
        return(
            <section>
                <Menu />
                <UserList users={this.state.users} />
                <Footer />
            </section>
        )
    }
}

export default App;
