import React from 'react'
import User from './User'

export default function UserTable({ user }) {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Surname</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        {user.map(user => { return (<User key={user.id} user={user}/>)})}
      </tbody>
  </table>
  )
}
