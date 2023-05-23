#include "product.h"
#include "concreteProduct1.h"
#include "concreteCreator1.h"

Product *ConcreteCreator1::FactoryMethod() const
{
    return new ConcreteProduct1();
}
