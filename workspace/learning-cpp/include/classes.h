#include <iostream>

namespace classesSchool
{
    class ClassA
    {
        void defaultVisibility(); // private by default

    public:
        ClassA();
        void publicMethod();

    protected:
        void protectedMethod();

    private:
        void privateMethod();
    };

    class DriverClass
    {
    public:
        DriverClass();
    };
}