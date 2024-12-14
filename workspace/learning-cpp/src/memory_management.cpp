#include "memory_management.h"
#include <memory>

struct vector3
{
    float x, y, z;
    vector3(float x, float y, float z) : x(x), y(y), z(z){};
};
using namespace memoryManagementSchool;

MemoryManagementSchool::MemoryManagementSchool()
{
    /*
    Stack and Heap:
        - Both are in RAM
    Stack:
        - Predefined size
        - The addresses in memory is the one next to the other
        - Very fast
        - Each tread has it's own stack
        - It is being freed when it goes out of scope
    Heap:
        - Can grow during process
        - Completely different addresses
        - Smart pointers call delete by themselves
    Important:
        - Always try to allocate memory in the stack
        - Two cases to use heap:
            - When the desired lifetime of the object is more than the scope
            - When we need a lot of memory
    */
    // Example 0
    std::cout << "--------- Example 0 ---------" << std::endl;
    int value = 5; // This is allocated in stack
    int array[5];
    array[0] = 1;
    array[1] = 2;
    array[2] = 3;
    array[3] = 4;
    array[4] = 5;
    std::cout << "size of an int is " << sizeof(int) << " bytes" << std::endl;
    std::cout << "int var at " << &value << " next var will be at " << &value + 1 << std::endl; // pointer arithmetic
    for (auto &el : array)
    {
        std::cout << "array element " << el << " at address " << &el << std::endl;
    }
    std::cout << "elements in stack are stored next to each other " << std::endl;

    int *hvalue = new int; // This is is heap. "new" returns a pointer
    *hvalue = 5;
    int *harray = new int[5];
    vector3 *hvec = new vector3(0, 0, 0);
    for (int i = 0; i < 5; i++)
    {
        harray[i] = i;
    }
    for (int i = 0; i < 5; i++)
    {
        std::cout << "array element " << harray[i] << " at address " << &harray[i] << " next will be " << *harray + i + 1 << std::endl;
    }

    delete hvalue; // You must manually deallocate memory
    delete[] harray;
    delete hvec;

    /*
    "new":
        New keyword calls malloc behind the scenes
        Malloc needs a lot of bookkeeping, asks the operating system and it is time consuming
        It goes through the free list
    Smart Pointers:
        Problems with normal pointers and dynamic memory allocation:
            - memory leaks
            - wild pointers (pointers which have been declared but never initialized to point to any valid object)
            - dangling pointers (pointers that occur when the object is deallocated from the memory without modifying the value if the pointer)
        Python, Java, C# have garbage collectors, C++ not. Smart pointers try to fill this gap
    */

    // Example 1
    std::cout << "--------- Example 1 ---------" << std::endl;
    std::shared_ptr<vector3> vec_ptr(new vector3(0,0,0));
}