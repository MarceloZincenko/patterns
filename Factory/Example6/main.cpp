#include "creator.h"
#include "concretecreator1.h"
#include "concretecreator2.h"
#include "client.h"
#include <iostream>

int main() {
  std::cout << "App: Launched with the ConcreteCreator1.\n";
  Creator *creator = new ConcreteCreator1();
  ClientCode(*creator);
  std::cout << std::endl;

  std::cout << "App: Launched with the ConcreteCreator2.\n";
  Creator* creator2 = new ConcreteCreator2();
  ClientCode(*creator2);

  delete creator;
  delete creator2;
  return 0;
}