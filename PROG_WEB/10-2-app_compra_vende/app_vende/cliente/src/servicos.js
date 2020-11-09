//@flow
import { PedidoProcessado } from './modelos'

const urlEnviaPedidoProcessado = '/CmdEnviePedidoProcessado'
const urlBuscaPedidos = '/CmdBbusquePedidos'

/**
  Envia pedido ao servidor e retorna Promise contendo resposta em
  formato JSON.
*/
const enviaPedidoProcessado =
  (pedidoProcessado: PedidoProcessado) =>
    processaRequisicaoPOST(urlEnviaPedidoProcessado, pedidoProcessado)

/**
  Busca pedidos e retorna Promise contendo resposta em
  formato JSON.
*/
const buscaPedidos = () => processaRequisicaoPOST(urlBuscaPedidos)


// envia requisição POST e retorna Promise com a resposta JSON.
function processaRequisicaoPOST(url, dados) {
  const params = {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify(dados)
  }

  return fetch(url, params)
    .then(resposta => {
      if (!resposta.ok)
        throw new Error('Falha na comunicação com servidor')
      return resposta
    })
    .then(resposta => resposta.json())
}

export {enviaPedidoProcessado, buscaPedidos}
