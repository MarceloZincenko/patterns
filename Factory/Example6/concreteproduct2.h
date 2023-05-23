#pragma once
#include "product.h"
#include <string>

class ConcreteProduct2 : public Product {
    public:
        std::string Operation() const override; 
};