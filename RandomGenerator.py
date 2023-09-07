import random
import time
import tracemalloc

from faker import Faker

# def custom_range(start, till, step):
#     while start < till:
#
#         yield start
#         start += step
#
#
# for num in custom_range(1, 10, 2):
#     print(num)


# todo people type class 2 way function 1) create list where we add peoples, 2) create it with generators
class People:
    def __init__(self, ID, name, phoneNumber):
        self.ID = ID
        self.name = name
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.ID}, {self.name}, {self.phoneNumber}"


def add_people_in_list(count):
    people_ = []
    for i in range(count):
        fake = Faker()
        ID = random.randint(1, 999)
        name = fake.first_name()
        phoneNumber = fake.phone_number()
        people_.append(People(ID, name, phoneNumber))
        i += 1
    return people_


def add_people_with_generator(count):
    for i in range(count):
        fake = Faker()
        ID = random.randint(1, 999)
        name = fake.first_name()
        phoneNumber = fake.phone_number()
        yield People(ID, name, phoneNumber)
        i += 1


start_time = time.time()
tracemalloc.start()
peoples = add_people_with_generator(10)
for people in peoples:
    print(people)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for add_people_with_generator: {execution_time:.3f} seconds")
print(f"Used memory for add_people_with_generator: {tracemalloc.get_tracemalloc_memory() * 0.000001:.3f} MB")
tracemalloc.stop()


print()


end_time = time.time()
tracemalloc.start()
peoples_with_list = add_people_in_list(10)
for people in peoples_with_list:
    print(people)
execution_time = end_time - start_time
print(f"Execution time for peoples_with_list: {execution_time:.3f} seconds")
print(f"Used memory for peoples_with_list: {tracemalloc.get_tracemalloc_memory() * 0.000001:.3f} MB")
tracemalloc.stop()
