// modelo.js

class Atleta {
  constructor (nome, altura) {
    this.__nome = nome
    this.__altura = altura
  }

  get nome () {
    return this.__nome
  }

  get altura () {
    return this.__altura
  }
}

class Equipe {
  constructor (nome) {
    this.__nome = nome
    this.__atletas = []
  }

  adicione (atleta) {
    this.__atletas.push(atleta)
  }

  get nome () {
    return this.__nome
  }

  get atletas () {
    return this.__atletas
  }

  encontreAtletasComAlturmaMinima (alturaMinima) {
    // FIXME bug!
    var time = this.atletas
    var timeAltura = []
    for (var i = 0; i < time.length; i++) {
      if (time[i].altura >= alturaMinima){
        timeAltura.push(time[i])
      }
    }
  
    return timeAltura
  }
}

export {Atleta, Equipe}
