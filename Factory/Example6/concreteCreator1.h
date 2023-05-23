#pragma once
#include "creator.h"
#include "product.h"
#include "concreteProduct1.h"

class ConcreteCreator1 : public Creator {
    public:
        Product *FactoryMethod() const override;
};