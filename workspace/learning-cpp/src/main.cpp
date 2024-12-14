#include <iostream>
#include "classes.h"
#include "lambda_functions.h"
#include "pointers.h"
#include "memory_management.h"
#include "threads_school.h"

int main() {
    std::cout << "================================\n 1) Classes \n================================" << std::endl;
    classesSchool::DriverClass class_school;
    std::cout << "================================\n 2) Lambda Functions \n================================" << std::endl;
    lambdaFunctionsSchool::LambdaFunctionsSchool lambda_functions_school;
    std::cout << "================================\n 3) Pointers and Iterators \n================================" << std::endl;
    pointersSchool::PointersSchool pointers_school;
    std::cout << "================================\n 4) Memory \n================================" << std::endl;
    memoryManagementSchool::MemoryManagementSchool memory_management_school;
    std::cout << "================================\n 5) Threads \n================================" << std::endl;
    threadsSchool::ThreadsSchool threadsSchool;
    threadsSchool.driver();
    return 0;
}
