/*!
* @file trie.h
* @author Rafael Nilson Witt
* @brief Código da trie.
* @version 1.0
* @date 2021-05-05
*
* @copyright Copyright (c) 2021
*/
#ifndef STRUCTURES_TRIE_H
#define STRUCTURES_TRIE_H

#include <string>
#include <stdio.h>
#include <tuple>
#define ALPHABET_SIZE 26

namespace structures {

/*!
* @brief Árvore de prefixos.
* 
* A árvore de prefixos é uma estrutura de dados eficiente no que diz respeito à
* recuperação de informações. Por isso ela também é conhecida como Trie, de reTRIEval.
* Usando uma Trie bem organizada, pode-se alcançar complexidade de busca O(M), onde M
* representa o tamanho máximo de suas chaves. Ao passo que, uma BST balanceada teria tempo
* proporcional a MlogN, em que N representa o número de chaves na árvore. Essas vantagens
* todavia não são sem seus custos, uma vez que a Trie perde para a BST em espaço ocupado em 
* memória.
*/
struct TrieNode {
	struct TrieNode* children[ALPHABET_SIZE];
	int pos, len;
};

/*!
* @brief Aloca memória para um novo TrieNode.
*
* A posição e o comprimento de cada TrieNode começam zerados. Além disso, todos
* as posições do vetor de nodos filhos começam nulas.
*
* @return struct TrieNode* Ponteiro para o novo TrieNode criado.
*/
struct TrieNode*
initNode();

/*!
* @brief Adiciona uma chave na árvore de prefixos.
*
* @param root Root da árvore.
* @param word Palavra para inserir.
* @param pos Posicao no dicionario da palavra a ser inserida.
* @param len Comprimento da linha no dicionario que possui a palavra a ser inserida.
*/
void insert(struct TrieNode* root, std::string word, int pos, int len);

int findPrefix(struct TrieNode* index);
/*!
* @brief Procura por uma palavra na árvore de prefixos.
*
* @param word Palavra a ser procurada na trie.
* @param root Raíz da árvore.
*
* @return pair<int,int> Par que indica se a palavra pertence ao dicionário, é apenas 
* um prefixo ou que não pertence ao dicionário. Se a palavra pertencer ao dicionário, a
* primeira entrada representa a posição da palavra enquanto a segunda, o comprimeto da linha. 
*/
std::tuple<int, int, int> search(struct TrieNode*, std::string word);

int countWords(std::istream& in) {
    int count = 0;
    for(std::string word; in >> word; ++count) {}
    return count;
}

// implementacao incluida aqui
#include "trie.inc"

}  // namespace structures

#endif
