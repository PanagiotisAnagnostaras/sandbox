#include "lambda_functions.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace lambdaFunctionsSchool;

LambdaFunctionsSchool::LambdaFunctionsSchool()
{
    std::vector<int> v1{0};
    std::cout << "\naddress of v1 is " << &v1 << "\n"
              << std::endl;
    /*
    Syntax:
        []()->return_type{}
    Where:
        []: capture clause (mandatory)
        (): parameter list (optional)
        -> return_type: return type (optional)
        {}: body (mandatory)
    */

    // Example 0
    std::cout << "--------- Example 0 ---------" << std::endl;
    auto print_vector_ref_1 = [&v1]()
    {
        std::cout << "\n1) Print vector caught by ref\n"
                  << std::endl;
        std::cout << "\naddress of v1 is " << &v1 << "\n"
                  << std::endl;
        std::for_each(v1.begin(), v1.end(), [](const int &element)
                      { std::cout << element << " at address " << &element << std::endl; });
    };

    auto print_vector_value_1 = [v1]()
    {
        std::cout << "\n2) Print vector caught by value\n"
                  << std::endl;
        std::cout << "\naddress of v1 is " << &v1 << "\n"
                  << std::endl;
        std::for_each(v1.begin(), v1.end(), [](const int &element)
                      { std::cout << element << " at address " << &element << std::endl; });
    };

    for (int i = 1; i < 10; i++)
    {
        v1.push_back(i);
    }

    print_vector_ref_1();
    print_vector_value_1();

    auto print_vector_ref_2 = [&v1]()
    {
        std::cout << "\n3) Print vector caught by ref\n"
                  << std::endl;
        std::cout << "\naddress of v1 is " << &v1 << "\n"
                  << std::endl;
        std::for_each(v1.begin(), v1.end(), [](const int &element)
                      { std::cout << element << " at address " << &element << std::endl; });
    };

    auto print_vector_value_2 = [v1]()
    {
        std::cout << "\n4) Print vector caught by value\n"
                  << std::endl;
        std::cout << "\naddress of v1 is " << &v1 << "\n"
                  << std::endl;
        std::for_each(v1.begin(), v1.end(), [](const int &element)
                      { std::cout << element << " at address " << &element << std::endl; });
    };

    print_vector_ref_2();
    print_vector_value_2();
}