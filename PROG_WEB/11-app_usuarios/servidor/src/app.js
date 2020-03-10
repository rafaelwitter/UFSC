//@flow
import https from 'https'
import fs from 'fs'
import { PORTA } from './env'
import path from 'path'
import express from 'express'
import {processaComando} from './processadorDeComando'
import {processaConsulta} from './processadorDeConsulta'

import type {Comando, Consulta} from './tipos_flow'

const opcoes = {
  key: fs.readFileSync(path.join(__dirname, '../cert/key.pem')),
  cert: fs.readFileSync(path.join(__dirname, '../cert/cert.pem'))
}

const app = express()
app.use(express.json())
app.use(express.static('publico'))

app.post('/comando/:cmd', (req, res) => {
  const comando: Comando = {type: req.params.cmd, ...req.body}
  processaComando(comando)
    .then(resultado => res.json(resultado))
})

app.post('/consulta/:cst', (req, res) => {
  const consulta: Consulta = {type: req.params.cst, ...req.body}
  processaConsulta(consulta)
    .then(resultado => res.json(resultado))
})

const server = https.createServer(opcoes, app)

// eslint-disable-next-line no-console
server.listen(PORTA, () => console.log(`Servidor no ar na porta ${PORTA}...`))
