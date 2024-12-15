#include <chrono>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
  // Lambda functions
  int multiplier = 2;
  auto lambda = [multiplier](int base) {
    std::cout << multiplier * base << std::endl;
  };
  std::thread t1(lambda, 3);
  t1.join();

  // Threads, Mutex and Time Performance
  int shared_resource = 0;

  auto lambda_ref_unsafe = [&shared_resource] {
    for (int i = 1; i <= 3000000; i++) {
      shared_resource = shared_resource + 1;
    }
  };
  auto start_unsafe = std::chrono::high_resolution_clock::now();
  std::thread t_unsafe_1(lambda_ref_unsafe);
  std::thread t_unsafe_2(lambda_ref_unsafe);
  t_unsafe_1.join();
  t_unsafe_2.join();
  auto end_unsafe = std::chrono::high_resolution_clock::now();
  auto duration_unsafe = std::chrono::duration_cast<std::chrono::milliseconds>(
      end_unsafe - start_unsafe);
  std::cout << "Unsafe: shared resource is " << shared_resource << " and took "
            << duration_unsafe.count() << " milliseconds." << std::endl;

  shared_resource = 0;
  std::mutex mutex_shared;
  auto lambda_ref_safe = [&shared_resource, &mutex_shared] {
    for (int i = 1; i <= 3000000; i++) {
      mutex_shared.lock();
      shared_resource = shared_resource + 1;
      mutex_shared.unlock();
    }
  };
  auto start_safe = std::chrono::high_resolution_clock::now();
  std::thread t_safe_1(lambda_ref_safe);
  std::thread t_safe_2(lambda_ref_safe);
  t_safe_1.join();
  t_safe_2.join();
  auto end_safe = std::chrono::high_resolution_clock::now();
  auto duration_safe = std::chrono::duration_cast<std::chrono::milliseconds>(
      end_safe - start_safe);
  std::cout << "Safe: shared resource is " << shared_resource << " and took "
            << duration_safe.count() << " milliseconds." << std::endl;

  // Pointers
  int *p_int;
  void *p_void;
  int v_int = 1;
  p_int = &v_int;
  p_void = p_int;
  std::cout << "value = " << v_int << " dereference pointer = " << *p_int
            << " value of pointer " << p_int << " address of value = " << &v_int
            << " void declared casted pointer =  " << (*(int *)p_void)
            << std::endl;

  // Memory management
  class Shape {
   public:
    Shape(int volume, int mass) : volume_(volume), mass_(mass) {};
    int getMass() { return mass_; };

   private:
    int volume_;
    int mass_;
  };
  Shape shape_1(1, 1);
  Shape shape_2 = Shape(1, 1);
  Shape *shape_p = new Shape(1, 1);
  delete shape_p;


  // Smart pointers
  // - Basically it calls the delete when it goes out of scope
  // Smart pointers: unique_ptr
  std::unique_ptr<Shape> shape_up_1(new Shape(2,2));
}