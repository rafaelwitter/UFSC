#include <string>
#include <vector>

#include <gtest/gtest.h>
#include "binary_tree.h"

namespace {

/**
 * Valores a serem inseridos na árvore de inteiros.
 */
const auto int_values = std::vector<int>{
    30, 20, 50, 10, 40, 80, 60, 70
};

const auto int_in_order = std::vector<int>{
    40, 20, 10, 30, 60, 50, 70, 80
};

/**
 * Teste unitário para árvore binária
 */
class BinaryTreeTest: public testing::Test {
protected:
    /**
     * Lista para teste com inteiros.
     */
    structures::BinaryTree<int> int_list{};
		
    /**
     * Testa a inserção de múltiplos valores em uma lista.
     */
    template <typename T, typename U>
    void multiple_insertion(T& list, const U& values) {
        ASSERT_TRUE(list.empty());
        for (auto& value : values) {
            list.insert(value);
        }
        ASSERT_FALSE(list.empty());
        ASSERT_EQ(values.size(), list.size());
    }

    /**
     * Testa se todos os valores inseridos estão na lista.
     */
    template <typename T, typename U>
    void contains_all(const T& list, const U& values) {
        for (auto& value : values) {
            ASSERT_TRUE(list.contains(value));
        }
    }
};

}  // namespace


/**
 * Testa se a árvore de inteiros permite corretamente a inserção de vários
 * elementos.
 */
TEST_F(BinaryTreeTest, MultipleIntegerInsertion) {
    multiple_insertion(int_list, int_values);
    ASSERT_EQ(4, int_list.height());
}

TEST_F(BinaryTreeTest, Leaves) {
    multiple_insertion(int_list, int_values);
    ASSERT_EQ(3, int_list.leaves());
}

TEST_F(BinaryTreeTest, Limits) {
    multiple_insertion(int_list, int_values);
    structures::ArrayList<int> L = int_list.limits();
    
    ASSERT_EQ(10, L.pop_front());
    ASSERT_EQ(80, L.pop_back());
}

TEST_F(BinaryTreeTest, Filter) {
    multiple_insertion(int_list, int_values);
    int_list.filter(1);
    
    ASSERT_FALSE(int_list.contains(20));
    ASSERT_FALSE(int_list.contains(60));
    ASSERT_FALSE(int_list.contains(80));
    
    ASSERT_TRUE(int_list.contains(30));
    ASSERT_TRUE(int_list.contains(10));
    ASSERT_TRUE(int_list.contains(50));
    ASSERT_TRUE(int_list.contains(40));
    ASSERT_TRUE(int_list.contains(70));
}

TEST_F(BinaryTreeTest, Clone) {
    multiple_insertion(int_list, int_values);
    
    structures::BinaryTree<int> cop = int_list.clone();
        
    int tree_a_size = int_list.size();
    int tree_b_size = cop.size();
    
    ASSERT_EQ(tree_a_size, tree_b_size);

    structures::ArrayList<int> A = int_list.in_order();
    structures::ArrayList<int> B = cop.in_order();
    
    for (int i = 0; i < A.size(); i++)
    	ASSERT_EQ(A.pop(i), B.pop(i));
}

TEST_F(BinaryTreeTest, Balance) {
    multiple_insertion(int_list, int_values);
    structures::BinaryTree<int> cop = int_list.balance();
    
    contains_all(cop, int_values);
    
		structures::ArrayList<int> A = cop.pre_order();
		
		for (int i = 0; i < cop.size(); i++) {
			int value = A.pop(0);
			int expected = int_in_order[i];
			
			//std::cout << "Value is " << value << " and expected is " << expected << std::endl;
			ASSERT_EQ(value, expected);
		}
}

int main(int argc, char* argv[]) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}