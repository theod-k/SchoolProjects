#include <stdlib.h>
#include <iostream>

class Blob{
  public:
    Blob(){
      size = 0;
    }

    //Adds numbers to the last position in the array
    void append(int n);

    //Overloads = to set blob
    void operator=(int n);

    //Overloads the [] operator to get the int in the array
    int& operator[](int i);

    int getSize(){
      return(size);
    }

  private:
    int arr[100];
    int size;
};

//Overload << for printing
std::ostream& operator<<(std::ostream& os, Blob b);

//Overloads the [] operator to get the int in the array
//int operator[](int i) const;

int main(){
  const int kNumElements = 10;
  Blob a;

  //Append some random numbers to the blob.
  for(int i = 0; i < kNumElements; ++i){
    int r = rand()%100;
    a.append(r);
  }

  std::cout << a << std::endl;

  // Double the number at all indices
  for(int i = 0; i < kNumElements; ++i){
    a[i] = 2 * a[i];
  }

  std::cout << a << std::endl;

  // Let's append a few more numbers.
  a.append(111);
  a.append(222);

  std::cout << a << std::endl;

  return(0);
}

void Blob::append(int n){
  arr[size] = n;
  size+=1;
}

int& Blob::operator[](int i){
  return(arr[i]);
}

std::ostream& operator<<(std::ostream& os, Blob b){
  os << "[";
  for(int i = 0; i < b.getSize()-1; i++){
    os << b[i] << " ";
  }
  os << b[b.getSize()-1] << "]";

  return(os);
}
