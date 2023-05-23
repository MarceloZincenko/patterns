#include "product.h"
#include "concreteProduct2.h"
#include "concreteCreator2.h"

Product *ConcreteCreator2::FactoryMethod() const
{
    return new ConcreteProduct2();
}
