#pragma once
#include "product.h"
#include <string>

class Creator {
    public:
        virtual ~Creator(){};
        virtual Product* FactoryMethod() const = 0;
        std::string SomeOperation() const;
};