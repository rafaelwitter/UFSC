# UFSC-CTC-INE-INE5646 Programação para Web -- App Config React Flow - Versão Docker Heroku

Aplicação para demonstrar quais são os arquivos de configuração, no lado cliente e no lado servidor, que toda aplicação baseada em React, Bulma e Flow deve ter para poder rodar em um container docker cuja imagem será instalada no Heroku.

## Configuração no seu computador

O progrma Docker Desktop precisa estar instalado e em execução na sua máquina. Acesse [https://www.docker.com/get-started](https://www.docker.com/get-started) para saber como fazer isso.

Se o VSCode for utilizado então é preciso instalar a extensão [Remote Development da Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).


Você também precisa criar uma conta no [Heroku](https://heroku.com) e instalar o programa `heroku` no seu computador. Acesse [https://devcenter.heroku.com/articles/heroku-cli#download-and-install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) para download do programa.

## Instruções

### Durante o desenvolvimento com VSCode

#### Preparação Inicial

Os procedimentos a seguir devem ser realizados uma única vez.

##### Configurando arquivo .env

Crie, no diretório raiz do projeto ***no seu computador local***, o arquivo **.env** com o seguinte conteúdo

```bash
SEGUNDOS_AGUARDANDO=2
PORTA=3000
```

A variável de ambiente `SEGUNDOS_AGUARDANDO` define quantos segundos o lado servidor deve aguardar para enviar uma resposta ao lado cliente, simulando com isso um processamento demorado.

A variável de ambiente `PORTA` ***é opcional*** e define a porta utilizada pelo servidor. Se não estiver definida será usada a porta **3000**. No entanto, quando o container for instalado no Heroku a variável `PORT` conterá a porta da aplicação. Essa variável é definida pelo próprio Heroku.

O arquivo **.env** também pode ser usado para armazenar dados sigilosos como senhas, chaves, etc. Essas informações nunca devem ser armazenadas em locais públicos (como repositórios git ou repositórios de imagens docker).

##### Instalando bibliotecas JavaScript

Abra um terminal e instale as bibliotecas JavaScript usadas pelo lado cliente da aplicação:

```bash
cd cliente
npm install
```

Abra um terminal e instale as bibliotecas JavaScript usadas pelo lado servidor da aplicação:

```bash
cd servidor
npm install
```

#### Durante o desenvolvimento

Para colocar a aplicação no ar durante o seu desenvolvimento proceda da seguinte forma.

Abra um terminal e inicie a execução do lado cliente (os arquivos serão monitorados pelo webpack):

```bash
cd cliente
npm start
```

Abra um segundo terminal e inicie a execução do lado servidor (os arquivos serão monitorados pelo babel):

```bash
cd servidor
npm start
```

A partir de agora altere os arquivos JavaScript como desejar.

### Em produção

Depois que a aplicação está pronta é preciso gerar "uma versão executável". Para isso é preciso gerar uma imagem e depois instanciar e executar um container a partir da imagem gerada.

#### Gerando a imagem

A imagem, aqui chamada de ***ine5646-app-demo*** conterá a versão executável da aplicação. Execute o seguinte comando para gerar a imagem (note que o comando termina com um ponto depois de ine5646-app-demo):

```bash
docker build -t ine5646-app-demo .
```

#### Instanciando o container/Executando a aplicação

Crie ou utilize um arquivo chamado ***.env*** com o seguinte conteúdo:

```bash
SEGUNDOS_AGUARDANDO=2
```

Crie um container para executar a aplicação. Execute o seguinte comando para instanciar o container e colocá-lo no ar.

```bash
docker run -d --rm -p 4000:3000 --env-file .env ine5646-app-demo
```

O primeiro número do parâmetro `-p 4000:3000` representa a porta utilizada pelo container para dar acesso à aplicação que está rodando dentro do container. Assim, para acessar a aplicação, basta digitar `http://localhost:4000` no seu navegador. Naturalmente, a porta `4000` deve estar livre (não estar sendo usada por outra aplicação ou container).

O segundo número do parâmetro `-p 4000:3000` deve ser igual à porta usada pela aplicação, ou seja, o valor da variável `PORTA` no arquivo *.env* ou 3000 caso não esteja definida.

Os dois números do parâmetro `-p 4000:3000` podem ser iguais, como em `-p 3000:3000`.

Naturalmente, pode-se utilizar outras portas (por exemplo, `-p 4500:3100`) e o arquivo **.env** pode estar localizado em qualquer diretório. Neste caso, a aplicação seria acessada via `http://localhost:4500`.

Como neste exemplo o arquivo *.env* só define uma única variável obrigatória uma forma alternativa de instanciar e executar um container seria definir o valor de `SEGUNDOS_AGUARDANDO` diretamente:

```bash
docker run -d -p:4000:3000 -e SEGUNDOS_AGUARDANDO=3000 ine5646-app-demo
```
***ATENÇÃO***: Observe que no container local a aplicação é acessada via `http`. Mas quando ela estiver instalada no Heroku o acesso será via `https` com certificado gerado pelo próprio Heroku.

## Fazendo o deploy da imagem no Heroku

Depois que você conseguiu executar a aplicação no seu computador local a apartir da imagem gerada o próximo passo é disponibilizar a aplicação para acesso de qualquer pessoa via site do Heroku. Esse processo envolve duas etapas: 1) transferência da imagem docker para o Heroku; 2) configuração das variáveis de ambiente no Heroku.

### Transferindo a imagem docker para o Heroku

Execute os seguintes comandos em um terminal:

```bash
heroku container:login
heroku create app-teste-prog-web
docker tag ine5646-app-demo registry.heroku.com/app-teste-prog-web/web
docker push registry.heroku.com/app-teste-prog-web/web
heroku container:release web -a app-teste-prog-web
```

### Definindo as variáveis de ambiente no Heroku
Depois que a imagem foi transferida para o Heroku proceda da seguinte forma:

1. Acesse [https://heroku.com](https://heroku.com) e faça login
2. Clique no nome da aplicação (no exemplo seria good-lake-87254)
3. Clique no menu *Settings*
4. Clique no botão *Reveal Config Vars*
5. Adicione todas as variáveis de ambiente que estão definidas no arquivo `.env`. No caso, apenas a variável PORTA.

A partir de agora a aplicação pode ser acessada a partir de qualquer navegador.

Opcionalmente, é possível alterar o nome da aplicação para um mais fácil de lembrar. No início da página há uma seção chamada *App Information* onde é possível fazer a alteração.
