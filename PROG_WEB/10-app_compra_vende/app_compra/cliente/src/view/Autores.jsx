// @flow
import React from 'react'

// eslint-disable-next-line linebreak-style
type Autor = {|
  nome: string,
  matricula: number,
|};

const autores: Array<Autor> = [
  { nome: 'Adam Pereira Gomes', matricula: 19200408 },
  { nome: 'Bruno Duarte Barreto Borges', matricula: 18100519 },
  { nome: 'João Felipe Uller', matricula: 17102812 },
  { nome: 'Pedro Henrique Dias Nobrega', matricula: 19100876 },
  { nome: 'Rafael Nilson Witt', matricula: 18200649 },
]

function Autores() {
  return (
    <div
      style={{
        backgroundColor: '#888',
        borderColor: '#555',
        borderWidth: 1,
        padding: '1rem',
      }}
    >
      <table className="table is-bordered is-striped is-narrow is-hoverable is-fullwidth" style={{ width: '100%' }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Matrícula</th>
          </tr>
        </thead>
        <tbody>
          {autores.map((autor, i) => (
            <tr key={i}>
              <td>{i + 1}</td>
              <td>{autor.nome}</td>
              <td>{autor.matricula}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Autores
