import UserTable from "./UserTable";
import { useState, useRef, useEffect } from "react";
// import uuid from 'react-uuid'
import axios from 'axios'
import './App.css'

function App() {
  const userNameRef = useRef()
  const userSurnameRef = useRef()
  const userEmailRef = useRef()
  const [userList, setUserList] = useState([])

  axios.defaults.baseURL = 'http://127.0.0.1:5000/';

  const fetchEvents = async() => {
    const response = await axios.get('/users')
    setUserList(response.data)
  }
  

  useEffect(()=>{
    fetchEvents()
  },[])

  function handleAddUser(e){
    const name = userNameRef.current.value
    const surname = userSurnameRef.current.value
    const email = userEmailRef.current.value

    if (name === '' || surname === '' || email === '') return

    axios.post('/users', {name: name, surname: surname, email: email}).then(() => {
      fetchEvents()
    })
    userNameRef.current.value = null
    userSurnameRef.current.value = null
    userEmailRef.current.value =null
  }

    return (
        <form>
          <div className="login">
          <label><b>Username</b></label>
            <input ref={userNameRef} type="text" placeholder="Name" name="fname" required/>
            <input ref={userSurnameRef} type="text" placeholder="Surname" name="sname" required/>
            <input ref={userEmailRef} type="email" placeholder="Email" name="email" required/>
            <button onClick={handleAddUser}>Submit</button>
          </div>
          <div>
          </div>
          <div>
            <UserTable user={userList}/>
          </div>
        </form>
    );
  }

export default App;
