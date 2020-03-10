//@flow

import React from 'react'
import util_masks from './util_masks'

import CadastraEmMassa from './CadastraEmMassa.jsx'

type Props = {| cancelar: void => void |}

function CadastraVeiculosEmMassa (props: Props) {
  const orientacoes = {
    titulo: 'Cadastro em Massa de Veículos',
    subtitulo: 'Digite a placa, o CPF do proprietário e o ano de fabricação',
    exemplo: `ABA2018,${util_masks.cpfMask},1976`

  }
  return <CadastraEmMassa tipo='veiculo' orientacoes={orientacoes} cancelar={props.cancelar}/>
}


export default CadastraVeiculosEmMassa
