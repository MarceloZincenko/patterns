#pragma once
#include "creator.h"
#include "product.h"
#include "concreteProduct2.h"

class ConcreteCreator2 : public Creator {
    public:
        Product *FactoryMethod() const override;
};