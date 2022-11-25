import React, {useState, useEffect} from 'react'
import './App.css'
import UserTable from './UserTable'

function DisplayUsers (){
const [users, setUsers] = useState([{}])

  useEffect(() => {
        fetch("/users").then(
          res => res.json()
        ).then(
          data => {
            setUsers(data)
            console.log(data)
          }
        )
      }, [])
  return (
    <div className='kita'>
      <table className='bratee'>
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>SURNAME</th>
            <th>EMAIL</th>
          </tr>
        </thead>
          <tbody>
            {users.map((user, i) => 
              <tr key={i}>
                <td className='redovi'>{user.id}</td>
                <td className='redovi'>{user.name}</td>
                <td className='redovi'>{user.surname}</td>
                <td className='redovi'>{user.email}</td>
              </tr>
              )}
          </tbody>
      </table>
    </div>
  )
}

async function loginUser(credentials) {
  return fetch('/users', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
 }

export default function AddUsers (){
  const [name, setName] = useState();
  const [surname, setSurname] = useState();
  const [email, setEmail] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    const response = await loginUser({
      name,
      surname,
      email
    });
    if ("email" in response) {
      DisplayUsers();
    }
  }

  return(
    <form onSubmit={handleSubmit}>
      <label>
        <p>USERNAME</p>
        <input type="text" onChange={e => setName(e.target.value)}/>
      </label>
      <label>
        <p>LAST NAME</p>
        <input type="text" onChange={e => setSurname(e.target.value)}/>
      </label>
      <label>
        <p>EMAIL</p>
        <input type="text" onChange={e => setEmail(e.target.value)}/>
      </label>
      <div>
        <button type="submit" >SUBMIT</button>
      </div>
    </form>
  )
}