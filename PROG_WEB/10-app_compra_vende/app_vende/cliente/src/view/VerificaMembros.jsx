import TabelaMembros from './TabelaMembros.jsx'
import React, {useReducer, useEffect} from 'react'
import Autor from '../tipos_flow'

const autores: Autor[] = [
  {
    nome: "Adan Pereira Gomes",
    matricula: 19200408
  },
  {
    nome: "Bruno Duarte Barreto Borges",
    matricula: 18100519
  },
  {
    nome: "Joao Fellipe Uller",
    matricula: 17102812
  },
  {
    nome: "Pedro Henrique Dias Nobrega",
    matricula: 19100876
  },
  {
    nome: "Rafael Nilson Witt",
    matricula: 18200649
  }
]  

type Estado = {|
  mostrandoAutores: boolean,
  autores: []
|}

type Acao = 
| { type: 'MOSTRE_AUTORES' }
| { type: 'ESCONDA_AUTORES' }


type Dispatch = Acao => void

type Modelo = [Estado, Dispatch]

const estadoInicial: Estado = {
  mostrandoAutores: false,
  autores: []
}

function reducer(estado: Estado, acao: Acao): Estado {
  switch (acao.type) {
  case 'MOSTRE_AUTORES':
    return {...estadoInicial, mostrandoAutores: true, autores: autores}
      
  case 'ESCONDA_AUTORES':
    return {...estadoInicial, mostrandoAutores: false, autores: []}

  }
}

function useModelo(): Modelo {
    const [estado, dispatch] = useReducer(reducer, estadoInicial)
    
    useEffect(() => {
        if(estadoInicial){
            dispatch({type: 'MOSTRE_AUTORES'})    
        }
    }, [estado.mostrandoAutores])

    useEffect(() => {
        if (!estadoInicial) {
            dispatch({type: 'ESCONDA_AUTORES'})
        }
  }, [estado.mostrandoAutores])

  return [estado, dispatch]
}

