import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';  // new
import UsersList from './components/UsersList'
import AddUser from './components/AddUser'


class App extends Component {
  constructor() {
    super();
    this.state = {
        users: [],
        username: '', // new
        email: ''
    };
    this.addUser = this.addUser.bind(this);  // new
    this.handleChange = this.handleChange.bind(this);  // new
  }

  componentDidMount() {
    this.getUsers(); 
  };

  handleChange(event) {
  const obj = {};
  obj[event.target.name] = event.target.value;
  this.setState(obj);
};

  // new
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users }); })  //傳回來在debug console看到的結構就是data.data.users
    .catch((err) => { console.log(err); });
  }

    addUser(event) {
        event.preventDefault();
        // new
        const data = {
        username: this.state.username,
        email: this.state.email
      };
      // new
      axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then((res) => { 
            this.getUsers();  // new
            this.setState({ username: '', email: '' });  // new
      })
      .catch((err) => { console.log(err); });
    }

  render() {
  return (
    <section className="section">
      <div className="container">
        <div className="columns">
          <div className="column is-half">  {/* new */}
            <br/>
            <h1 className="title is-1">All Users</h1>
            <hr/><br/>
            <AddUser 
                addUser={this.addUser} 
                username={this.state.username}
                email={this.state.email}
                handleChange={this.handleChange}  // new
            />  {/* new */}
            <br/><br/>  {/* new */}
            <UsersList users={this.state.users}/>
          </div>
        </div>
      </div>
    </section>
  )
   }
};

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
