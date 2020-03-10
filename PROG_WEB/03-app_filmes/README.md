# UFSC - CTC - INE - INE5646 Programação para Web :: Exercício App Filmes

A aplicação mostra uma relação de filmes (título, ano de lançamento e diretor). O usuário pode ver os detalhes de um filme clicando um botão junto ao título do filme.

## Objetivo do Exercício

Mostrar uma aplicação do tipo SPA (*Single Page Application*) que utiliza a bilioteca [React](https://reactjs.org/) e o framework CSS [Bulma](https://bulma.io/) para o desenvolvimento do lado cliente. A aplicação também utiliza o agregador [webpack](https://webpack.js.org/) para gerar o arquivo JavaScript que é executado pelo browser.

## Instruções

Depois de baixar/clonar o respositório, entre no diretório **cliente** e digite

`npm install`

para instalar os pacotes JavaScript utilizados pelo lado cliente da aplicação.

Em seguida entre no diretório **servidor** e digite

`npm install`

para instalar os pacotes JavaScript utiliados pelo lado servidor da aplicação.

### Durante o desenvolvimento

O desenvolvimento da aplicação envolve duas frentes de trabalho: a programação necessária para o lado cliente e a programação necessária para o lado servidor.

#### Lado Cliente

Para iniciar o desenvolvimento do lado cliente entre no diretório **cliente** e digite

`npm start`

Cada vez que um arquivo no lado cliente for alterado o *webpack* será acionado para gerar uma nova versão dos arquivos necessários para o lado cliente. Estes arquivos são armazenados no diretório **publico** dentro do diretório **servidor**.

#### Lado Servidor

Para iniciar o desenvolvimento do lado servidor entre no diretório **servidor** e digite

`npm start`

A partir de então a aplicação estará disponível na porta 3000. Para acessar, use o navegador e digite o endereço `https://localhost:3000`

Sempre que um arquivo for salvo a aplicação irá reiniciar automaticamente (graças ao pacote **nodemon**).

### Em produção

Depois que o código da aplicação está pronto é preciso gerar as versões otimizadas (em termos de tamanho e velocidade de execução) dos arquivos do lado cliente e do lado servidor.

#### No Lado Cliente

Para gerar a versão em produção do lado cliente entre no diretório **cliente** e digite

`npm run build`

Observe que o tamanho do arquivo *bundle.js* diminui drasticamente de tamanho.

#### No Lado Servidor

Para gerar a versão em produção do lado servidor entre no diretório **servidor** e digite

`npm run build`

Para executar a aplicação em modo produção entre no diretório **servidor** e digite

`node build\app.js`
