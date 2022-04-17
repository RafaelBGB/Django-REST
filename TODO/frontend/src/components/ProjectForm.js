import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            users: [props.users[0]?.uid],
            url_on_repo: ''
        }
    }

    handleChange(event) {
        if ([event.target.name] == 'users'){
            this.setState(
                {'users': [event.target.value]}
            )
        }
        else {
            this.setState(
                {[event.target.name]: event.target.value}
            )
        }
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.users, this.state.url_on_repo)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name">Название</label>
                    <input type="text" className="form-control" name="name"
                        value={this.state.name} onChange={(event) => this.handleChange(event)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="users">Участник проекта</label>
                    <select name="users" className="form-control" onChange={(event) =>
                                this.handleChange(event)}>
                        {this.props.users.map((item) =>
                            <option value={item.uid}>
                                {item.username}
                            </option>
                        )}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="url_on_repo">Ссылка на репозиторий</label>
                    <input type="text" className="form-control" name="url_on_repo"
                           value={this.state.url}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div>
                    <input type="submit" className="btn btn-primary" value="Сохранить"/>
                </div>
            </form>
        )

    }
}

export default ProjectForm
