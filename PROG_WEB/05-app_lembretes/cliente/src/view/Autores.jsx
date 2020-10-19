//@flow
import React, {useReducer} from 'react'
import type {Autor} from '../tipos_flow'

interface AutoresProps {
  autores: Autor[]
}

function Autores (props: AutoresProps) {
  const {autores} = props

  console.log(autores)
  return (
    <table className="table">
      <thead>
        <tr>
          <th>
            <abbr title="Número">No.</abbr>
          </th>
          <th>Nome</th>
          <th>Matrícula</th>
        </tr>
      </thead>
      <tbody>
        {autores.map((autor, i) => {
          return (
            <tr key={i}>
              <th>{i}</th>
              <td>{autor.nome}</td>
              <td>{autor.matricula}</td>
            </tr>
          )
        })} 
      </tbody>
    </table>
  )
}
  
export default Autores
