//!  Copyright [2020] <Autor>

#ifndef STRUCTURES_BINARY_TREE_H
#define STRUCTURES_BINARY_TREE_H

#include "./array_list.h"
#include <climits>

namespace structures {

//! Classe Árvore binária
template<typename T>
class BinaryTree {
 public:
    //! ...
    BinaryTree();
    //! ...
    ~BinaryTree();
    //! ...
    void insert(const T& data);
    //! ...
    void remove(const T& data);
    //! ...
    bool contains(const T& data) const;
    //! ...
    bool empty() const;
    //! ...
    std::size_t size() const;
    //! ...
    ArrayList<T> pre_order() const;
    //! ...
    ArrayList<T> in_order() const;
    //! ...
    ArrayList<T> post_order() const;

    //******************************************************************
    // Prova prática - implementações necessárias:

    // (1) determinação da altura da árvore:
    int height();

    // (2) contagem do número de folhas:
    int leaves();

    // (3) criação de uma lista com o menor (mínimo) e o maior (máximo)
    //     valor da árvore:
    ArrayList<T> limits();

    // (4) criação de uma duplicação, em memória, da árvore:
    BinaryTree<T> clone();

    // (5) remove nós pelo número de seus filhos:
    void filter(int n_child);

    // (6) criação de um nova árvore que tenha todos os valores e a
    //     menor altura possível, ou seja, balanceada com base apenas
    //     no estabelecimento de uma nova ordem de inserção:
    BinaryTree<T> balance();

    //******************************************************************


 private:
    struct Node {
        //! Construtor
        explicit Node(const T& data) :
        data_{data}
        {}

        //! Destrutor
        ~Node() {
            delete left_;
            delete right_;
        }

        T data_;
        Node* left_{nullptr};
        Node* right_{nullptr};

        //! Inserção
        void insert(const T& data) {
            if (data < data_) {
                if (left_ == nullptr) {
                    left_ = new Node(data);
                    if (left_ == nullptr)
                        throw std::out_of_range("Full tree!");
                } else {
                    left_->insert(data);
                }
            } else {
                if (right_ == nullptr) {
                    right_ = new Node(data);
                    if (right_ == nullptr)
                        throw std::out_of_range("Full tree!");
                } else {
                    right_->insert(data);
                }
            }
        }

        //! Remoção
        bool remove(const T& data) {
            bool deleted = false;
            if (data < data_ && left_ != nullptr) {
                left_ = remove(data, left_, deleted);
            } else if (data > data_ && right_ != nullptr) {
                right_ = remove(data, right_, deleted);
            } else {
                if (right_ != nullptr && left_ != nullptr) {
                    Node* temp = right_->minimum();
                    data_ = temp->data_;
                    right_ = remove(data_, right_, deleted);
                } else if (right_ != nullptr) {
                    Node* temp = right_;
                    data_ = temp->data_;
                    right_ = temp->right_;
                    left_ = temp->left_;
                    temp->right_ = temp->left_ = nullptr;
                    delete temp;
                    deleted = true;
                } else if (left_ != nullptr) {
                    Node* temp = left_;
                    data_ = temp->data_;
                    right_ = temp->right_;
                    left_ = temp->left_;
                    temp->right_ = temp->left_ = nullptr;
                    delete temp;
                    deleted = true;
                }
            }
            return deleted;
        }

        //! Contém
        bool contains(const T& data) const {
            if (data < data_)
                return left_ == nullptr? false : left_->contains(data);
            else if (data > data_)
                return right_ == nullptr? false : right_->contains(data);
            else
                return true;
        }

        //! Pré ordem
        void pre_order(ArrayList<T>& v) const {
            v.push_back(data_);
            if (left_ != nullptr)
                left_->pre_order(v);
            if (right_ != nullptr)
                right_->pre_order(v);
        }

        //! Em ordem
        void in_order(ArrayList<T>& v) const {
            if (left_ != nullptr)
                left_->in_order(v);
            v.push_back(data_);
            if (right_ != nullptr)
                right_->in_order(v);
        }

        //! Pós ordem
        void post_order(ArrayList<T>& v) const {
            if (left_ != nullptr)
                left_->post_order(v);
            if (right_ != nullptr)
                right_->post_order(v);
            v.push_back(data_);
        }
        
        //: Altura da árvore
        int height() {
        	int h = 0;
        	if (this != nullptr) {
        		int left = this->left_->height();
        		int right = this->right_->height();
        		
        		h = max_h(left, right) + 1;
        	}
        	return h;
        }
        
        //: Função de máximo genérica
        int max_h(int l, int r) {
        	if (l > r)
        		return l;
        	else
        		return r;
        }
        
        int min_h(int l, int r) {
        	if(l < r)
        		return l;
        	else
        		return r;        	
        }
        
        //: Número de folhas
        int leaves() {
        	int l = 0;
        	
        	if (this != nullptr) {
        		if (this->left_ == nullptr && this->right_ == nullptr) {
        			l += 1;
        		} else {
        			if (this->left_ != nullptr) {
        				l += this->left_->leaves();
        			}
        			
        			if (this->right_ != nullptr) {
        				l += this->right_->leaves();
        			}
        		}
        	}
        	
        	return l;
        }
        
        int min_value() {
        	int v = INT_MAX;
        	
        	if (this != nullptr) {
        		v = min_h(this->data_, v);
        		
        		if (this->left_ != nullptr) {
        			v = min_h(v, this->left_->min_value());
        		}
        		
        		if (this->right_ != nullptr) {
        			v = min_h(v, this->right_->min_value());
        		}
        	}
        	
        	return v;
        }
        
        int max_value() {
        	int v = INT_MIN;
        	
        	if (this != nullptr) {
        		v = max_h(this->data_, v);
        		
        		if (this->left_ != nullptr) {
        			v = max_h(v, this->left_->max_value());
        		}
        		
        		if (this->right_ != nullptr) {
        			v = max_h(v, this->right_->max_value());
        		}
        	}
        	
        	return v;
        }
        
        void filter(int n_child) {
        	if (this != nullptr) {
        		int childs = 0;
        		
        		if (this->left_ != nullptr) {
        			childs++;
        			this->left_->filter(n_child);
        		}
        		
        		if (this->right_ != nullptr) {
        			childs++;
        			this->right_->filter(n_child);
        		}
        		
        		if (childs == n_child)
        			remove(this->data_);
        	}
        }
        
     private:
        //! Complemento da funcão de remoção
        Node* remove(const T& data, Node* arv, bool& deleted) {
            deleted = false;
            if (arv == nullptr)
                return arv;
            if (data < arv->data_) {
                arv->left_ = remove(data, arv->left_, deleted);
                return arv;
            }
            if (data > arv->data_) {
                arv->right_ = remove(data, arv->right_, deleted);
                return arv;
            }
            // doi filhos
            if (arv->right_ != nullptr && arv->left_ != nullptr) {
                Node* temp = arv->right_->minimum();
                arv->data_ = temp->data_;
                arv->right_ = remove(data, arv->right_, deleted);
                return arv;
            }
            // um filho ou folha
            Node* temp = nullptr;
            if (arv->right_ != nullptr)
                temp = arv->right_;
            else
                temp = arv->left_;

            arv->right_ = arv->left_ = nullptr;
            delete arv;
            deleted = true;
            return temp;
        }

        //! Encontrar o menor
        Node* minimum() {
            if (left_ == nullptr)
                return this;
            return left_->minimum();
        }
    };

    Node* root_{nullptr};
    std::size_t size_{0};
};




//******************************************************************
// Prova prática - implementações necessárias:

//! (1) determinação da altura da árvore:
template<typename T>
int BinaryTree<T>::height() {
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    // -1 porque a raiz não é contada como parte da altura da árvore
    return root_->height() - 1;
}

//! (2) contagem do número de folhas:
template<typename T>
int BinaryTree<T>::leaves() {
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    return root_->leaves();
}

//! (3) criação de uma lista com o menor (mínimo) e o maior (máximo)
//!     valor da árvore:
template<typename T>
ArrayList<T> BinaryTree<T>::limits() {
    ArrayList<T> L(2);
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    int m = root_->min_value();
    int mm = root_->max_value();
    
    //std:: cout << "Min value is " << m << std::endl;
    //std::cout << "And max is " << mm << std::endl;
    L.push_front(m);
    L.push_back(mm);
    return L;
}

//! (4) criação de uma duplicação, em memória, da árvore:
template<typename T>
BinaryTree<T> BinaryTree<T>::clone() {
    BinaryTree<T> C;
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    
    ArrayList<T> O = pre_order();
    while (!O.empty()) {
    	int value = O.pop(0);
    	
    	C.insert(value);
    }
    
    return C;
}

//! (5) remove nós pelo número de seus filhos:
template<typename T>
void BinaryTree<T>::filter(int n_child) {
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    
    root_->filter(n_child);
}

//! (6) criação de um nova árvore que tenha todos os valores e a
//!     menor altura possível, ou seja, balanceada com base apenas
//!     no estabelecimento de uma nova ordem de inserção:
template<typename T>
BinaryTree<T> BinaryTree<T>::balance() {
    BinaryTree<T> B;
    /*
        COLOQUE SEU CÓDIGO AQUI ...
    */
    
    ArrayList<T> O = in_order();
    
    int median = O.size()/2 - 1;
    int new_root =  O.pop(median);
    
    B.insert(new_root); 
    
    int index = median - 1;
    while (index >= 0) {
    	int cur_index = index/2;
    	int value = O.pop(cur_index);
    	
    	B.insert(value);
    	index--;
    }
    
    index = median;
    
    while (index >= 0) {
    	int cur_index = index/2;    	
    	int value = O.pop(cur_index);
    	
    	B.insert(value);
    	index--;
    }
   
    return B;
}

//******************************************************************



//! Construtor
template<typename T>
BinaryTree<T>::BinaryTree()
{}

//! Destrutor
template<typename T>
BinaryTree<T>::~BinaryTree() {
    delete root_;
}

//! Inserção
template<typename T>
void BinaryTree<T>::insert(const T& data) {
    if (empty()) {
        root_ = new Node(data);
        if (root_ == nullptr)
            throw std::out_of_range("FUll tree!");
    } else {
            root_->insert(data);
    }
    ++size_;
}

// Remoção
template<typename T>
void BinaryTree<T>::remove(const T& data) {
    if (empty())
        throw std::out_of_range("Empty tree");

    if (size() != 1u) {
        if (root_->remove(data))
            --size_;
    } else {
        if (root_->data_ == data) {
            delete root_;
            root_ = nullptr;
            --size_;
        }
    }
}

//! Contém
template<typename T>
bool BinaryTree<T>::contains(const T& data) const {
    if (empty())
        return false;
    return root_->contains(data);
}

//! Vazio
template<typename T>
bool BinaryTree<T>::empty() const {
    return size() == 0;
}

//! Tamanho
template<typename T>
std::size_t BinaryTree<T>::size() const {
    return size_;
}

//! Pré ordem
template<typename T>
ArrayList<T> BinaryTree<T>::pre_order() const {
    ArrayList<T> v{size_};
    if (!empty())
        root_->pre_order(v);
    return v;
}

//! Em ordem
template<typename T>
ArrayList<T> BinaryTree<T>::in_order() const {
    ArrayList<T> v{size_};
    if (!empty())
        root_->in_order(v);
    return v;
}

//! Pós ordem
template<typename T>
ArrayList<T> BinaryTree<T>::post_order() const {
    ArrayList<T> v{size_};
    if (!empty())
        root_->post_order(v);
    return v;
}

}  // namespace structures

#endif
