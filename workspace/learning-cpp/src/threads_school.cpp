#include "threads_school.h"

using namespace threadsSchool;

ThreadsSchool::ThreadsSchool()
{
    n_ = 10000;
    sum_wo_mutex_ = 0;
    sum_w_mutex_ = 0;
}

void ThreadsSchool::driver()
{
    std::cout << "--------- Example 1 ---------" << std::endl;
    // Example 1
    /*
    - A thread can execute
        a) A Function Pointer
        b) A Lambda Expression
        c) A Function Object
        d) Non-Static Member Function
        e) Static Member Function
    */
    std::thread t1([](int n, int &sum)
                   {for (int i=0;i<n;i++){sum++;} }, n_, std::ref(sum_wo_mutex_)); // arguments to lambda function must be rvalues, refences are not, thus std::ref
    std::thread t2(&ThreadsSchool::myFun1, this);

    std::vector<std::thread> threads_unsafe;

    threads_unsafe.push_back(std::move(t1)); // threads cannot be copied that's why move
    threads_unsafe.push_back(std::move(t2));

    for (auto &t : threads_unsafe)
    {
        t.join();
    }

    std::cout << "1) Sum without mutex = " << sum_wo_mutex_ << " expected = " << (threads_unsafe.size()) * n_ << std::endl;

    std::thread t3([this]()
                   {
        for (int i =0 ; i<this->n_; i++){
            this->sum_guard_.lock();
            this->sum_w_mutex_++;
            this->sum_guard_.unlock();

        } });

    std::thread t4(&ThreadsSchool::myFun2, this);

    std::vector<std::thread> threads_safe;
    threads_safe.push_back(std::move(t3));
    threads_safe.push_back(std::move(t4));

    for (auto &t : threads_safe)
    {
        t.join();
    }

    std::cout << "2) Sum with mutex = " << sum_w_mutex_ << " expected = " << (threads_unsafe.size()) * n_ << std::endl;

    std::cout << "--------- Example 2 ---------" << std::endl;

    int x{5}, factorial_x;

    factorial_x = computeFactorial(x);

    std::cout << "1) Factorial of " << x << " is " << factorial_x << std::endl;

    assert(("Checking factorial function", factorial_x == 120));

    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < times_to_factorial_; i++)
    {
        computeFactorial(number_to_factorial_);
    }

    auto end = std::chrono::high_resolution_clock::now();

    auto duration_serial = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "2) Serial execution took " << duration_serial.count() << std::endl;

    start = std::chrono::high_resolution_clock::now();

    std::vector<std::thread> t_factorial;

    t_factorial.reserve(times_to_factorial_);

    for (int i = 0; i < times_to_factorial_; i++)
    {
        t_factorial.push_back(std::thread([this](const int &m)
                                          { this->computeFactorial(m); }, number_to_factorial_));
    }
    for (auto &t : t_factorial)
    {
        t.join();
    }

    end = std::chrono::high_resolution_clock::now();

    duration_serial = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    std::cout << "3) Threaded execution took " << duration_serial.count() << std::endl;
}

void ThreadsSchool::myFun1()
{
    for (int i = 0; i < n_; i++)
    {
        sum_wo_mutex_++;
    }
}

void ThreadsSchool::myFun2()
{
    for (int i = 0; i < n_; i++)
    {
        sum_guard_.lock();
        sum_w_mutex_++;
        sum_guard_.unlock();
    }
}

int ThreadsSchool::computeFactorial(const int &m)
{
    int result{1};
    for (int n = 0; n < 10000; n++)
    {
        result = 1;
        for (int i = 1; i <= m; i++)
        {
            result *= i;
        }
    }
    return result;
}