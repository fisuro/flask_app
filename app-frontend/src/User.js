import React from 'react'
import axios from 'axios'
import fetchEvents from "./App";

export default function User({user}) {
  function handleDelete(e){
      axios.delete(`/users/${user.id}`).then(() => {
        fetchEvents()
      })
  }
  function handleEdit(e){

  }
  return (
    <tr>
      <td key="id">{user.id}</td>
      <td key="name">{user.name}</td>
      <td key="surname">{user.surname}</td>
      <td key="email">{user.email}</td>
      <button onClick={handleDelete}>Delete</button>
      <button onClick={handleEdit}>Edit</button>
    </tr>)
      
}
