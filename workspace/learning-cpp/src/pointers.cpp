#include "pointers.h"
#include <iostream>

namespace pointersSchool
{
    PointersSchool::PointersSchool()
    {
        // Example 1:
        std::cout << "--------- Example 1 ---------" << std::endl;
        int var{0};
        int &ref = var;
        int *ptr = &var;
        std::cout << "ptr = " << ptr << " var = " << var << " dereferencing pointer, *ptr = " << *ptr << " address of var, &var = " << &var << " ref = "
                  << ref << " address of ref, &ref = " << &ref << std::endl;

        // Example 2: differences between Pointers and References
        std::cout << "--------- Example 2 ---------" << std::endl;
        // A pointer can be declared as void, a reference cannot
        void *ptr_void = &var;
        std::cout << " ptr_void = " << ptr_void << std::endl;
        // void &ref_void = var; This is invalid
        // Pointer can be NULL, reference not, they must always have a valid value
        ptr_void = NULL;
        std::cout << " ptr_void = NULL -> ptr_void = " << ptr_void << std::endl;
        // But they cannot be dereferenced: int i = *ptr_void , is invalid

        // Example 3: void pointer
        std::cout << "--------- Example 3 ---------" << std::endl;
        // A void pointer can hold addresses of different types
        int var_int;
        float var_float;
        ptr_void = &var_int;
        std::cout << "Address of var_int kept by ptr_void " << ptr_void << std::endl;
        ptr_void = &var_float;
        std::cout << "Address of var_float kept by ptr_void " << ptr_void << std::endl;
        // A void pointer can not get dereferenced:
        // std::cout << " *ptr_void = " << *ptr_void << std::endl; This is invalid
        // But can be casted to a type and then dereferenced
        std::cout << "*(int*)ptr_void = " << *(int *)ptr_void << " var_int = " << var_int << " var_float = " << var_float << std::endl;

        // Example 4:
        std::cout << "--------- Example 4 ---------" << std::endl;
        // Pass by value, pass by pointer, pass by reference
        std::cout << "Example 4" << std::endl;
        int var_i = 1;
        int *ptr_i = &var_i;
        int &ref_i = var_i;
        std::cout << " var_i = " << var_i << " *ptr_i = " << *ptr_i << " ref_i = " << ref_i << std::endl;
        this->helperFun(var_i, ptr_i, ref_i);
        std::cout << " var_i = " << var_i << " *ptr_i = " << *ptr_i << " ref_i = " << ref_i << std::endl;

        // Example 5:
        std::cout << "--------- Example 5 ---------" << std::endl;
        // NULL vs nullptr
        // this->helperFunForNull(NULL); // this fails because it is ambiguous
        this->helperFunForNull(nullptr); // this is fine
    }

    void PointersSchool::helperFun(int pass_by_val, int *pass_by_ptr, int &pass_by_ref)
    {
        pass_by_val = 2;
        *pass_by_ptr = 2;
        std::cout << " pass_by_val = " << pass_by_val << " *pass_by_ptr = " << *pass_by_ptr << " pass_by_ref = " << pass_by_ref << std::endl;
    }

    void PointersSchool::helperFunForNull(int x){
        std::cout << "from int " << std::endl;
    }
    void PointersSchool::helperFunForNull(int* x){
        std::cout << "from int* " << std::endl;
    }

}
