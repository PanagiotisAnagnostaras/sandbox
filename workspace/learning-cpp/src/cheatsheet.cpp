#include <chrono>
#include <thread>
#include <mutex>
#include <iostream>
#include <vector>

int main(){
    int multiplier = 2;
    auto lambda = [multiplier](int base){ std::cout<< multiplier * base<< std::endl;};
    std::thread t1(lambda, 3);
    t1.join();

    int shared_resource = 0;

    auto lambda_ref_unsafe = [&shared_resource]{for (int i =1 ; i<=3000000 ; i++){shared_resource = shared_resource + 1;}};
    auto start_unsafe = std::chrono::high_resolution_clock::now();
    std::thread t_unsafe_1(lambda_ref_unsafe);
    std::thread t_unsafe_2(lambda_ref_unsafe);
    t_unsafe_1.join();
    t_unsafe_2.join();
    auto end_unsafe = std::chrono::high_resolution_clock::now();
    auto duration_unsafe = std::chrono::duration_cast<std::chrono::milliseconds>(end_unsafe - start_unsafe);
    std::cout << "Unsafe: shared resource is " << shared_resource  << " and took " << duration_unsafe.count() << " milliseconds." << std::endl;

    shared_resource = 0;
    std::mutex mutex_shared;
    auto lambda_ref_safe = [&shared_resource, &mutex_shared]{for (int i =1 ; i<=3000000 ; i++){mutex_shared.lock();shared_resource = shared_resource + 1;mutex_shared.unlock();}};
    auto start_safe = std::chrono::high_resolution_clock::now();
    std::thread t_safe_1(lambda_ref_safe);
    std::thread t_safe_2(lambda_ref_safe);
    t_safe_1.join();
    t_safe_2.join();
    auto end_safe = std::chrono::high_resolution_clock::now();
    auto duration_safe = std::chrono::duration_cast<std::chrono::milliseconds>(end_safe - start_safe);
    std::cout << "Safe: shared resource is " << shared_resource << " and took " << duration_safe.count() << " milliseconds." << std::endl;
}