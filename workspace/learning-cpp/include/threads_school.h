#include <thread>
#include <iostream>
#include <vector>
#include <mutex>
#include <assert.h>
#include <chrono>
#include <unistd.h>
namespace threadsSchool
{
    class ThreadsSchool
    {
    public:
        ThreadsSchool();
        void driver();

    protected:
    private:
        void myFun1();
        void myFun2();
        static int computeFactorial(const int &m);
        int n_, sum_wo_mutex_, sum_w_mutex_;
        std::mutex sum_guard_;
        int number_to_factorial_{100}, times_to_factorial_{1000};
    };

}