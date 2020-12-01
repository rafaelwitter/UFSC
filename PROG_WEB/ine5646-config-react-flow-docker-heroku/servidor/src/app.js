// @flow

import {PORTA, TEMPO} from './env'

import http from 'http'
import path from 'path'
import express from 'express'


const app = express()

app.use(express.json())
app.use(express.static(path.resolve(__dirname, '../publico')))

app.get('/limites', (req, res) => {
  // esperar TEMPO segundos para responder
  setTimeout(() => res.json({min: 3, max: 10}), TEMPO *1000)
})

const server = http.createServer(app)

// eslint-disable-next-line no-console
server.listen(PORTA, () => console.log(`Servidor no ar na porta ${PORTA}...`))
