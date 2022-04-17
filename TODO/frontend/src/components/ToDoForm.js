import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            name_todo: '',
            project: props.project[0]?.uid,
            author: props.author[0]?.uid,
            text: ''
        }
    }

    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        )
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.name_todo, this.state.project, this.state.author, this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name_todo">Название заметки</label>
                    <input type="text" className="form-control" name="name_todo"
                        value={this.state.name_todo} onChange={(event) =>
                            this.handleChange(event)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="project">Проект</label>
                    <select name="project" className="form-control" onChange={(event) =>
                            this.handleChange(event)}>
                        {this.props.project.map((item) =>
                            <option value={item.uid}>
                                {item.name}
                            </option>
                        )}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="author">Проект</label>
                    <select name="author" className="form-control" onChange={(event) =>
                            this.handleChange(event)}>
                        {this.props.author.map((item) =>
                            <option value={item.uid}>
                                {item.username}
                            </option>
                        )}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="text">Текст заметки</label>
                    <input type="text" className="form-control" name="text"
                        value={this.state.text} onChange={(event) =>
                            this.handleChange(event)}
                    />
                </div>
                <div>
                    <input type="submit" className="btn btn-primary" value="Сохранить"/>
                </div>
            </form>
        )
    }
}

export default ToDoForm
