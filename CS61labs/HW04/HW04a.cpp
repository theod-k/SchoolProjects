//HW04a
//Create the reheapification function
//Check if the binary tree is always less
//Then make it so the binary tree is always complete
#include "bintree.h"
#include <vector>

using namespace std;
using namespace tree_func;

void inOrderMove(binary_tree_node<int> *root_ptr, vector<int>& dataArr){
  if(root_ptr == NULL){
    return;
  }
  else{
    inOrderMove(root_ptr->left(), dataArr);
    dataArr.push_back(root_ptr->data());
    inOrderMove(root_ptr->right(), dataArr);
  }
}

void heapification_min(binary_tree_node<int>* root_ptr, vector<int> dataArr, int* index){
  if(root_ptr == NULL){
    return;
  }
  else{
    root_ptr->data() = dataArr[++*index];
    heapification_min(root_ptr->left(), dataArr, index);
    heapification_min(root_ptr->right(), dataArr, index);
  }
}

int main(){
  binary_tree_node<int>* bt = new binary_tree_node<int>();
  insert(15, bt);
  insert(10, bt);
  insert(13, bt);
  insert(20, bt);
  insert(23, bt);

  print(bt, 3);

  std::vector<int> dataArr;
  int index = -1;

  inOrderMove(bt, dataArr);
  heapification_min(bt, dataArr, &index);

  print(bt, 5);
  return(0);
}
