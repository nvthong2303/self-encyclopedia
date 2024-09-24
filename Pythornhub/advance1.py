# # #### Map function
# # numbers = [1, 2, 3, 4, 5]
# # squared = map(lambda x: x**2, numbers)
# # print(type(squared))
# # # <class 'map' >
# # print(type(numbers))
# # # <class 'list' >
# # print(list(squared))
# # # [1, 4, 9, 16, 25]
# # print(type(list(squared)))
# # # <class 'list' >
# a = ["thong", "nguyen", "van", "cmc", "vietnam", "hust"]
# iterator_a = iter(a)

# # try:
# #     while True:
# #         print(next(iterator_a))
# # except StopIteration:
# #     print("End of list")
# #     pass

# numbers = [1, 2, 3, 4, 5]  # List là một iterable
# for num in numbers:
#     print(num)

# numbers = [1, 2, 3]
# iterator = iter(numbers)  # Chuyển iterable (list) thành iterator

# print(next(iterator))  # In ra 1
# print(next(iterator))  # In ra 2
# print(next(iterator))  # In ra 3
# print(next(iterator))  # In ra 4
# print(next(iterator))  # In ra 5
# print(next(iterator))  # In ra 6


# class Counter:
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1

# if __name__ == "__main__":
#     a, b = 2, 5
#     c1 = Counter(a, b)
#     c2 = Counter(a, b)

#     print("Print the range without iter()")

#     for i in c1:
#         print("Eating more Pizzas, counting ", i, end="\n")

#     print("\nPrint the range using iter()\n")

#     # Way 2- using iter()
#     obj = iter(c2)
#     try:
#         while True:  # Print till error raised
#             print("Eating more Pizzas, counting ", next(obj))
#     except:
#         # when StopIteration raised, Print custom message
#         print("\nDead on overfood, GAME OVER")


# intertools
## compress
from itertools import compress, cycle, count, repeat, product, permutations, combinations, combinations_with_replacement, accumulate, chain, islice, zip_longest

# dates = [
#     "2020-01-01",
#     "2020-02-04",
#     "2020-02-01",
#     "2020-01-24",
#     "2020-01-08",
#     "2020-02-10",
#     "2020-02-15",
#     "2020-02-11",
# ]
# counts = [1, 4, 3, 8, 0, 7, 9, 2]

# bools = [n > 3 for n in counts]
# print(bools)
# print(list(compress(dates, bools)))  


## cycle
# cyc = cycle([1, 2, 3])
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))
# print(next(cyc))


## count
counter = count(10, 2)
# print(next(counter))  # 10
# print(next(counter))  # 12
# print(next(counter))  # 14
# print(next(counter))  # 10
# print(next(counter))  # 12
# print(next(counter))  # 14

# lambda function
# exception handling
# decorators
# collections
# generators
# magic methods
# threading
# regular expression

