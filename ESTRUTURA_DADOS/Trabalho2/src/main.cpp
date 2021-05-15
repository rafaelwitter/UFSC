/*!
 * @file main.cpp
 * @author Rafael Nilson Witt
 * @brief Código do programa principal.
 * @version 1.0
 * @date 2021-05-05
 *
 * @copyright Copyright (c) 2021
 */

#include <fstream>
#include <iostream>
#include <string>

#include "trie.h"

/*!
 * @brief Programa principal, realiza a leitura e processamento dos dicionários
 * e indica o que as palavras da entrada são, se a palavra pertence ao
 * dicionário é impresso a sua posição e o comprimeto da linha em que a palavra
 * está.
 *
 */
int main() {
	using namespace std;
	using namespace structures;
	TrieNode* root = initNode();

	string filename;

	cin >> filename;
	int posProx = 0;

	string line;
	ifstream myfile(filename);
	if (myfile.is_open()) {
		while (getline(myfile, line)) {
			string word;
			int i;
			if (line[0] != '[') {
				posProx += line.length() + 1;
				continue;
			}
			for (i = 1; i < line.length(); i++) {
				if (line[i] == ']')
					break;
				word += line[i];
			}
			word[i] = '\0';
			int length = line.length();
			insert(root, word, posProx, length);
			posProx += line.length() + 1;
		}
		myfile.close();
	} else {
		printf("Nao abriu arquivo\n");
	}

	string word;
	pair<int, int> p;
	while (1) {
		cin >> word;
		if (word.compare("0") == 0) {
			break;
		}
		p = search(root, word);
		if (p.first == 0 && p.second == 0)
			printf("is prefix\n");
		else if (p.first == -1)
			printf("is not prefix\n");
		else
			printf("%d %d\n", p.first, p.second);
	}

	return 0;
}
