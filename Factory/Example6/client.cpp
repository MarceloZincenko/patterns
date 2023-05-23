#include "creator.h"
#include <iostream>

void ClientCode(const Creator& creator) {

    std::cout << "Client: I'm not aware of the creator's class, but it still works.\n" << creator.SomeOperation() << std::endl;

}