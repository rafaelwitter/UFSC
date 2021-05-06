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
#include <stdio.h>
#include <typeinfo>
#include <tuple>
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
	tuple<int, int, int> p;
	while (1) {
		cin >> word;
		if (word.compare("0") == 0) {
			break;
		}
		
    p = search(root, word);
	  
    if (get<0>(p) == -1) {
      cout << word << " is not prefix\n";
    } else if (filename == "dicionario2.dic") {
      cout << word << " is a prefix of " << get<2>(p) << " words" << endl;
      if(get<1>(p) > 0) {
        cout << word << " is at (" << get<0>(p) << "," << get<1>(p) << ")" << endl;
      }
    } 
    // Comentei isso porque não sei se precisa
    //if (get<0>(p) == 0 && get<0>(p) == 0)
		//    cout << word << " is prefix of " << word.compare(line) << " words" << endl;
		
    else if (filename == "dicionario1.dic"){
		    cout << word << " is prefix of " << get<2>(p) << " words" << endl;
		    cout << word << " is at (" << get<0>(p) << "," << get<1>(p) << ")" << endl; 
		};
	}
	return 0;
}
