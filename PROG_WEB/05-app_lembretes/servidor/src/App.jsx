//@flow
import React, {useEffect, useReducer} from 'react'
import jwt from 'jsonwebtoken'

import Login from './Login.jsx'
import Autores from './Autores.jsx'
import PublicaLembrete from './PublicaLembrete.jsx'
import MostraLembretes from './MostraLembretes.jsx'

import 'bulma/css/bulma.min.css'

import type {Token, TokenDecodificado, Autor} from '../tipos_flow'

type Estado = {
  token: Token | void,
  tokenDecodificado: TokenDecodificado | void,
  mostrandoAutores: boolean,
  autores: Array<Autor>
}

type Acao = 
  {type: 'REGISTRE_TOKEN', token: Token, tokenDecodificado: TokenDecodificado }
| { type: 'RECEBA_NOVO_TOKEN', token: Token }
| { type: 'REGISTRE_USUARIO_SAIU' }
| { type: 'MOSTRE_AUTORES' }
| { type: 'ESCONDA_AUTORES' }

const estadoInicial: Estado = {
  token: undefined,
  tokenDecodificado: undefined,
  mostrandoAutores: false,
  autores: []
}

const autores: Autor[] = [
  {
    nome: "Thais Goulart Firmino",
    matricula: 17103973
  },
  {
    nome: "Cleberton de Souza Oliveira",
    matricula: 17205083
  },
  {
    nome: "Alceu Ramos Conceição Júnior",
    matricula: 14200720
  },
  {
    nome: "Pedro Gandra Della Giustina",
    matricula: 18202534
  },
  {
    nome: "Rafael Nilson Witt",
    matricula: 18200649
  },

]

function reducer(estado: Estado, acao: Acao): Estado {
  switch (acao.type) {
  case 'REGISTRE_TOKEN':
    return {token: acao.token, tokenDecodificado: acao.tokenDecodificado, mostrandoAutores: false, autores: []}    
  
  case 'RECEBA_NOVO_TOKEN': 
    return {token: acao.token, tokenDecodificado: jwt.decode(acao.token), mostrandoAutores: false, autores: []}
  
  case 'REGISTRE_USUARIO_SAIU':
    return estadoInicial

  case 'MOSTRE_AUTORES':
    return {token: estado.token, tokenDecodificado: estado.tokenDecodificado, mostrandoAutores: true, autores: autores}
      
  case 'ESCONDA_AUTORES':
    return {token: estado.token, tokenDecodificado: estado.tokenDecodificado, mostrandoAutores: false, autores: []}
    
  default:
    throw new Error(`BUG: acao.type inválido: ${acao.type}`)
  }
}

function tokenValido(tokenDecodificado: TokenDecodificado): boolean {
  if(tokenDecodificado) { 
    const agora: number = Date.now()
    const exp = tokenDecodificado.exp * 1000
    return agora < exp
  } else {
   return false
  }
  
}

// FIXME Não há nade de errado com esta aplicação. A tarefa consiste em
// colocar a aplicação na sua máquina virtual na nuvem da UFSC.

function App () {
  const [estado, dispatch] = useReducer(reducer, estadoInicial)

  useEffect(() => {
    let token = window.localStorage.getItem('token')
    let tokenDecodificado

    if (token === null)
      token = undefined
    else {
      tokenDecodificado = jwt.decode(token)
      if (tokenValido(tokenDecodificado))
        dispatch({type: 'REGISTRE_TOKEN', token, tokenDecodificado})
      else
        window.localStorage.removeItem('token')
    }
  }, [])

  useEffect(() => {
    if (estado.token !== undefined) {
      window.localStorage.setItem('token', estado.token)
    }
    else {
      window.localStorage.removeItem('token')
    }
  }, [estado.token])

  return (
    <div className='container is-fluid'>
      <div className='message'>
        <div className='message-header'>
            UFSC - CTC - INE - INE5646 :: App lembretes ::
        </div>
        <div className='message-body'>
          {!estado.mostrandoAutores ? (
            <>
              <button 
                className='button is-warning' 
                onClick={() => dispatch({type: 'MOSTRE_AUTORES'})}
              >
                Mostrar autores
              </button>
              <Login onToken={token => dispatch({type: 'RECEBA_NOVO_TOKEN', token})}
                onSaiu={() => dispatch({type: 'REGISTRE_USUARIO_SAIU'})}
                token={estado.token}
                tokenDecodificado={estado.tokenDecodificado}/>
              {
                estado.token &&
                  <PublicaLembrete token={estado.token}
                    onTokenInvalido={() => dispatch({type: 'REGISTRE_USUARIO_SAIU'})}/>
              }
              {
                estado.token &&
                  <MostraLembretes token={estado.token}
                    onTokenInvalido={() => dispatch({type: 'REGISTRE_USUARIO_SAIU'})}/>
              }
            </>
          ) : (
            <>
              <Autores autores={estado.autores}/>
              <button 
                className='button is-success' 
                onClick={() => dispatch({type: 'ESCONDA_AUTORES'})}
              >
                OK
              </button>
            </>
          )}
          
        </div>
      </div>
    </div>
  )
}

export default App

