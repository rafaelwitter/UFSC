# Universidade Federal de Santa Catarina
## Trabalho final Estrutura de Dados INE-5609 2020/1
#### Alunos Rafael N. Witt, matrícula nº 18200649

- Descrição do programa.

```
O programa permite adicionar, remover pessoas e filtra-las através de 1 ou mais parametros 
Cada pessoa ao ser instancianda necessita obrigatoriamente dos seguintes argumentos --> Nome, Idade, Nacionalidade e Raça/Cor.
Cada pessoa gerada recebe um ID unico com geramento aleatorio através da bibliote random.
São feitos filtros de busca no arquivo view/main.py através do metodo semelhante ao multilistas, filtrando dados iguais correspondentes ao digitados na tela.
A serialização de objetos através foi feita com a biblioteca Pickle gravada em arquivo em formato de dicionários.
```

- Escolha do modelo da aplicação.
```
O programa foi pensando com base em Multilistas onde um objeto possuem vários atributos em comum. Como descrito na regra de negócios, os objetos são salvos como dicionários, tendo um identificador único chamado de ID da pessoa. E cada pessoa possui uma série de argumentos.
Nome: Escolhido pelo usuário.
Idade: Definida pelo usuário.
Nacionalidade: Escolhida pelo usuário através de um Combox, da biblioteca descrita na regra de negócios/view, são 7 países que fica a escolha do user.
Raça/Cor: Escolhida pelo usuário também através de um Combox, sao definido 3 possibilidades: Branco, Negro ou Pardo.
Visto que os campos (nacionalidade e raça) já são limitados tendem a ter uma filtagrem por vários parametros.
As pesquisas simples são feitas em todos os atributos, nome, idade, nacionalidade e raça, a escolha é feita pelo usuário através de botões do tipo Radio.
As pesquuisas compostas são feitas em combinação de atributos, escolhido pelo usuário através de botões do tipo Radio.
Então pode-se filtrar, pessoas com idade = x, pessoas com idade = X que tem nacionalidade = Y, ou pessoas que moram no pais = X e tem a cor = Y.
Essa filtragem é feita na tela da aplicação, onde é criado um layout para exibição dos atributos selecionados. 
```

- Regra de negócios
   - Modelo
     ```
     Nessa camada existe um arquivo, o modelo da aplicação --> É a base para o controlador de pessoas criar, salvar e remover objetos do tipo Pessoa   
     ```
   - Controlador
     ```
     Nessa camada existem dois arquivos --> 
     Controlador Geral onde é inicializado o sistema através do arquivo executor.py é feita a inicialização da tela principal, com opçoes em botões que permite --> Visualizar todas as pessoas (Aqui pode ser excluido um objeto), Adicionar pessoas, Fazer uma pesquisa através de uma unica chave e Fazer uma pesquisa com multiplas chaves.
     Controlador de Pessoas onde é realizado a serialização, busca e remoção de pessoas.
     ```
   - View 
     ```
     Biblioteca utilizada: PySimpleGui
     Nessa camada existe o arquivo da interface da aplicação, onde possui duas classes, sendo elas:
     TelaPrincipal: responsavel por exibir os botões de listagem, criação e filtagrem de pessoas.
     TelaPesquisa: responsavel por fazer a filtragem dos dados e exibir os objetos correspondetes a pesquisa
     ```
   - DAO
     ```
     Biblioteca utilizada: Pickle
     Camada responsavel pela serialização e recuperação dos objetos. Foi utilizado a biblioteca do python chamda Pickle para fazer a serialização do objeto, pessoa, onde há um identificador único para cada pessoa, gerado aleatoriamente, que serve como chave para o objeto inteiro. 
     Os objetos são salvos no disco através do arquivo contido no diretório DAO/pessoa_id.py, esse arquivo utilizou uma classe abstrata para serialização, onde toda vez que o programa é inicializado é feito uma tentativa de leitura do arquivo pré determinado no arquivo pessoa_id.py, se o arquivo estiver no disco então é chamada a função load, que devolve todos os objetos ja criados para o cache da aplicação e se não houver o arquivo, então é realizado a criação através do comando dump.
     Através do ID é feita a exclusão dos objetos
     ```
     
- Executando a aplicação
```bash
$python3 executor.py
```
