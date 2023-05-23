#pragma once
#include "product.h"
#include <string>

class ConcreteProduct1 : public Product {
    public:
        std::string Operation() const override; 
};