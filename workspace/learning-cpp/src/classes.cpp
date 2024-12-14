#include "classes.h"

namespace classesSchool
{
    ClassA::ClassA()
    {
        std::cout << "1) constructor object created" << std::endl;
    }

    void ClassA::defaultVisibility()
    {
        std::cout << "default visibility is private" << std::endl;
    }

    void ClassA::publicMethod()
    {
        std::cout << "2) public method" << std::endl;
    }

    void ClassA::protectedMethod()
    {
        std::cout << "protected method" << std::endl;
    }

    void ClassA::privateMethod()
    {
        std::cout << "private method" << std::endl;
    }

    DriverClass::DriverClass(){
        ClassA class_a;
        class_a.publicMethod(); // only public visible.
        
    }

};