# def getFinalString(s):
#     str = "AWS"
#     while str in s:
#         s = s.replace(str, "")
#     return -1 if s == "" else s
# print(getFinalString("AAWSWS"))

# import math
# def military_to_standard(hours, mins):
# if hours > 12:
# hours -= 12
# return str(hours) + ":" + str(mins).zfill(2) + " PM"
# elif hours == 12:
# return str(hours) + ":" + str(mins).zfill(2) + " PM"
# elif hours == 0:
# hours += 12
# return str(hours) + ":" + str(mins).zfill(2) + " AM"
# else:
# return str(hours) + ":" + str(mins).zfill(2) + " AM"
# print(military_to_standard(0, 0))

# def test(func, arg): # func = multiply, arg = 2
#    return func(func(arg)) # multiply(multiply(2)) = 16
# def multiply(x): # x = 2
#    return x * x # 2 * 2 = 4
# print(test(multiply, 2)) # test(multiply, 2) = 16

# def my_func(f, arg):
# 	return f(arg)
# print(my_func(lambda x: 2*x*x, 5))

# def factorial(x):
# if x == 1:
# return 1
# else:
# return x * factorial(x-1)
# print(factorial(5))

# def calc(list):
# if len(list)==0:
# return 0
# else:
# return list[0]**2 + calc(list[1:])
# list = [1, 3, 4, 2, 5]
# x = calc(list)
# print(x)
# from itertools import product
# a = {1,2}
# print(len(list(product(range(3),a))))

# def power(x, y):
# if y == 0:
# return 1
# else:
# return x * power(x, y-1)
# print(power(2, 3))

# num = int(input())
# def fib(n: int) -> int:
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fib(n-1) + fib(n-2)
# print(fib(num))

# num = int(input())
# def fibonacci(n):
# if n == 0:
# return []
# elif n == 1:
# return [0]
# elif n == 2:
# return [0,1]
# else:
# sequence = fibonacci(n-1)
# sequence.append(sequence[-1]+sequence[-2])
# return sequence
# fib_sequence = fibonacci(num)
# for number in fib_sequence:
# print(number)
# def spiralTraverse(array):
# traversedArray = []
# while array: # while array is not empty
# traversedArray += array.pop(0) # pop the first row and add it to traversedArray
# .pop(0) removes the first element of the array and returns ite
# array = list(zip(*array))[::-1] #  rotate the remaining array clockwise
# return traversedArray
# scores = [12, 20, 10, 24]
# def breakingRecords(scores):
# minMax = [0,0]
# minScore, maxScore = scores[0], scores[0]
# for i in range(len(scores)):
# if scores[i] < minScore:
# minScore = scores[i]
# minMax[1] += 1
# elif scores[i] > maxScore:
# maxScore = scores[i]
# minMax[0] += 1
# return minMax
# print(breakingRecords(scores))
# Find individual lengths of each subarray in a 2D array
# def findLengths(array):
# lengths = []
# for i in range(len(array)):
# lengths.append(len(array[i]))
# return lengths
# print(findLengths([[1,2,3],[4,5],[6,7,8,9]]))
# Find the sum of each subarray in a 2D array
# def findSums(array):
# sums = []
# for i in range(len(array)):
# sums.append(sum(array[i]))
# return sums
# print(findSums([[1,2,3],[4,5],[6,7,8,9]]))
# Find the sum of each subarray in a 2D array and return the sum of the sums
# def findSumOfSums(array):
# sums = []
# for i in range(len(array)):
# sums.append(sum(array[i]))
# return sum(sums)
# print(findSumOfSums([[1,2,3],[4,5],[6,7,8,9]]))

# data = [
#   [23, 11, 5, 14],
#   [8, 32, 20, 5]
# ]
# color = input()
# sums = []
# def findSumOfSums(data):
#   for i in range(len(data)):
#   sums.append(sum(data[i]))
#   return sum(sums)
# total = findSumOfSums(data)
# if color == "brown":
# print(int((data[0][0] + data[1][0])*100/total))
# elif color == "blue":
# print(int((data[0][1]+data[1][1])*100/total))
# elif color == "green":
# print(int((data[0][2]+data[1][2])*100/total))
# else:
# print(int((data[0][3]+data[1][3])*100/total))

# x=[1,2,3,4,5,6]
# x.append(8)
# x.insert(0, 0)
# x.remove(2)
# print(len(x))

# prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
# average = int(sum(prices) / len(prices))
# count = 0
# for i in range(len(prices)):
# if prices[i] > average:
# count += 1
# print(count)

# insects = [n*2**i for i in range(12)]

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))

# text = input()
# print((sum(len(word) for word in text.split()))/len(text.split()))

# contacts = { "David": ["123-321-88", "david@test.com"], "James": ["241-879-093", "james@test.com"], "Bob": ["987-004-322", "bob@test.com"], "Amy": ["340-999-213", "a@test.com"] }
# name = input()
# if name in contacts:
# print(contacts[name][1])
# else:
# print("Not found")
# name = input()
# if name in contacts:
# print(contacts[name][1])
# else:
# print("Not found")

# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))

# distance = list(range(len(points)))
# z = 0
# for (x, y) in points:
# distance[z] = (x**2 + y**2)**0.5
# z += 1
# print(min(distance))

# list1 = s1.split()
# list2 = s2.split()
# print(len(set(list1) & set(list2)))
#
# n = p.head
# while n != None:
# print(n.title)
# n = n.next
# a = 0
# for i in range(len(x.adj)):
# if i+1==n:
# for j in x.adj[i]:
# if j==1:
# a+=1
# matrix = [[1,2,3,4],[5,6,7,8]]
# print(len(matrix[0]))

# def standard_to_military(hours, time_of_day):
# if time_of_day == "AM":
# if hours == 12:
# return 0
# else:
# return hours
# else:
# if hours == 12:
# return 12
# else:
# return hours + 12

# def rotate_right(num_list):
#     return num_list[-1:] + num_list[:-1]
# print(rotate_right([1,2,3,4,5]))

# def rotate_element(num_list, k):
# if len(num_list) == 0:
# return num_list
# if k > 0:
# for i in range(k):
# last_value = num_list[-1]
# num_list.insert(0, last_value)
# num_list.pop()
# return num_list
# print(rotate_element([1,2,3,4,5], 3))

# def majorityElement(array):
# current_max = 0
# if range(len(array)):
# return array[0]
# for i in range(len(array)):
# temp = array.count(array[i])
# if temp > current_max:
# current_max = temp
# return current_max

# class BST:
# def __init__(self, value):
# self.value = value
# self.left = None
# self.right = None
# def validateBst(tree):
# return validateBstHelper(tree, float("-inf"), float("inf")) # -inf and inf are the smallest and largest numbers possible
# def validateBstHelper(tree, minValue, maxValue):
# if tree is None: # if tree is empty
# return True
# if tree.value < minValue or tree.value >= maxValue: # if tree value is less than min or greater than or equal to max
# return False
# leftIsValid = validateBstHelper(tree.left, minValue, tree.value) # check left side of tree
# return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue) # check right side of tree

# def mystery(s):
# prt1 = 0
# prt2 = 3
# lst = []
# while prt2 <= len(s):
# sub = s[prt1:prt2]
# if sub not in lst:
# lst.append(sub)
# prt1 += 1
# prt2 += 1
# return lst
# print(mystery("ababababa"))

# def mystery(nums):
# if len(nums) == 0:
# return 0
# i = 0
# for j in range(1, len(nums)):
# if nums[j] != nums[i]:
# i += 1
# nums[i] = nums[j]
# return i + 1
# print(mystery([1,1,2]))
# def first_palindrome(words):
# for string in range(len(words)):
# if words[string] == words[string][::-1]:
# return  words[string]
# return ""
# print(first_palindrome(["def", "ghi"]))

# def subarray_sum(nums, target):
# n = len(nums)
# if n < 3:
# return []
# window_sum = sum(nums[:3])
# if window_sum == target:
# return nums[:3]
# for i in range(3, n):
# window_sum += nums[i] - nums[i - 3]
# if window_sum == target:
# return nums[i - 2:i + 1]
# return []
# print(subarray_sum([0, 5, -7, 1, -2, 7, 6, 1, 4, 1, 10], 15))
# import random
# s = "aba"
# s.replace(random(0,len(s)),'')
# print(s)

# import random
# def palindrome_del(s):
# s = ''.join([s[i] for i in range(len(s)) if i != random.randint(0, len(s) - 1)])
# return s == s[::-1]
# print(palindrome_del("aba"))

# import math

# def approximate(x, dx):
#   """Approximates the quantity of x ^ 1/3."""
#   dy = (1/3) * x ** (-2/3) * dx
#   return x ** (1/3) + dy
#
# print(approximate(107.5, 0.1))

# import math
# print(math.floor(107.5))

# d = { "a": 'b', "b": 'c', "c": 'a' }
# for x, y  in d.items():
#     print(x, y, d[x], d[y])
# print(d.items())
# inventory = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# inventory = {'bananas': 5, 'apples': 3, 'cherries': 100}
# def maximum_count(inventory):
# max = 0
# for x in inventory:
# if inventory[x] > max:
# max = inventory[x]
# elif inventory[x] == max:
# max = inventory[x]
# return inventory.keys(max)
# print(maximum_count(inventory))

# inventory = {"banana": 5, "apple": 3, "orange": 10, "bacon": 1, "sausages": 13}
# def low_inventory(inventory, threshold):
# value_list = []
# for key, value in inventory.items():
# if value <= threshold:
# value_list.append(key)
# return value_list
# print(low_inventory(inventory, 3))

# def category_total(inventory, categories, category):
# total = 0
# for key, value in inventory.items():
# if key in categories[category]:
# total += value
# return total

# def most_common_first_letter(word_list):
# first_letters = [word[0] for word in word_list]
# return max(set(first_letters), key=first_letters.count)
# print(most_common_first_letter(["cat","bat", "rat", "bar", "car", "can"]))

# opened = ["[","{","("]
# closed = ["]", "}",")"]
# def balanced_symbols(s):
#   stack = []
#   for i in s:
# if i in opened:
#   stack.append(i)
# elif i in closed:
#   pos = closed.index(i)
#   if ((len(stack) > 0) and (opened[pos] == stack[len(stack) -1])):
# stack.pop()
#   else:
# return False
#   if len(stack) == 0:
# return True
#   else:
# return False
# s = "{[]{()}}"
# print(balanced_symbols(s))
# O(n) Time

# def unique(my_list):
# my_dict = {}
# for item in my_list:
# if item in my_dict:
# my_dict[item] += 1
# else:
# my_dict[item] = 1
# return my_dict.keys()
# print(unique([1,2,3,3,2,1,0]))

# k = 14
# costs = [2, 4, 1, 8, 6]
# def maximumPoints(k, costs):
# n = len(costs)
# max_points = 0
# total_cost = 0
# skipped = False
# skip_index = -1
# for i in range(n):
# total_cost += costs[i]
# while total_cost > k and not skipped:
# total_cost -= costs[skip_index + 1]
# skip_index += 1
# skipped = True
# max_points = max(max_points, i - skip_index)
# return max_points
# print(maximumPoints(k, costs))

# def find_anagrams(word_list):
# my_dict = {}
# for word in word_list:
# srt_letters = ''.join(sorted(word))
# if srt_letters in my_dict:
# my_dict[srt_letters].append(word)
# else:
# my_dict[srt_letters] = [word]
# for key, words in my_dict.items():
# if len(words) >= 2:
# return [words[0], words[1]]
# return []
# print(find_anagrams(["cat", "dog", "tac", "god", "act"]))
# def consecutive(list):
#   l, r = 0, 1
#   count = 0
#   while l < r:
# if list[l] == list[r]:
#   l += 1
#   r += 1
#   count += 1
# elif list[l] != list[r]:
# l += 1
# r += 1
# return count
# print(consecutive([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))

# def total_inventory(dict1,dict2):
# total = 0
# for key in dict1: # for each key in dict1
# total += dict1[key] # add the value of the key to total
# for key in dict2: # for each key in dict2
# total += dict2[key] # add the value of the key to total
# return total
# print(total_inventory({'pencil': 10, 'pen': 8, 'paper': 7}, {'pencil': 11, 'pen': 12, 'paper': 13}))

# def translate(list,dic):
# translatedList = []
# for i in list: # for each element in list
# translatedList.append(dic[i]) # append the value of the element to translatedList
# return translatedList
# print(translate(['cat', 'dog', 'walrus'], {0: 'dog', 1: 'walrus', 2: 'cat'}))
# def roman_nums(input):
# roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# total = 0
# for i in range(len(input)):
# value = roman[input[i]] # value = roman['I'] = 1
# if i+1 < len(input) and roman[input[i+1]] > value: # if next value is > current value
# total -= value
# else: # if the next value is not greater than the current value
# total += value
# return total
# print(roman_nums('III'))
# print(roman_nums('LVIII'))
# print(roman_nums('MMXXIII'))

# capitals = {
# "France": "Paris",
# "Netherlands": "Amsterdam",
# "Germany": "Berlin",
# "Switzerland": "Bern",
# }
# Printing just the keys
# for country in capitals.keys():
# print(country)
#  Printing just the values
# for capital in capitals.values():
# print(capital)
# Printing both keys and values
# for country, capital in capitals.items():
# print(country, capital)
# Printing the keys and values in a formatted string
# for country, capital in capitals.items():
# print("The capital of " + country + " is " + capital + ".")

# words = ["apple", "apple", "banana", "apple", "orange", "banana", "pear", "banana"]
# def word_freq(words):
# output = {}
# for word in words:
# if not(word in output):
# output[word] = 1
# else:
# output[word] += 1
# return output
# print(word_freq(words))

# This is from the Leetcode problem 34. Find First and Last Position of Element in Sorted Array
# class Solution:
# def searchRange(self, nums: List[int], target: int) -> List[int]:
# low, high = 0, len(nums)-1
# while low <= high:
# mid = (low + high)//2
# if nums[mid] == target:
# return [self.find_left(nums, target, low, mid), self.find_right(nums, target, mid, high)]
# elif nums[mid] < target:
# low = mid + 1
# else:
# high = mid - 1
# return [-1, -1]
# def find_left(self, nums, target, low, high):
# while low < high:
# mid = (low + high)//2
# if nums[mid] == target:
# high = mid
# else:
# low = mid + 1
# return low
# def find_right(self, nums, target, low, high):
# while low < high:
# mid = (low + high)//2 + 1
# if nums[mid] == target:
# low = mid
# else:
# high = mid - 1
# return low
# Itterative
# def factorial(n):
# result = 1
# for i in range(n, 1, -1):
# result *= i
# return result
# print(factorial(0))
# print(factorial(1))
# print(factorial(3))
# print(factorial(5))

# Recursive
# def factorial(n):
# if n < 2:
# return 1
# else:
# return n * factorial(n-1) # multiply n by the factorial of n-1, because n! = n * (n-1)!
# Because its recursive, it will keep calling itself until n == 0 or n == 1
# print(factorial(0))
# print(factorial(1))
# print(factorial(3))
# print(factorial(5))

# def are_anagrams(word1, word2):
#   firstWord = set()
#   secondWord = set()

#   for word in word1:
#     firstWord.add(word)
#   for word in word2:
#     secondWord.add(word)

#   return firstWord == secondWord

# print(are_anagrams("dad","add")) # True
# print(are_anagrams("boy","girl")) # False
# print(are_anagrams("lady","bird")) # False
# print(are_anagrams("not","ton")) # True

# def palindrome(s):
#   return s == s[::-1]
# print(palindrome("dad"), ": This is the function palindrome")

# def palindrome_r(s):
#   if len(s) <= 1:
#     return True
#   if s[0] == s[-1]:
#     return palindrome_r(s[1:-1])
#   else:
#     return False
# print(palindrome_r("dad"), ": This is the function palindrome_r")

# def double_sum(nums):
# current_sum = 0
# for i in range(0, len(nums)):
# current_sum += 2 * nums[i]
# return current_sum
# print(double_sum([4, 2, 10, 5])) # 42, because (4*2) + (2*2) + (10*2) + (5*2) = 42

# a = 12
# b = 8
# while a > b:
# a -= 2
# print(a, b)
# b -= 1
# print(a - 1, b)

# def abracadabra(head):
# list = head
# while list:
# if(list.next == None):
# break
# if (list.val == list.next.val):
# list.next = list.next.next
# else:
# list = list.next
# return head
# print(abracadabra([1,2,2,3,4,5,5, 6, 7]))

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(A[1][2])

# def maximumOccurringCharacter(text):
# result = {}
# for i in text:
# if i in result:
# result[i] += 1
# else:
# result[i] = 1
# return max(result, key=result.get)
# print(maximumOccurringCharacter("abbbaacc"))

# def maxDifference(px):
# l, r = 0, 1
# max_diff = px[r] - px[l]
# while r < len(px):
# if px[l] > px[r]:
# l = r
# else:
# max_diff = max(max_diff, px[r] - px[l])
# r += 1
# return max_diff
# print(maxDifference([7, 1, 2, 5]))

# def maxSubsetSumNoAdjacent(array):
#     filtered = []
#     if not array:
#         return 0
#     elif len(array) == 2:
#         return max(array)
#     for i in range(0, len(array)):
#         if not(i in filtered):
#             filtered.append(array[i])

# def maxSubsetSumNoAdjacent(array):
# if not array:
# return 0
# elif len(array) == 1:
# return array[0]
# maxSums = array[:]
# maxSums[1] = max(array[0], array[1])
# for i in range(2, len(array)):
# maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
# return maxSums[-1]
# print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])) # 330


# def maxSubArray(nums):
# maxSum = nums[0]
# currSum = 0
# for i in range(0, len(nums)):
# if currSum < 0:
# currSum = 0
# currSum += nums[i]
# maxSum = max(maxSum, currSum)
# return maxSum
# print(maxSubArray([1,2,3,4,5,6,7,8,9,10])) # 55

# import math
# print(math.ceil(1905/100))

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(array))

# def solution(inputArray):
# result = []
# for i in range(len(inputArray) - 1):
# result.append(inputArray[i] * inputArray[i + 1])
# return max(result)
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# def solution(statues):
# count = 0
# statues.sort()
# for i in range(len(statues) - 1):
# if statues[i] + 1 != statues[i + 1]:
# count += statues[i + 1] - statues[i] - 1
# return count
# print(solution([6, 2, 3, 8])) # 3

# def solution(sequence):
# dropped = False
# last = prev = min(sequence) - 1
# for elm in sequence:
# if elm <= last:
# if dropped:
# return False
# else:
# dropped = True
# if elm <= prev:
# prev = last
# elif elm >= prev:
# prev = last = elm
# else:
# prev, last = last, elm
# return True

# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
# def solution(matrix):
# rows = len(matrix)
# cols = len(matrix[0])
# result = 0
# for col in range(cols):
# for row in range(rows):
# if matrix[row][col] == 0:
# continue
# else:
# result += matrix[row][col]
# return result
# print(solution([[0, 1, 1, 2],
#   [0, 5, 0, 0],
#   [2, 0, 3, 3]]))
# def powerset(array):
# """
# Generates the powerset of a given array.
# The powerset of a set is the set of all possible subsets, including the empty subset and the set itself.
# Parameters:
# array (list): The input list for which the powerset needs to be generated.
# Returns:
# list: A list of lists representing the powerset of the input array.
# """
# subsets = [[]]  # Initialize the powerset with the empty subset
# for ele in array: # For each element in the input array
# for i in range(len(subsets)): # For each subset in the powerset
# currentSubset = subsets[i] # Get the current subset
# subsets.append(currentSubset + [ele])  # Add a new subset with the current element
# return subsets
# print(powerset([1, 2, 3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# a, b, c, d, *e, f, g = range(20) # *e = 3,4,5,6,7,8,9,10,11,12,13,14
# print(len(e)) # 14

# for i in range(10): # 0,1,2,3,4,5,6,7,8,9
# if i > 5:
# print(i)
# break
# else:
# print("7")

# try:
# print(1)
# print(1+ "1" == 2)
# print(2)
# except TypeError:
# print(3)
# else:
# print(4)

# for i in range(10):
#     try:
#         if 10 / i == 2.0:
#             break
#     except ZeroDivisionError:
#         print(1)
#     else:
#         print(2)

# join() # join() is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

# import pandas as pd

# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
#                     'value1': [1, 2, 3, 4]})
# print(df1)
# df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
#                     'value2': [5, 6, 7, 8]})
# print(df2)
# merged_df = pd.merge(df1, df2, on='key', how='outer')

# print(merged_df)


# print(merged_df)

# from collections import defaultdict
# import heapq
# from typing import List

# class FoodRatings:
#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.cuisine_to_heap = defaultdict(list)
#         self.food_to_cuisine = {}
#         self.food_to_rating = defaultdict(int)
#         for i in range(len(foods)):
#             self.food_to_cuisine[foods[i]] = cuisines[i]
#             heapq.heappush(self.cuisine_to_heap[cuisines[i]], (-ratings[i], foods[i]))
#             self.food_to_rating[foods[i]] = -ratings[i]

#     def changeRating(self, food: str, newRating: int) -> None:
#         cuisine = self.food_to_cuisine[food]
#         heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
#         self.food_to_rating[food] = -newRating

#     def highestRated(self, cuisine: str) -> str:
#         smallest_lexico = None
#         while len(self.cuisine_to_heap[cuisine]) > 0:
#             curr = self.cuisine_to_heap[cuisine][0]
#             if curr[0] != self.food_to_rating[curr[1]]:
#                 heapq.heappop(self.cuisine_to_heap[cuisine])
#                 continue
#             smallest_lexico = curr[1]
#             break
#         return smallest_lexico

# print()

# var1 = "THIS"
# length = len(var1)
# for i in range(length):
#     print(var1[i], end=" ")

# var2 = set(var1)
# print(var2)


# st = time.time()

# nums = [0, 1, 0, 3, 12]

# nums = [0, 1, 0, 3, 12]

# def moveZeroes(nums: List[int]) -> None:
#     left, right = 0, len(nums) - 1
#     while left < right:
#         if nums[left] == 0:
#             nums.pop(left)
#             nums.append(0)
#             right -= 1
#         else:
#             left += 1
#     print(nums)
# moveZeroes(nums)
# et = time.time()
# print(et - st, "seconds\n")


# st = time.time()

# nums = [0, 1, 0, 3, 12]

# def moveZeroes1(nums: List[int]) -> None:
#     non_zero = 0

#     for current in range(len(nums)):
#         if nums[current] != 0:
#             nums[non_zero], nums[current] = nums[current], nums[non_zero]
#             non_zero += 1
#     print(nums)
# moveZeroes1(nums)
# et = time.time()
# print(et - st, "seconds")

# from typing import List
# import time

# st = time.time()
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3


# def findMaxAverage(nums: List[int], k: int) -> float:
#     currSum = maxSum = sum(nums[:k])
#     for i in range(k, len(nums)):
#         currSum += nums[i] - nums[i - k]
#         maxSum = max(maxSum, currSum)
#     return maxSum / k


# result = findMaxAverage(nums, k)
# print(result)
# et = time.time()
# print(et - st, "seconds")

# from typing import List
# import collections
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         res = collections.Counter(nums)
#         if len(nums)== 1:
#             return nums[0]
#         return max(res, key=res.get)
# solution = Solution()
# print(solution.majorityElement([3,2,3])) # 3
# stack = []

# while True:
#     # Read a character
#     char = input("Enter a character (or press Enter to finish): ")

#     # If the character is '(', push it on the stack
#     if char == "(":
#         stack.append(char)
#     # If the character is ')' and the stack is not empty, pop from the stack
#     elif char == ")" and stack:
#         stack.pop()
#     # If the character is ')' and the stack is empty, print "unbalanced" and exit
#     elif char == ")" and not stack:
#         print("unbalanced")
#         break

# If the stack is empty, print "balanced"; otherwise, print "unbalanced"
# if not stack:
#     print("balanced")
# else:
#     print("unbalanced")


# class CamelCase:
#     def __init__(self, input: str):
#         self.input = input

#     def encode(self) -> str:
#         words = self.input.split()
#         for i in range(len(words)):
#             words[i] = words[i][0].upper() + words[i][1:].lower()
#         words[0] = words[0].lower()
#         return "".join(words)

#     def decode(self) -> str:
#         res = []
#         for i in range(len(self.input)):
#             if self.input[i].isupper():
#                 res.append(" ")
#             res.append(self.input[i])
#         return "".join(res).strip().casefold().capitalize()
# camel_instance = CamelCase("The quick brown fox jumps over the lazy dog")
# camel_instance2 = CamelCase("theQuickBrownFoxJumpsOverTheLazyDog")
# print(camel_instance.encode())
# print(camel_instance2.decode())


# def drawTree(height: int) -> str:
#     result = ""
#     for i in range(height):
#         result += " " * (height - i - 1) + "*" * (2 * i + 1) + "\n"
#     return result
# print(drawTree(5))


# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         count = {0: 1}
#         cur_sum, total_sub = 0, 0
#         for num in nums:
#             cur_sum += num
#             if cur_sum - goal in count:
#                 total_sub += count[cur_sum - goal]
#             count[cur_sum] = count.get(cur_sum, 0) + 1
#         return total_sub


# def two_out_of3(a: bool, b: bool, c: bool) -> bool:
#     res = [int(a), int(b), int(c)]
#     return True if sum(res) == 2 else False

# print(two_out_of3(True, True, True)) # True

# def next_palindrome(a: int) -> int:
#     a += 1
#     while str(a) != str(a)[::-1]:
#         a += 1
#     return a

# print(next_palindrome(99)) # 101

# def all_digits_even(k: int) -> bool:
#     k = list(str(k))
#     res =  [char for char in k if int(char) % 2 == 0]
#     return True if len(res) > 0 else False
# print(all_digits_even(12))


# def factorial(d: int) -> int:
#     if d == 0:
#         return 1
#     if d == 1:
#         return 1
#     return d * (factorial(d - 1))

# def is_strong(n: int) -> bool:
#     n = list(str(n))
#     res = [factorial(int(strong)) for strong in n]
#     return True if sum(res) == int("".join(n)) else False

# def next_leap_year(yyyy: int) -> int:
#     return yyyy + 4 - yyyy % 4


# def num_digits(p: int) -> int:
#     return len(list(str(p)))


# print(num_digits(123))


# def is_armstrong(n: int) -> bool:
#     n = list(str(n))
#     res = [pow(int(armstrong), 3) for armstrong in n]
#     return sum(res) == int("".join(n))


# print(is_armstrong(153))


# class Classification(enumerate):
#     abundant = "abundant"
#     perfect = "perfect"
#     deficient = "deficient"


# def classify(k: int) -> int:
#     res = sum([i for i in range(1, k) if k % i == 0])
#     if res == k:
#         return Classification.perfect
#     elif res > k:
#         return Classification.abundant
#     else:
#         return Classification.deficient


# print(classify(12))  # abundant
# print(classify(6))  # perfect
# print(classify(8))  # deficient
# print(classify(28)) # perfect
#     return yyyy + 4 - yyyy % 4from functools import reduce
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = []
#         n = len(nums)
#         left_products = [1] * n
#         right_products = [1] * n
#         res = [1] * n

#         for i in range(1, n):
#             left_products[i] = left_products[i - 1] * nums[i - 1]

#         for i in range(n - 2, -1, -1):
#             right_products[i] = right_products[i + 1] * nums[i + 1]
#         for i in range(n):
#             res[i] = left_products[i] * right_products[i]
#         # print(reduce((lambda x, y: x * y),nums)) -> cummulative product of list
#         return res


# def double_it(n: int) -> int:
#     while n <= 100:
#         n *= 2
#         print(n)

# print(double_it(2))


# def main():
#     dictionary = dict()
#     dictionary["learning"] = "awesome"
#     dictionary["coding"] = "fun"
#     dictionary["learn"] = "awesome"
#     dictionary["code"] = "fun"

#     dictionary = remove_keys_containing_string(dictionary, "learn")
#     print(dictionary)

# def remove_keys_containing_string(dictionary: dict, remove: str):
#     new_dictionary = dict()
#     for key in dictionary.keys():
#         if remove not in key:
#             new_dictionary[key] = dictionary[key]
#     return new_dictionary

# main()


# Fill Karel

# from stanfordkarel import (
#     move,
#     right_is_clear,
#     facing_east,
#     turn_left,
#     right_is_blocked,
#     not_facing_east,
#     put_beeper,
#     beepers_present,
#     facing_west,
#     pick_beeper,
#     no_beepers_present,
#     not_facing_west,
#     front_is_clear,
#     beepers_in_bag,
#     facing_south,
#     front_is_blocked,
#     no_beepers_in_bag,
#     not_facing_south,
#     left_is_clear,
#     facing_north,
#     left_is_blocked,
#     run_karel_program,
# )

# from karel.stanfordkarel import *


# def main():
#     fill_world()


# def fill_world():
#     while front_is_clear():
#         fill_row()
#         move_to_next_row()


# def fill_row():
#     while front_is_clear() or no_beepers_present():
#         put_beeper()
#         if front_is_clear():
#             move()


# def move_to_next_row():
#     turn_left()
#     turn_left()
#     while beepers_present():
#         move()
#         if front_is_blocked() and facing_west():
#             turn_right()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# if __name__ == "__main__":
#     run_karel_program()

# from typing import List
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         N = len(nums)

#         first = {}

#         current = 0
#         longest = 0

#         first[current] = 0
#         for i in range(N):
#             if nums[i] == 0:
#                 nums[i] = -1
#             current += nums[i]
#             if current in first:
#                 longest = max(longest, i + 1 - first[current])
#             else:
#                 first[current] = i + 1
#         return longest

# import collections
# import heapq
# import string
# class Solution:
#     def minimizeStringValue(self, s: str) -> str:
#         f = collections.Counter(s)
#         h = []
#         for c in string.ascii_lowercase:
#             heapq.heappush(h,  (f[c], c))
# class Solution:
# def minimizeStringValue(self, s: str) -> str:
# f = Counter(s)
# h = []
# for c in string.ascii_lowercase:
# heapq.heappush(h,  (f[c], c))
#
# q = []
# ans = []
#
# for c in s:
# if c == "?":
# count, now = heapq.heappop(h)
# q.append(now)
# heapq.heappush(h, (count + 1, now))
# q.sort()
# q = collections.deque(q)
# for c  in s:
# if c == "?":
# ans.append(q.popleft())
# else:
# ans.append(c)
# return "".join(ans)
# first[current] = i + 1
# return longest

# class Solution:
# def findMinArrowShots(self, points: List[List[int]]) -> int:
# N = len(points)
#
# START, END = 0, 1
# events = []
# for index, (s, e) in enumerate(points):
# events.append((s, START, index))
# events.append((e, END, index))
# events.sort()

# bursted = [False] * N
# current = set()
# shots = 0

# for x, t, index in events:
# if t == START:
# current.add(index)
# else:
# if bursted[index]:
# continue
# shots += 1
# for c in current:
# bursted[c] = True
#
# return shots
#
# class Solution:
# def findMinArrowShots(self, points):
# points.sort(key = lambda x: x[1])
#
# total, end_point = 0, float("-inf")
#
# for i in points:
# if i[0] > end_point:
# total += 1
# end_point = i[1]
#
# return total
# import collections
# import heapq
# import string
# class Solution:
#     def minimizeStringValue(self, s: str) -> str:
#         f = collections.Counter(s)
#         h = []
#         for c in string.ascii_lowercase:
#             heapq.heappush(h,  (f[c], c))

#         q = []
#         ans = []

#         for c in s:
#             if c == "?":
#                 count, now = heapq.heappop(h)
#                 q.append(now)
#                 heapq.heappush(h, (count + 1, now))
#         q.sort()
#         q = collections.deque(q)
#         for c  in s:
#             if c == "?":
#                 ans.append(q.popleft())
#             else:
#                 ans.append(c)
#         return "".join(ans)

# from typing import List


# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         N = len(nums)

#         first = {}

#         current = 0
#         longest = 0

#         first[current] = 0
#         for i in range(N):
#             if nums[i] == 0:
#                 nums[i] = -1
#             current += nums[i]
#             if current in first:
#                 longest = max(longest, i + 1 - first[current])
#             else:
#                 first[current] = i + 1
#         return longest


# def is_curzon(num: int) -> bool:
#     return (pow(2, num) + 1) % ((2 * num) + 1) == 0


# print(is_curzon(5))  # True


# def is_valid_triangle(side1: int, side2: int, side3: int) -> bool:
#     return (side1 + side2) > side3


# def is_circularprime(num: int) -> bool:
#     num = list(str(num))
#     N = len(num)
#     def is_prime(num: int) -> bool: ⭐
#         if num < 2:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     for _ in range(N, -1, -1):
#         curr_num = int("".join(num))
#         if is_prime(curr_num):
#             num = num[-1:] + num[:-1]
#         else:
#             return False
#     return True

# print(is_circularprime(1193))  # True


# def biggest_prime_of_eight_digit_number(num: int) -> int:
#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True

#     num = list(str(num))
#     num.sort(reverse=True)
#     N = len(num)
#     res = []
#     for i in range(N):
#         if is_prime(int(num[i])):
#             res.append(num[i])
#     return int("".join(res))


# How does the is_prime function determine if a number is prime?

# from typing import List
# def kaprekar_seq(n: int) -> List[int]:
#     n = sorted(str(n), reverse=True)
#     n2 = sorted(n, reverse=False)
#     book = []
#     if n == n2:
#         return book.append(int("".join(n)))
#     book.append(int("".join(n)))
#     product = 0
#     while product != 6174:
#         product = int("".join(n)) - int("".join(n2))
#         n = sorted(str(product), reverse=True)
#         n2 = sorted(n, reverse=False)
#         book.append(product)
#     return book

# print(kaprekar_seq(1945)) # 6174

# how do I get the value from a node in a linked list?

# from typing import List, Optional
# def isPalindrome(self, head: Optional[ListNode]) -> bool:
#     res = ""
#     cur = head
#     while cur:
#         res += str(cur.val)
#         cur = cur.next
#     return res == res[::-1]


# from typing import List
# def fizz_buzz(n: int) -> List[str]:
#     res = []
#     for i in range(1, n + 1):
#         if i % 3 == 0:
#             res.append("Fizz")
#         elif i % 5 == 0:
#             res.append("Buzz")
#         elif (i  % 3 == 0) and (i % 5 == 0):
#             res.append("FizzBuzz")
#     return res


# print(
#     fizz_buzz(15)
# )  # ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


# def vowel_to_upper_cons_to_lower(string: str) -> str:
#     vowels = "aeiouy"
#     string = list(string)
#     N = len(string)
#     for i in range(N):
#         if string[i] in vowels:
#             string[i] = string[i].upper()
#         else:
#             string[i] = string[i].lower()
#     return "".join(string)

# print(vowel_to_upper_cons_to_lower("Hello")) # "hEllO"

# from typing import List
# def split_Even_Odd_Sublist(num_array: List[int]) -> List[List[int]]:
#     res = [[] for _ in range(2)]
#     for i in range(len(num_array)):
#         if  num_array[i] % 2 == 0:
#             res[0].append(num_array[i])
#         else:
#             res[1].append(num_array[i])
#     return res

# print(split_Even_Odd_Sublist([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [[2, 4, 6, 8], [1, 3, 5, 7, 9]]


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
#         dp = [0] * (n + 1)
#         dp[1] = dp[2] = 1
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#         return dp[n]


# class Solution:
#     def minOperations(self, k: int) -> int:
#         nums = [1]
#         num_operations = 0

#         if sum(nums) >= k:
#             return 0

#         while True:
#             max_num = max(nums)

#             if max_num * 2 >= k:
#                 nums.append(max_num)
#             else:
#                 nums.append(max_num * 2)

#             num_operations += 1

#             if sum(nums) >= k:
#                 break

#         operations_dict = dict()
#         for i in range(num_operations):
#             if nums[i] == nums[i + 1]:
#                 operation = "increase"
#                 element = nums[i]
#             else:
#                 operation = "duplicate"
#                 element = nums[i] * 2
#             operations_dict[i] = {"operation": operation, "element": element}

#         for i in range(len(operations_dict)):
#             if operations_dict[i]["operation"] == "increase":

# from typing import List
# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#       max_val, alt = 0, 0
#       for i in gain:
#         alt += i
#         max_val = max(alt, max_val)
#       return max_val

# print(Solution().largestAltitude([-5, 1, 5, 0, -7])) # 1

# import collections
# from typing import List
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return min(collections.Counter(nums), key=collections.Counter(nums).get)

# print(Solution().singleNumber([4, 1, 2, 1, 2])) # 4


# from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         current = root
#         res = []
#         while current:
#             if current.val == val:
#                 res.append(current)
#             elif current.val < val:
#                 current = current.right
#             else:
#                 current = current.left
#         return res
# print(Solution().searchBST([4, 2, 7, 1, 3], 2)) # [2, 1, 3]


# def length(seq) -> int:
#     if isinstance(seq, (str, list, tuple, set, dict, range, bytes)):
#         return len(seq)
#     elif isinstance(seq, int):
#         return len(str(seq))
#     elif isinstance(seq, float):
#         return len(str(seq).replace(".", ""))
#     else:
#         return seq


# print(length("hello"))  # 5
# print(length([1, 2, 3, 4, 5]))  # 5
# print(length((1, 2, 3, 4, 5)))  # 5
# print(length({1, 2, 3, 4, 5}))  # 5
# print(length({"one": 1, "two": 2, "three": 3}))  # 3
# print(length(range(5)))  # 5
# print(length(12345))  # 5
# print(length(b"hello"))  # 5
# print(length(12345.0))  # 5
# print(length(True))  # 4

# from itertools import accumulate
# def summation(seq) -> int:
#     res = [i for i in seq if isinstance(i, int)]
#     return list(accumulate(res))[-1]

# print(summation([1, 2, 3, 4, 5])) # 15


# from typing import List
# def kaprekar_seq(n: int, book: List[int] = None) -> List[int]:
#     if book is None:
#         book = []
#     n = sorted(str(n), reverse=True)
#     n2 = sorted(n, reverse=False)
#     if n == n2:
#         book.append(int("".join(n)))
#         return book
#     book.append(int("".join(n)))
#     product = int("".join(n)) - int("".join(n2))
#     n = sorted(str(product), reverse=True)
#     n2 = sorted(n, reverse=False)
#     book.append(product)
#     if product != 6174:
#         return kaprekar_seq(product, book)
#     return book


# print(kaprekar_seq(1945)) # 6174
# def isInc(n: int) -> bool:
#     prev = n % 10
#     if n < 10:
#         return True
#     elif n > 10:
#         return isInc(n // 10) and prev > n // 10 % 10

# from typing import List
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if not nums:
#             return 1

#         n = len(nums)
#         for i in range(n):
#             while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1

#         return n + 1
# nums = list(range(1, 10001))
# print(Solution().firstMissingPositive([1, 2, 0])) # 3
# print(Solution().firstMissingPositive(nums)) # 100001

# from typing import List
# def collatz_seq(q: int) -> List[int]:
#   if q == 1:
#     return [1]
#   elif q % 2 == 0:
#     return [q] + collatz_seq(q  // 2)
#   else:
#     return [q] + collatz_seq(3 * q + 1)

# print(collatz_seq(13)) # [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]


# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n)[2:].count('1')

# def variable_to_camel_case(text: str) -> str:
#     for i, str in enumerate(text):
#         if i == 0:
#           continue
#         if str == "_":
#             text = text.replace(str, "")
#             text = text[:i] + text[i].upper() + text[i + 1:]
#     return text

# print(variable_to_camel_case("hello_world")) # "helloWorld"


# def camel_case_to_snake_case(camel: str) -> str:
#     for i, str in enumerate(camel):
#         if str.isupper():
#             camel = camel.replace(str, "_" + str.lower())
#     return camel

# print(camel_case_to_snake_case("helloWorld")) # "hello_world"

# import time

# def anagram(s1: str, s2: str) -> bool:
#   return len(set(s2) & set(s1)) == len(s2)

# print(anagram("listen", "silent")) # True

# from collections import Counter

# def anagrams2(s1: str, s2: str) -> bool:
#   return Counter(s1) == Counter(s2)

# print(anagrams2("listen", "silent")) # True

# def convertToSeconds(s: str) -> int:
#     return int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:])

# print(convertToSeconds("12:30:15"))  # 45015

# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return None
#         curr = head
#         count = 0
#         while curr:
#             count += 1
#             curr = curr.next
#         mid = count // 2
#         curr = head
#         prev = None
#         while mid:
#             prev = curr
#             curr = curr.next
#             mid -= 1
#         prev.next = curr.next
#         return head


# from typing import List
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Dictionary to store groups of anagrams
#         res = defaultdict(list)
#         # Iterate through the list of strings
#         for s in strs:
#             # Initialize count list with 26 zeros, representing the 26 letters of the English alphabet
#             count = [0] * 26
#             # Iterate through the characters of the string
#             for c in s:
#                 # Increment the count of the character at its position in the alphabet
#                 count[ord(c) - ord("a")] += 1
#             # Convert the count list to a tuple to make it hashable and use as a key in the dictionary
#             # Add the original string to the list corresponding to the tuple key
#             res[tuple(count)].append(s)
#         # Return the values of the dictionary, which are lists of grouped anagrams
#         return res.values()

# print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# def pascal_output(size: int) -> str:
#   res = []
#   space = " "
#   for i in range(size):
#     res.append(
#       space * (size - i - 1) +
#       " ".join(str(11 ** i))
#     )
#   return "\n".join(res)

# print(pascal_output(5))


# def upto_n(n: int) -> str:
#     res = []
#     row = []
#     count = 1
#     while count <= n:
#         for i in range(len(res) + 1):
#             if count <= n:
#                 row.append(str(count))
#                 count += 1
#         res.append(" ".join(row))
#         row = []
#     res.append("**")
#     return "\n".join(res)
# print(upto_n(15))

# from typing import List
# from collections import defaultdict


# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         def atMostK(k: int) -> int:
#             count = defaultdict(int)
#             res = l = 0
#             for r in range(len(nums)):
#                 if count[nums[r]] == 0:
#                     k -= 1
#                 count[nums[r]] += 1
#                 while k < 0:
#                     count[nums[l]] -= 1
#                     if count[nums[l]] == 0:
#                         k += 1
#                     l += 1
#                 res += r - l + 1
#             return res
#         return atMostK(k) - atMostK(k - 1)
# print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3)) # 7


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         N = len(needle)
#         for i in range(len(haystack) - N + 1):
#             if haystack[i:N + i] == needle:
#                 return i
#         return -1


# print(Solution().strStr("hello", "ll")) # 2
# from typing import List
# class Solution:
#     def searchInsert(nums: List[int], target: int) -> int:
#         found = -1 if not nums.index(target) else nums.index(target)
#         if found == -1:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)
#         return found
# print(Solution.searchInsert([1, 3, 5, 6], 5)) # 2


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().replace(" ", " ").split(" ")[-1])

# from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1 = [i for i in  nums1 if nums[i] != 0]
#         nums2 = [i for i in  nums2 if nums[i] != 0]
#         print(f"1{nums1}, 2{nums2}")
#         return [1, 2, 2, 3, 5, 6]

# from typing import List
# class Solution:
#     def countAlternatingSubarrays(nums: List[int]) -> int:
#         count = 0
#         length = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 length += 1
#             else:
#                 count += (length * (length + 1)) // 2
#                 length = 1

#         count += (length * (length + 1)) // 2
#         return count
# nums = [0, 1, 1, 1]
# print(Solution.countAlternatingSubarrays(nums))


# def manhattan_distance(point1: list, point2: list) -> int:
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# print(manhattan_distance([1, 1], [0, 0])) # 2

# from typing import List

# class Solution:
#     def minimumDistance(self, points: List[List[int]]) -> int:
#         min_max_distance = float('inf')
#         for i in range(len(points)):
#             point_removed = points.pop(i)
#             max_distance = self.calculate_max_distance(points)
#             min_max_distance = min(min_max_distance, max_distance)
#             points.insert(i, point_removed)
#         return min_max_distance

#     def calculate_max_distance(self, points: List[List[int]]) -> int:
#         max_distance = 0
#         for i in range(len(points)):
#             for j in range(i + 1, len(points)):
#                 max_distance = max(max_distance, self.manhattan_distance(points[i], points[j]))
#         return max_distance

#     def manhattan_distance(self, point1: list, point2: list) -> int:
#         return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# print(Solution().minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))  # Output: 12
# print(Solution().minimumDistance([[1, 1], [1, 1], [1, 1]]))  # Output: 0
# print(
#     Solution().minimumDistance([[3, 2], [3, 9], [7, 10], [4, 4], [8, 10], [2, 7]])
# )  # Output: 4
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         sum = 0
#         N = len(s)
#         i = 0
#         while i < N:
#           if i < N - 1 and d[s[i]] < d[s[i + 1]]:
#             sum += d[s[i+1]] - d[s[i]]
#             i += 2
#           else:
#             sum += d[s[i]]
#             i += 1
#         return sum

# from typing import List
# from collections import Counter


# class Solution:

#     def topKFrequent(nums: List[int], k: int) -> List[int]:
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         return [num for num, _ in count.most_common(k)]


# print(Solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))

# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         maxCount = max(Counter(nums), key=Counter(nums).get)
#         res = []
#         l = 0
#         for right, num in enumerate(nums):
#             count = 0
#             if num == maxCount:
#                 count += 1
#             while count > k:
#                 if nums[l] == maxCount:
#                     count -= 1
#                 l += 1
#             res.append()
#         return res

# print(Solution.countSubarrays([1, 2, 1, 2, 3], 2)) # 7
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return len(set(zip(s,t))) == len(set(s)) == len(set(t))

# def rus_mult_print(a: int, b: int) -> None:
#     runningTotal = 0
#     while a > 0:
#         if a % 2 != 0:
#             print(f"{a:2d} {b:3d} +")
#             runningTotal += b
#         else:
#             print(f"{a:2d} {b:3d} x")
#         a //= 2
#         b *= 2
#     print(f"= {runningTotal}")

# print(rus_mult_print(13, 17))

# def upside_down_triangle(length: int):
# print(Solution.topKFrequent(

# ))


# from itertools import groupby
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         N = len(nums)

#         def calc(nums):
#             N = len(nums)

#             last_min_index = None
#             last_max_index = None

#             total = 0
#             for index, x in enumerate(nums):
#                 if x == minK:
#                     last_min_index = index

#                 if x == maxK:
#                     last_max_index = index

#                 if last_min_index is not None and last_max_index is not None:
#                     total += min(last_min_index, last_max_index) + 1
#             return total

#         total = 0
#         for g, vs in groupby(nums, key=lambda x: minK <= x <= maxK):
#             if g:
#                 total += calc(list(vs))
#         return total


# LIMIT = 50
# def print_pyram(n: int) -> None:
#     for i in range(1, n + 1):
#         for _ in range(i):
#             print(format(i,"^2"), " ", sep="", end="")
#         print("", sep="")

# print(print_pyram(LIMIT))


# class Solution:
#     def exist(self, board, word):
#         def backtrack(i, j, k):
#             if k == len(word): return True
#             if (
#                 i < 0
#                 or i >= len(board)
#                 or j < 0
#                 or j >= len(board[0])
#                 or board[i][j] != word[k]
#             ): return False

#             temp = board[i][j]
#             board[i][j] = ""

#             if (
#                 backtrack(i + 1, j, k + 1)
#                 or backtrack(i - 1, j, k + 1)
#                 or backtrack(i, j + 1, k + 1)
#                 or backtrack(i, j - 1, k + 1)
#             ): return True

#             board[i][j] = temp
#             return False

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if backtrack(i, j, 0):
#                     return True
#         return False
# from typing import List
# class Solution:
#     def exist(self, A: List[List[str]], S: str) -> bool:
#         R, C = len(A), len(A[0])
#         V = [[False]*C for r in range(R)]
#         def dfs(r, c, p):
#             if V[r][c] or A[r][c] != S[p]: return False
#             V[r][c] = True
#             if p+1 == len(S): return True
#             for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
#                 if i < 0 or i >= R or j < 0 or j >= C: continue
#                 if dfs(i, j, p+1): return True
#             V[r][c] = False
#             return False
#         return any(dfs(r, c, 0) for r in range(R) for c in range(C))


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def dfs(i, j, k, vis):
#             if k == len(word):
#                 return True
#             if (i, j) in vis or i < 0 or i == len(board) or j < 0 or j == len(board[0]):
#                 return False
#             if board[i][j] != word[k]:
#                 return False
#             if board[i][j] == word[k]:
#                 k += 1
#             vis.add((i, j))
#             u, d, l, r = (
#                 dfs(i - 1, j, k, vis),
#                 dfs(i + 1, j, k, vis),
#                 dfs(i, j - 1, k, vis),
#                 dfs(i, j + 1, k, vis),
#             )
#             vis.remove((i, j))
#             return u or d or l or r

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i, j, 0, set()):
#                     return True
#         return False


# def pyramid_a1(size: int) -> None:
#     output = []
#     for line_num in range(1, size + 1):
#         output += [" " * (size - line_num) + "*" * ((line_num * 2) - 1)]
#     print("\n".join(output))

# print(pyramid_a1(8))


# def patternC(size: int) -> None:
#     output = []
#     for line_num in range(1, size + 1):
#         space = size - line_num
#         output += [
#           " " * space +
#           (
#     "@" if line_num == 1 else f"@{'-' * (((line_num * 2)) - 3)}@"
#           )
#         ]

#     print("\n".join(output))
# print(patternC(20))


# def upside_down_triangle(length: int) -> None:
#     for i in range(length):
#         print(" " * i + "*" * (2 * (length - i) - 1))
# print(upside_down_triangle(7))

# def right_angle(length: int):

# def right_angle(length: int) -> None:
#     for i in range(length):
#         print("*" * (i + 1))
# print(right_angle(7))

# def right_angle_opp(length: int):
#     for i in range(length):
#         print(" " * (length - i) + "*" * i)
# print(right_angle_opp(7))

# def diamond(length: int):

# def right_angle_opp(length: int) -> None:
#     for i in range(length):
#       print(" " * (length - i) + "*" * i)
# print(right_angle_opp(7))


# def diamond(length: int) -> None:
#     for i in range((length // 2)):
#         print(" " * (length - i - 1) + "*" * (2 * i + 1))
#     print(" " * (length // 2) + "*" * length)
#     for i in range((length // 2) - 1, -1, -1):
#         print(" " * (length - i - 1) + "*" * (2 * i + 1))
# print(diamond(13))

# from math import floor, sqrt
# from math import floor, sqrt
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return floor(sqrt(x))
# print(Solution.mySqrt(9))

# class Solution:
#         return floor(sqrt(x))
# print(Solution.mySqrt(9))

#     def maxDepth(self, s: str) -> int:
#             accumulate(map(lambda c: 1 if c == "(" else -1 if c == ")" else 0, s))
#         )
# bin()

# def rps_evaluation(player_one: str, player_two:str) -> int:
#     if player_one == player_two:
#         return 0
#     if (player_one == "Rock" and player_two == "Scissors") or (player_one == "Scissors" and player_two == "Paper") or (player_one == "Paper" and player_two == "Rock"):
#         return 1
#     else:
#         return -1

# def length_longest_substring(s: str) -> int:
#     if not s: return 0
#     N = len(s)
#     l, r = 0, 0
#     seen = set()
#     max_length = 0
#     while l < N and r < N:
#         if s[r] not in seen:
#             seen.add(s[r])
#             r += 1
#             max_length = max(max_length, r - l)
#         else:
#             seen.remove(s[l])
#             l += 1
#     return max_length

# print(length_longest_substring("pwwkew"))

# class Solution:
#     def makeGood(s: str) -> str:
#         N = len(s)
#         if N == 1:  return s
#         l, r = 0, 1
#         while r <= N - 1:
#             if (
#                 s[l].isupper() and s[r].islower() and s[l].lower() == s[r]
#                 or s[l].islower() and s[r].isupper() and s[l].upper() == s[r]
#             ):
#                 s = s[:l] + s[r + 1 :]
#                 N -= 2
#                 l = 0
#                 r = 1
#             else:
#                 l += 1
#                 r += 1
#         return s

# print(Solution.makeGood("leEeetcode")) # "leetcode"


# class Solution:
#     def makeGood(self, s: str) -> str:
#         stack = []
#         for char in s:
#             if stack:
#                 if char.lower() == stack[-1].lower() and char != stack[-1]:
#                     stack.pop()
#                 else:
#                     stack.append(char)
#             else:
#                 stack.append(char)
#         return "".join(stack)

# def line(line_num:int) -> str:
#     return start_line() + repeat_middle(line_num + 1) + end_line()

# def start_line() -> str:
#     return '@'

# def end_line() -> str:
#     return '@'

# def repeat_middle(line_num: int) -> str:
#     return '-' * line_num

# def pyramid_b1(size: int) -> list[str]:
#     pyramid = []
#     pyramid.append(end_line())
#     for line_num in range(size):
#         pyramid.append(line(line_num))
#     return pyramid

# def format_pyramid(pyramid: list[str]) -> str:
#     WIDTH = 30
#     CRLF = '\n'
#     result = []
#     for line in pyramid:
#         result.append(line.center(WIDTH))
#     return CRLF.join(result)

# print(format_pyramid(pyramid_b1(10)))

# def patternC(size: int) -> None:
#     output = []
#     for line_num in range(1, size + 1):
#         space = size - line_num
#         output += [
#             " " * space
#             + ("@" if line_num == 1 else f"@{'-' * (((line_num * 2)) - 3)}@")
#         ]

#     print("\n".join(output))


# print(patternC(20))
# from bitstring import BitArray


# class Solution:
#     @staticmethod
#     def reverseBits(n: int) -> int:
#         bString: str = bin(n)[2:]  # Convert to binary and remove '0b'
#         bString = bString.zfill(32)  # Pad with zeros to ensure 32 bits
#         reversedString: str = bString[::-1]  # Reverse the string
#         return int(reversedString, 2)  # Convert back to integer

# print(Solution.reverseBits(0b00000010100101000001111010011100))

# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         lo = hi = 0
#         for c in s:
#             lo += 1 if c == "(" else -1
#             hi += 1 if c != ")" else -1
#             if hi < 0:
#                 break
#             lo = max(lo, 0)
#         return lo == 0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         curr = head
#         while curr and curr.next:
#             if curr.val == curr.next.val:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next
#         return head


# from typing import List
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         hset = {}
#         for idx in range(len(nums)):
#             if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
#                 return True
#             hset[nums[idx]] = idx
#         return False

# print(Solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))


# def longestMonotonicSubarray(nums: list[int]) -> int:
#     return len(max(longest_increasing(nums), longest_decreasing(nums)))


# def longest_increasing(nums: list[int]) -> list[int]:
#     res: list[list[int]] = []
#     for left in range(len(nums)):
#         for right in range(left, len(nums)):
#             if all(nums[i] < nums[i + 1] for i in range(left, right)):
#                 res.append(nums[left : right + 1])
#     return max(res, key=len)


# def longest_decreasing(nums: list[int]) -> list[int]:
#     res: list[list[int]] = []
#     for left in range(len(nums)):
#         for right in range(left, len(nums)):
#             if all(nums[i] > nums[i + 1] for i in range(left, right)):
#                 res.append(nums[left : right + 1])
#     return max(res, key=len)


# print(longest_decreasing([1, 4, 3, 3, 2]))
# print(longest_increasing([1, 4, 3, 3, 2]))
# print(longestMonotonicSubarray([1, 4, 3, 3, 2]))


# def solution(sides: list[tuple[int, int], tuple[int, int], tuple[int, int]]) -> bool:
#     # Since the list contains sub-arrays of tuples we utilize two for loops
#     # This just looks at tuple[int, int], tuple[int, int], tuple[int, int]
#     for side in sides:
#         # range(start, end, step)
#         # this essentially just looks at the first, second, and third element of the tuple
#         for i in range(0, 3, 3):
#             print(side[i], side[i + 1], side[i + 2])
#             """
#                 AB + BC must be greater than AC, or AB + BC > AC
#                 AB + AC must be greater than BC, or AB + AC > BC
#                 BC + AC must be greater than AB, or BC + AC > AB
#             """
#             if (
#                 side[i] + side[i + 1] > side[i + 2]
#                 and side[i] + side[i + 2] > side[i + 1]
#                 and side[i + 1] + side[i + 2] > side[i]
#             ):
#                 return True
#     return False


# print(solution([(7, 2, 2), (1, 2, 2), (7, 2, 2)]))


# import math


# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     return False


# def is_triangle_validation(vertices: list) -> bool:
#     if len(vertices) != 3:
#         return False
#     a = math.sqrt(
#         (vertices[0][0] - vertices[1][0]) ** 2 + (vertices[0][1] - vertices[1][1]) ** 2
#     )
#     b = math.sqrt(
#         (vertices[1][0] - vertices[2][0]) ** 2 + (vertices[1][1] - vertices[2][1]) ** 2
#     )
#     c = math.sqrt(
#         (vertices[2][0] - vertices[0][0]) ** 2 + (vertices[2][1] - vertices[0][1]) ** 2
#     )
#     return is_triangle(a, b, c)


# def main():
#     vertices = [[3, 2], [-2, -3], [2, 3]]
#     print(is_triangle_validation(vertices))


# if __name__ == "__main__":
#     main()

# a, b = 0, 1
# while b < 10:
#     a, b = b , a + b


# def roman2arabic(r: str) -> int:
#     roman: dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     total: int = 0
#     for i in range(len(r)):
#         value: int = roman[r[i]]
#         if (i + 1 < len(r) and roman[r[i + 1]] > value):
#             total -= value
#         else:
#             total += value
#     return total

# print(roman2arabic(
#   "VII"
# ))

# def arabic2roman(num: int) -> str:
#     values = {
#         1000: "M",
#         900: "CM",
#         500: "D",
#         400: "CD",
#         100: "C",
#         90: "XC",
#         50: "L",
#         40: "XL",
#         10: "X",
#         9: "IX",
#         5: "V",
#         4: "IV",
#         1: "I",
#     }
#     res: list[str] = []
#     for value, numeral in values.items():
#         res.append(num // value * numeral)
#         num %= value
#     return "".join(res)

# def arabic2roman(num: int) -> str:
#     values = {
#         1000: "M",
#         900: "CM",
#         500: "D",
#         400: "CD",
#         100: "C",
#         90: "XC",
#         50: "L",
#         40: "XL",
#         10: "X",
#         9: "IX",
#         5: "V",
#         4: "IV",
#         1: "I",
#     }
#     res: list[str] = []
#     for value, numeral in values.items():
#         res.append(num // value * numeral)
#         num %= value
#     return "".join(res)


# print(arabic2roman(12))  # "XII"
# print(arabic2roman(12))  # "XII"

# from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#         l, r = 0, len(height) - 1
#         leftMax, rightMax = height[l], height[r]
#         res = 0
#         while l < r:
#             if leftMax < rightMax:
#                 l += 1
#                 leftMax = max(leftMax, height[l])
#                 res += leftMax - height[l]
#             else:
#                 r -= 1
#                 rightMax = max(rightMax, height[r])
#                 res += rightMax - height[r]
#         return res
# from typing import List
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#         prev = [0] * m
#         ans = 0
#         for i in range(n):
#             curr = [0] * m
#             for j in range(m):
#                 if (matrix[i][j] == '1'): curr[j] = 1 + prev[j]
#             for j in range(m):
#                 mn = 1e9
#                 for k in range(j, m):
#                     mn = min(mn, curr[k])
#                     ans = max(ans, mn * (k - j + 1))
#             prev = curr
#         return ans


# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix or not matrix[0]: return 0
#         m = len(matrix)
#         n = len(matrix[0])

#         # For each column, keep track of the height of 1s in that column above the current row.
#         # The last entry (`heights[n]`) is always equal to zero.
#         heights = [0] * (n + 1)

#         best = 0
#         for row in matrix:
#             # Update the column heights.
#             for col in range(n):
#                 heights[col] = heights[col] + 1 if row[col] == '1' else 0

#             # Given a collection of heights (such as 3, 1, 3, 2, 2), find the largest rectangle.
#             stack = [-1]
#             for col in range(n + 1):
#                 # Consider the rectangle from stack[-1] to col.
#                 while heights[col] < heights[stack[-1]]:
#                     h = heights[stack.pop()]
#                     w = col - stack[-1] - 1
#                     best = max(best, h * w)
#                 stack.append(col)
#         return best


# class Solution:
#     def scoreOfString(s: str) -> int:
#         res: list[int] = []
#         for c in range(len(s) - 1):
#             res.append(abs(ord(s[c]) - ord(s[c + 1])))
#         return sum(res)

# print(Solution.scoreOfString("zaz"))

# from typing import List
# class Solution:
#     @staticmethod
#     def minRectanglesToCoverPoints(points: List[List[int]], w: int) -> int:
#         # Sort the points by x-coordinate
#         points.sort(key=lambda p: p[0])

#         rectangles = 0
#         i = 0
#         while i < len(points):
#             rectangles += 1
#             j = i + 1
#             while j < len(points) and points[j][0] - points[i][0] <= w:
#                 j += 1
#             i = j

#         return rectangles

# print(Solution.minRectanglesToCoverPoints([[2, 3], [1, 2]], 2))

# import heapq
# from typing import List


# class Solution:
#     @staticmethod
#     def minimumTime(n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
#         graph = [[] for _ in range(n)]
#         for u, v, length in edges:
#             graph[u].append((v, length))
#             graph[v].append((u, length))

#         time = [float("inf")] * n
#         time[0] = 0
#         pq = [(0, 0)]

#         while pq:
#             t, node = heapq.heappop(pq)
#             if t > time[node]:
#                 continue
#             for v, length in graph[node]:
#                 if t + length < time[v] and t + length < disappear[v]:
#                     time[v] = t + length
#                     heapq.heappush(pq, (time[v], v))

#         return [t if t < float("inf") else -1 for t in time]


# print(Solution.minimumTime(2, [[0, 1, 1]], [1,1]))


# from typing import List
# class Solution:
#     @staticmethod
#     def numberOfSubarrays(nums: List[int]) -> int:
#         stack = []
#         count = 0
#         for num in nums:
#             while stack and stack[-1] < num:
#                 stack.pop()
#             stack.append((num, stack.count((num,)) if stack else 1))
#             count += stack[-1][1]
#         return count

# print(Solution.numberOfSubarrays([3, 3, 3]))

# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     @staticmethod
#     def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
#         if root is None: return 0
#         res = 0
#         def dfs(
#             node: Optional[TreeNode],
#             is_left: bool,
#         ):
#             nonlocal res
#             if not node.left and not node.right and is_left:
#                 res += node.val
#             if node.left:
#                 dfs(node.left, True)
#             if node.right:
#                 dfs(node.right, False)


#         dfs(root, False)
#         return res

# print(Solution.sumOfLeftLeaves([3,9,20,None ,None,15,7]))

# class Solution:
#     @staticmethod
#     def findLatestTime(s: str) -> str:
#         hour = s[:2]
#         minutes = s[3:]

#         if "?" in hour:
#             if hour.index("?") == 0:
#                 hour = hour.replace(
#                     "?", "1" if hour[1] != "?" and hour[1] <= "9" else "0"
#                 )
#             elif (hour[0] == "0" or hour[0] == "1") and hour[1] == "?":
#                 hour = hour.replace("?", "1")
#         if "?" in minutes:
#             if minutes.index("?") == 0:
#                 minutes = minutes.replace(
#                     "?", "5" if minutes[1] != "?" and minutes[1] <= "9" else "9"
#                 )
#             else:
#                 minutes = minutes.replace("?", "9")

#         return f"{hour}:{minutes}"
# print(Solution.findLatestTime("1?:?4"))
# from typing import List
# class Solution:
#     @staticmethod
#     def maximumPrimeDifference(nums: List[int]) -> int:
#         def is_prime(n: int) -> bool:
#             if n < 2:
#                 return False
#             for i in range(2, int(n ** 0.5) + 1):
#                 if n % i == 0:
#                     return False
#             return True
#         indexes = []
#         for i, num in enumerate(nums):
#             if is_prime(num):
#                 indexes.append(i)
#         print(indexes)
#         return abs(indexes[-1] - indexes[0]) if indexes else 0

# print(Solution.maximumPrimeDifference([4,2,9,5,3]))


# import heapq
# from typing import List

# class Solution:
#     @staticmethod
#     def kthSmallestAmount(coins: List[int], k: int) -> int:
#         max_val = max(coins) * k
#         dp = [float("inf")] * (max_val + 1)
#         dp[0] = 0

#         for coin in coins:
#             for j in range(coin, max_val + 1):
#                 dp[j] = min(dp[j], dp[j - coin] + 1)

#         for j in range(len(dp)):
#             if dp[j] >= k:
#                 return j

# print(Solution.kthSmallestAmount([3, 6, 9], 3))  # Output: 9
# print(Solution.kthSmallestAmount([5, 2], 7))  # Output: 12

# from typing import List


# class Solution:
#     @staticmethod
#     def minimumValueSum(nums: List[int], andValues: List[int]) -> int:
#         n, m = len(nums), len(andValues)
#         dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
#         dp[0][0] = 0
#         for i in range(1, n + 1):
#             min_val = nums[i - 1]
#             for j in range(i, 0, -1):
#                 min_val &= nums[j - 1]
#                 for k in range(1, min(j, m) + 1):
#                     dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + min_val)
#         return dp[n][m] if dp[n][m] != float("inf") else -1


# print(Solution.minimumValueSum([1, 4, 3, 3, 2], [0, 3, 3, 2]))  # Output: 12
# print(Solution.minimumValueSum([2, 3, 5, 7, 7, 7, 5], [0, 7, 5]))  # Output: 17
# print(Solution.minimumValueSum([1, 2, 3, 4], [2]))  # Output: -1

# from typing import List, Optional
# from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     @staticmethod
#     def sumNumbers(root: Optional[TreeNode]) -> int:
#         def dfs(node, stack) -> int:
#             if not node:
#                 return 0
#             stack.append(str(node.val))
#             count = 0
#             if not node.left and not node.right:
#                 count += int("".join(stack))
#             else:
#                 count += dfs(node.left, stack)
#                 count += dfs(node.right, stack)
#             stack.pop()
#             return count

#         return dfs(root, [])

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# print(Solution.sumNumbers(root))


# import random


# class Solution:
#     @staticmethod
#     def numberOfSpecialChars(word: str) -> int:
#         book = set()
#         print(book)
#         print(sorted(word.split(" ")))
#         return 0


# print(Solution.numberOfSpecialChars("aaAbBcC"))
# # class Solution:
#     @staticmethod
#     def sumNumbers(root: Optional[TreeNode]) -> int:
#         def dfs(node, stack) -> int:
#             if not node:
#                 return 0
#             stack.append(str(node.val))
#             count = 0
#             if not node.left and not node.right:
#                 count += int("".join(stack))
#             else:
#                 count += dfs(node.left, stack)
#                 count += dfs(node.right, stack)
#             stack.pop()
#             return count

#         return dfs(root, [])

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# print(Solution.sumNumbers(root))

# from itertools import accumulate
# def sum_of_digit(n: int) -> int:
#     return list(accumulate(range(n)))[-1]

# print(sum_of_digit(8))


# def sum_of_digits2(n: int) -> None:
#     n = list(str(n))
#     print(n)
#     res = [int(i) for i in range(len(n))]
#     return sum(res)
#     # return sum(int(n))

# print(sum_of_digits2(12))


# def num_sum(n: int) -> int:
#     if n == 0:
#         return 0
#     return n % 10 + num_sum(n // 10)

# Implement a function to calculate the gross salary of an employee for the month of March. He is expecting 10% of HRA and 12% of TA on his basic salary. This month every employee will receive a $500 as a bonus.
# def gross_salary(salary: int, hra_percent: int = 10, ta_percent: int = 12, bonus: int = 500) -> float:
#     hra_percent, ta_percent = (hra_percent / 100) * salary, (ta_percent / 100) * salary
#     gross = salary + hra_percent + ta_percent + bonus
#     return gross.__round__(2)

# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
#         if depth == 1: return TreeNode(val, root)
#         def dfs(root, level):
#             if not root: return
#             if level + 1 == depth:
#                 temp, root.left = root.left, TreeNode(val)
#                 if temp: root.left.left = temp
#                 temp, root.right = root.right, TreeNode(val)
#                 if temp: root.right.right = temp
#             dfs(root.left, level + 1)
#             dfs(root.right, level + 1)
#         dfs(root, 1)
#         return root
# from itertools import accumulate
# def sum_of_nums(*n: int) -> int:
#     return list(accumulate(n))[-1]

# print(sum_of_nums(1, 2, 3, 4, 5))

# def cal_sum(*nums):
#     total = 0
#     print(type(nums))
#     for item in nums:
#         total += item
#         return total

# print(cal_sum(10, 20, 30))

# class TreeNode:
#     def __init__(

#     ) -> None:
# from typing import Optional
# class Solution:
#     def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
#         h = []
#         def dfs(root, curr):
#             if not root: return
#             if not root.left and not root.right:
#                 heapq.heappush(h, chr(root.val + 97) + curr)
#             dfs(root.left, (chr(root.val + 97) + curr))
#             dfs(root.right, (chr(root.val + 97) + curr))
#             return
#         dfs(root, "")
#         return h[0]
# from typing import List
# class Solution:
#     @staticmethod
#     def islandPerimeter(grid: List[List[int]]) -> int:
#         R: int = len(grid)
#         C: int = len(grid[0])

#         perimeter: int = 0
#         for row in range(R):
#             for col in range(C):
#                 if grid[row][col] == 1:
#                     perimeter += 4
#                     if row > 0 and grid[row - 1][col] == 1:
#                         perimeter -= 2
#                     if col > 0 and grid[row][col - 1] == 1:
#                         perimeter -= 2
#         return perimeter
# print(
#     Solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
# )
# # if (
# #    backtrack(i + 1, j, k + 1)
# #    or backtrack(i - 1, j, k + 1)
# #    or backtrack(i, j + 1, k + 1)
# #    or backtrack(i, j - 1, k + 1)
# # ): return True


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         return self.count_islands(grid)

#     def flood_fill(self, grid: list[list[str]], r: int, c: int) -> None:
#         if not (0 <= r < len(grid) and 0 <= c < len(grid[0])): return
#         if grid[r][c] == '0': return

#         grid[r][c] = '0'
#         for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             self.flood_fill(grid, r+dr, c+dc)


#     def count_islands(self, grid: list[list[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         ct = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '0': continue
#                 self.flood_fill(grid, r, c)
#                 ct += 1
#         return ct


# def display_in_reverse_order(*strings) -> str:
#     res: list[str] = []
#     for i in strings:
#         res.insert(0, i[::-1])
#     return "".join(res)


# print(display_in_reverse_order("Hello", "world"))


# def count_vowels_const(filename: str) -> tuple:
#     vowels_count = 0
#     consonants_count = 0
#     vowels = set("aeiouy")
#     with open(filename, "r") as file:
#         for line in file:
#             for char in line.lower():
#                 if char.isalpha():
#                     if char in vowels:
#                         vowels_count += 1
#                     else:
#                         consonants_count += 1
#     return vowels_count, consonants_count


# def check_file_char(char: str) -> str:
#     vowels = set("aeiouy")
#     char = char.lower()
#     if char.isalpha():
#         if char in vowels:
#             return "vowel"
#         else:
#             return "consonant"
#     else:
#         return "neither"

# import os

# print(os.getcwd())
# from collections import defaultdict


# def student_ranking_from_file(filename: str):
#     book = defaultdict(list)
#     with open(filename, "r") as file:
#         for line in file:
#             name, score = line.split()
#             book[int(score)].append(name)
#     for score in book:
#         book[score].sort()
#     return sorted(book.items(), key=lambda x: (-x[0], x[1]))


# def world(*guess: str, answer: str) -> None:
#     if (
#         len(guess) != len(answer)
#     ): print("Please make the lengths of both words equal")

#     for i in range(5):
#         guess = input()
#         if guess != answer:

#     print(f"Out of guesses!\n The answer was {answer}")

# from typing import List
# class Solution:
#     def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
#         m, n = len(land), len(land[0])
#         groups = []
#         for y1 in range(m):
#             for x1 in range(n):
#                 if not land[y1][x1]:
#                     continue
#                 if (y1 and land[y1 - 1][x1]) or (x1 and land[y1][x1 - 1]):
#                     continue
#                 y2, x2 = y1, x1
#                 while y2 + 1 < m and land[y2 + 1][x2]:
#                     y2 += 1
#                 while x2 + 1 < n and land[y2][x2 + 1]:
#                     x2 += 1
#                 groups.append([y1, x1, y2, x2])
#         return groups

# from typing import List, Deque
# class Solution:
#     @staticmethod
#     def openLock(deadends: List[str], target: str) -> int:
#         vis = set()
#         q = Deque([("0000", 0)])
#         while q:
#             curr, turn = q.popleft()
#             if curr == target:
#                 return turn
#             if curr in deadends or curr in vis:
#                 continue
#             vis.add(curr)
#             for i, c in enumerate(curr):
#                 up, down = (int(c) + 1) % 10, (int(c) - 1) % 10
#                 if up not in vis:
#                     q.append((curr[:i] + str(up) + curr[i + 1 :], turn + 1))
#                 if down not in vis:
#                     q.append((curr[:i] + str(down) + curr[i + 1 :], turn + 1))
#         return -1

# print(Solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))

# from collections.abc import Callable
# def convert_to_list(n: int) -> list[str]:
#     return list(str(n))

# def num_to_digits(func: Callable[[int], list[str]], n) -> list[int]:
#     return list(map(int, func(n)))

# print(num_to_digits(convert_to_list, 1729))

# from typing import List
# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         visited = set()
#         adjList = defaultdict(list)
#         for edge in edges:
#             adjList[edge[0]].append(edge[1])
#             adjList[edge[1]].append(edge[0])
#         q = []
#         for i in range(0, n):
#             if len(adjList[i]) == 1:
#                 q.append(i)
#         while n > 2:
#             visited = set()
#             for _ in range(0, len(q)):
#                 node = q.pop(0)

#                 for edge in adjList[node]:
#                     if edge in visited:
#                         continue
#                     adjList[edge].remove(node)

#                     if len(adjList[edge]) == 1:
#                         q.append(edge)
#                         visited.add(edge)
#                 adjList.pop(node)
#                 n -= 1
#         return [0] if (adjList == {0: []}) else q


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0: return 0
#         if n == 1 or n == 2: return 1
#         dp = [0] * (n + 1)
#         dp[1] = dp[2] = 1
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#         return dp[n]

# def euler1(n: int) -> int:
#     return filter(lambda x: x % 3 == 0 or x % 5 == 0, 1000)

# def is_special_array(l: list[int]) -> bool:
#     even: list[int] = [l[i] for i in range(0, len(l), 2)]
#     odd: list[int] = [l[i] for i in range(1, len(l), 2)]
#     return all(x % 2 == 0 for x in even) and all(x % 2 != 0 for x in odd)

# asd = [2, 7, 4, 9, 6, 1, 6, 3]
# print(is_special_array(asd))

# from math import gcd
# from functools import reduce

# def is_prim_pyth_triple(l: list[int]) -> bool:
#     l.sort()
#     if l[0] ** 2 + l[1] ** 2 != l[2] ** 2:
#         return False
#     if reduce(gcd, l) != 1:
#         return False
#     return True

# print(is_prim_pyth_triple([4, 5, 3]))
# print(is_prim_pyth_triple([7, 12, 13]))

# def can_find(chars :list[str],  words :list[str]) -> bool:
#     return all(any(char in word for word in words) for char in chars)

# print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
# print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
# print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
# print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))
# print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))


# def euler2(limit: int)-> int:
#     return


# def make_armstrong(start: int, limit: int) -> list[int]:
#     return

# def split_even_odd_sublist(num_list: list[int]) -> tuple[list[int], list[int]]:
#     return
# my_string = "Hello World"
# print([char for char in my_string if char not in "aeiouAEIOU"])

# from string import ascii_lowercase
# class Solution:
#    @staticmethod
#    def longestIdealString(s: str, k: int) -> int:
#        dp = dict.fromkeys(ascii_lowercase, 0)
#        print(type(dp))
#        for c in s:
#            dp[c] = max(dp[d] + 1 for d in dp if abs(ord(c) - ord(d)) <= k)
#        return max(dp.values())
#
# print(Solution.longestIdealString("acfgbd", 2))

# def is_prime(num: int) -> bool:
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def next_prime(n: int) -> int:
#     n += 1
#     while not is_prime(n):
#         n += 1
#     return n

# def prime_sequence(limit: int)-> list[int]:
#     res: list[int] = []
#     for i in range(limit):
#         res.append(next_prime(i))
#     return list(set(res))

# print(prime_sequence(20))

# def repeat_sequence(string: str) -> str:
#    res: str = ""
#    arrow = "->"
#    for i, char in enumerate(list(string)):
#        res += char.upper()
#        res += char.lower() * i
#        if (i != len(string) - 1):
#            res += arrow
#    return res
# print(repeat_sequence("UVWX"))

# def split_even_odd_sublist(num_list: list[int]) -> tuple[list[int], list[int]]:
#     even = list(filter(lambda x: x % 2 == 0, num_list))
#     odd = list(filter(lambda x: x % 2 != 0, num_list))
#     return (even, odd)

# print(split_even_odd_sublist([2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 12, 14, 15, 21]))

# def make_armstrong(start: int, limit: int)-> list[int]:
#    return [num for num in range(start, limit) if num == sum(int(digit) ** len(str(num)) for digit in str(num))]
#
# print(make_armstrong(100, 1000))

# def arm_strong(n: list[int]) -> int:
#     num_digits = len(str(n))
#     return n == sum(int(digit) ** num_digits for digit in str(n))

# def digits(n: int) -> list[int]:
#    return [int(digit) for digit in str(n)]


# def fibonacci_sequence(limit: int):
#    a, b = 0, 1
#    while a <= limit:
#        yield a
#        a, b = b, a + b
#
#
# def euler2(limit: int) -> int:
#    return sum(x for x in fibonacci_sequence(limit) if x % 2 == 0)
#

# def fibonacci(n: int) -> int:
#     if (n == 0):
#         return 0
#     elif (n == 1):
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# from functools import cache
# class Solution:
#   @staticmethod
#   def minFallingPathSum(grid: list[list[int]]) -> int:
#     if (len(grid[0]) == 1) : return grid[0][0]
#     @cache
#     def dfs(i, j):
#       if i == len(grid): return 0
#       if j < 0 or j == len(grid[0]): return float("inf")
#       best = float("inf")
#       for k in range(len(grid[0])):
#         if k != j: best = min(best, dfs(i + 1, k))
#       return grid[i][j] + best
#     res = float("inf")
#     for j in range(len(grid[0])):
#       res = min(res, dfs(0, j))
#     return res

# from typing import List
# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         N = len(grid)
#         DP = grid[0]

#         for i in range(1, N):
#             indx1 = DP.index(min(DP))
#             indx2 = DP.index(min(DP[:indx1] + DP[indx1 + 1 :]))
#             for j in range(N):
#                 if j != indx1:
#                     grid[i][j] += DP[indx1]
#                 else:
#                     grid[i][j] += DP[indx2]
#             DP = grid[i]

#         return min(DP)


# class Solution:
#   def minFallingPathSum(self, grid: list[list[int]]) -> int:
#     if (len(grid[0]) == 1) : return grid[0][0]
#     @cache
#     def dfs(i, j):
#       if i == len(grid): return 0
#       if j < 0 or j == len(grid[0]): return float("inf")
#       best = float("inf")
#       for k in range(len(grid[0])):
#         if k != j: best = min(best, dfs(i + 1, k))
#       return grid[i][j] + best
#     res = float("inf")
#     for j in range(len(grid[0])):
#       res = min(res, dfs(0, j))
#     return res

# from typing import List
# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         N = len(grid)
#         DP = grid[0]

#         for i in range(1, N):
#             indx1 = DP.index(min(DP))
#             indx2 = DP.index(min(DP[:indx1] + DP[indx1 + 1 :]))
#             for j in range(N):
#                 if j != indx1:
#                     grid[i][j] += DP[indx1]
#                 else:
#                     grid[i][j] += DP[indx2]
#             DP = grid[i]

#         return min(DP)

# from functools import cache
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         return (dp := cache(lambda i, j: 0 if i == len(key) else min(min(abs(j - k), len(ring) - abs(j - k)) + dp(i + 1, k) + 1 for k in range(len(ring)) if ring[k] == key[i])))(0, 0)

# from typing import List


# class Solution:
#     def canMakeSquare(self, grid: List[List[str]]) -> bool:
#         R = len(grid)
#         C = len(grid[0])

#         for r in range(R):
#             for c in range(C):
#                 if self.check_2_by_2(grid, r, c, "B"):
#                     return
#                 if self.check_2_by_2(grid, r, c, "W"):
#                     return
#         return True

#     def check_2_by_2(self, grid: List[List[str]], r: int, c: int, color: str) -> bool:
#         return (
#             grid[r][c] == color
#             and grid[r + 1][c] == color
#             and grid[r][c + 1] == color
#             and grid[r + 1][c + 1] == color
#         )


# def canMakeSquare(grid):
#     for i in range(len(grid) - 1):
#         for j in range(len(grid[0]) - 1):
#             square = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
#             if max(square.count("B"), square.count("W")) >= 3:
#                 return True
#     return False


# class Solution:
#     def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
#         res: int = 0
#         for i in range(len(grid) - 1):
#             for j in range(len(grid[0]) - 1):
#                 square = [
#                     grid[i][j],
#                     grid[i][j + 1],
#                     grid[i + 1][j],
#                     grid[i + 1][j + 1],
#                 ]
#                 if square.count(1) == 3:
#                     res += 1
#         return res


# class Solution:
#     def numberOfRightTriangles2(self, grid: List[List[int]]) -> int:
#         R, C = len(grid), len(grid[0])
#         rc = [0] * R
#         cc = [0] * C
#         for r in range(R):
#             for c in range(C):
#                 if grid[r][c] == 1:
#                     rc[r] += 1
#                     cc[c] += 1
#         res: int = 0
#         for r in range(R):
#             for c in range(C):
#                 if grid[r][c] == 1:
#                     res += (rc[r] - 1) * (cc[c] - 1)
#         return res


# class Solution:
#     def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
#         MOD = int(1e9 + 7)
#         dp = [[0] * (one + 1) for _ in range(zero + one + 1)]
#         dp[0][0] = 1
#         for i in range(1, zero + one + 1):
#             dp[i][0] = dp[i - 1][0]
#             if i <= zero:
#                 dp[i][0] = (dp[i][0] + dp[i - 1][0]) % MOD
#             for j in range(1, min(i, one) + 1):
#                 dp[i][j] = dp[i - 1][j]
#                 if i <= zero + j:
#                     dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
#                 if j > limit:
#                     dp[i][j] = (dp[i][j] - dp[i - limit - 1][j - 1]) % MOD
#         return (
#             sum(dp[i][j] for i in range(zero + one + 1) for j in range(1, one + 1))
#             % MOD
#         )


# from functools import cache


# class Solution:
#     def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
#         MOD = 10**9 + 7
#         N = zero + one

#         @cache
#         def go(zero, one, last):
#             if zero == 0 and one == 0:
#                 return 1

#             total = 0
#             if last != 0:
#                 for i in range(1, min(limit + 1, one + 1)):
#                     total += go(zero, one - i, 1)
#                     total %= MOD
#             return total % MOD

#         return go(zero, one, -1)


# from collections import defaultdict


# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph: dict[int, set[int]] = defaultdict(set)
#         for u, v in edges:
#             graph[u].add((v))
#             graph[v].add((u))
#         count: list[int] = [1] * n
#         ans: list[int] = [0] * n

#         @cache
#         def dfs(node: int = 0, parent=None) -> None:
#             for child in graph[node]:
#                 if child != parent:
#                     dfs(child, node)
#                     count[node] += count[child]
#                     ans[node] += ans[child] + count[child]

#         @cache
#         def dfs2(node: int = 0, parent=None) -> None:
#             for child in graph[node]:
#                 if child != parent:
#                     ans[child] = ans[node] - count[child] + n - count[child]
#                     dfs2(child, node)

#         dfs()
#         dfs2()
#         dfs.cache_clear()
#         dfs2.cache_clear()
#         return ans


# class Solution:
#     def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
#         # Base case
#         if nums1 == nums2:
#             return 0
#         nums1.sort()
#         nums2.sort()
#         # Find the difference between the first elements of both arrays
#         res = nums2[0] - nums1[0]
#         for i in range(1, len(nums1)):
#             # If the difference between the elements of both arrays is not the same
#             if nums2[i] - nums1[i] != res:
#                 return 0
#         return res


# from math import inf


# class Solution:
#     def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
#         nums1.sort()
#         nums2.sort()
#         n = len(nums1)
#         ans = inf
#         for i in range(n):
#             # Remove the ith element from both arrays
#             for j in range(i + 1, n):
#                 # Remove the jth element from both arrays
#                 lst = nums1[:]
#                 lst.pop(j)
#                 lst.pop(i)
#                 # Calculate the difference between the elements of both arrays
#                 cur = [-lst[i] + nums2[i] for i in range(n - 2)]
#                 # If the difference between the elements of both arrays is the same
#                 if len(set(cur)) == 1 and cur[0] < ans:
#                     # Update the answer
#                     ans = cur[0]
#         return ans


# from collections import deque


# class Solution:
#     def minEnd(self, n: int, x: int) -> int:
#         # Convert the integer to a binary string
#         bit = list(int(a) for a in "{:060b}".format(x))
#         zeros = deque()
#         # Find the positions of the zeros in the binary string
#         # We're doing it in reverse, and the starting position is 59
#         # because the binary string has a length of 60
#         for i in range(59, -1, -1):
#             # If the bit is 0, add the position to the zeros list
#             if bit[i] == 0:
#                 zeros.append(59 - i)
#         n -= 1
#         ans = x
#         # While there are zeros in the zeros list
#         while n and zeros:
#             # Get the position of the rightmost zero
#             r = n % 2
#             # If the rightmost zero is at the rightmost position
#             add = zeros.popleft()
#             if r:
#                 # Add 2^add to the answer
#                 # << is the left shift operator
#                 # which shifts the bits of the number to the left
#                 ans += 1 << add
#             n = n // 2
#         return ans


# class Solution:
#     def medianOfUniquenessArray(self, nums: List[int]) -> int:
#         n = len(nums)

#         def count(var):
#             right = 0
#             seen = {}  # book keeping

#             answer = 0
#             for left in range(n):
#                 if left > 0:
#                     # remove the left element from the book keeping
#                     x = nums[left - 1]
#                     # decrement the count of the element
#                     seen[x] -= 1
#                     # if the count is 0, remove the element from the book keeping
#                     if seen[x] == 0:
#                         del seen[x]
#                 # add elements to the book keeping
#                 while right < n and len(seen) < var:
#                     x = nums[right]
#                     # increment the count of the element
#                     seen[x] = seen.get(x, 0) + 1
#                     right += 1

#                 if len(seen) == var:
#                     # if the count of the elements is equal to var
#                     answer += n - right + 1

#             return answer

#         ptr_left, ptr_right = 1, n  # two pointer
#         # target value
#         target = (n**2 + n) // 4

#         # binary search
#         while ptr_left != ptr_right:
#             ptr = (ptr_left + ptr_right + 1) // 2

#             if count(ptr) > target:
#                 ptr_left = ptr
#             else:
#                 ptr_right = ptr - 1

#         return ptr_left


# # class Solution:
# from operator import xor
# from functools import reduce


# def minOperations(nums: List[int], k: int) -> int:
#     return (reduce(xor, nums) ^ k).bit_count()


# # def bit_count(self):
# #    return bin(self).count("1")


# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         wonderful = 0
#         seen = defaultdict(int, {0: 1})
#         mask = 0

#         for index, char in enumerate(word):
#             mask ^= 1 << (ord(char) - ord("a"))
#             wonderful += seen[mask]
#             for c in range(10):
#                 wonderful += seen[mask ^ (1 << c)]
#             seen[mask] += 1
#         return wonderful


# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         s1: list[str] = version1.split(".")
#         s2: list[str] = version2.split(".")

#         smol = min(len(s1), len(s2))

#         for i in range(smol):
#             if int(s1[i]) > int(s2[i]):
#                 return 1
#             elif int(s2[i]) > int(s1[i]):
#                 return -1

#         if len(s1) < len(s2):
#             for i in range(len(s1), len(s2)):
#                 if int(s2[i]) != 0:
#                     return -1

#         elif len(s1) > len(s2):
#             for i in range(len(s2), len(s1)):
#                 if int(s1[i]) != 0:
#                     return 1
#         return 0


# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort()
#         ans = 0
#         i, j = 0, len(people) - 1
#         while i <= j:
#             if people[i] + people[j] <= limit:
#                 i += 1
#             j -= 1
#             ans += 1
#         return ans

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#             if not head: return head
#             stack = []
#             curr = head
#             while curr:
#                 while stack and stack[-1].val < curr.val:
#                     stack.pop()
#                 if stack:
#                     stack[-1].next = curr
#                 stack.append(curr)
#                 curr = curr.next

#             return stack[0]

# from collections import Counter
# def is_substring(string: str) -> int:
#     char_index = Counter()
#     longest_length = start = 0
#     for i, char in enumerate(string):
#         if char in char_index and start <= char_index[char]:
#             start = char_index[char] + 1
#         else:
#             longest_length = max(longest_length, i - start + 1)

#         char_index[char] = i
#     return longest_length

# def roman_nums(r: str) -> int:
#     roman: dict = {

#     }
#     total: int = 0
#     for i in range(len(r)):
#         value: int = roman[r[i]]
#         if (i + 1 < len(r) and roman[r[i + 1]] > value):
#             total -= value
#         else:
#             total += value
#     return total

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# from typing import Optional
# class Solution:
#     def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head.val > 4:
#             head = ListNode(0, head)
#         node = head
#         while node:
#             node.val = (node.val * 2) % 10
#             if node.next and node.next.val > 4:
#                 node.val += 1
#             node = node.next
#         return head
# class Dummy:
#     def appendNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head: return head
#         curr = head
#         while curr.next:
#             curr = curr.next

#         curr.next = ListNode(n)
#         return head

# from collections import defaultdict
# from typing import List
# class Solution:
#     @staticmethod
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
#         ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
#             map(str, range(4, len(score) + 1))
#         )

#         res: list[int] = [0] * len(score)
#         for rank, (_, idx) in zip(ranks, sorted_scores):
#             res[idx] = rank


#         return res
# def display_in_reverse_order(*args: str) -> str:
#     res = []
#     for arg in args:
#         res.append(arg[::-1])
#     return "".join(reversed(res))

# def display_in_reverse_order(*arguments: str) -> str:
#     new_word = ""
#     for word in arguments:
#         new_word += word
#     return "".join(reversed(new_word))


# def display_in_reverse_order(*input: tuple[str]) -> str:
#     return reversed("".join(map(lambda x: x, input)))


from typing import List
from collections import deque
# class DSU:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.rank = [0] * n

#     def find(self, x):
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         x_parent = self.find(x)
#         y_parent = self.find(y)
#         if self.rank[x_parent] > self.rank[y_parent]:
#             self.parent[y_parent] = x_parent
#         elif self.rank[x_parent] < self.rank[y_parent]:
#             self.parent[x_parent] = y_parent
#         else:
#             self.parent[x_parent] = y_parent
#             self.rank[y_parent] += 1

#     def detectCycle(self, V, adj):
#         self.parent = [i for i in range(V)]
#         self.rank = [0] * V
#         for i in range(V):
#             self.parent[i] = i
#         for u in range(V):
#             for v in adj[u]:
#                 if u < v:
#                     if self.find(u) == self.find(v):
#                         return True
#                     else:
#                         self.union(u, v)
#         return False


# class DSU:
#     def __init__(self, n):
#         self.p = [-1] * n

#     def find(self, i):
#         if self.p[i] < 0:
#             return i
#         self.p[i] = self.find(self.p[i])
#         return self.p[i]

#     def unite(self, i, j):
#         i, j = self.find(i), self.find(j)
#         if i == j:
#             return i
#         if self.p[i] > self.p[j]:
#             i, j = j, i
#         self.p[i] += self.p[j]
#         self.p[j] = i
#         return i

#     def size(self, i):
#         return -self.p[self.find(i)]

#     def sizes(self):
#         return [-s for s in self.p if s < 0]


# class Solution:
#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         d = [[-1] * m for r in range(n)]
#         q = deque()
#         for r in range(n):
#             for c in range(m):
#                 if grid[r][c]:
#                     d[r][c] = 0
#                     q.append((0, r, c))
#         while len(q):
#             t, r, c = q.popleft()
#             for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#                 if i < 0 or i >= n or j < 0 or j >= m or d[i][j] >= 0:
#                     continue
#                 d[i][j] = t + 1
#                 q.append((t + 1, i, j))
#         v = []
#         for r in range(n):
#             for c in range(m):
#                 for i, j in [(r + 1, c), (r, c + 1)]:
#                     if i >= n or j >= m:
#                         continue
#                     v.append((min(d[r][c], d[i][j]), r * m + c, i * m + j))
#         v.sort(reverse=True)
#         dsu = DSU(n * m)
#         for t, x, y in v:
#             dsu.union(x, y)
#             if dsu.find(0) == dsu.find(n * m - 1):
#                 return t
#         return 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from typing import Optional
# class Solution:
#     def evaluateTree(self, root: Optional[TreeNode]) -> bool:

#     @cache
#     def dfs(self):
#         return None

# class BooleanLogic:
#     def __init__(self, a: bool, b:bool) -> None:
#         self.a = a
#         self.b = b
#         self.bools = {
#             0: False,
#             1: True,
#             2: self.a or self.b,
#             3: self.a and self.b
#         }

# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
#         @cache
#         def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
#             if not node: return None

#             node.left = dfs(node.left)
#             node.right = dfs(node.right)

#             if node.left is None and node.right is None and node.val == target: return None

#             return node

#         return dfs(root)


# class Solution:
#     def distributeCoins(self, root: Optional[TreeNode]) -> int:
#         def go(u):
#             if u is None:
#                 return 0, 0
#             missing = 1
#             moves = 0
#             for v in (u.left, u.right):
#                 v_missing, v_moves = go(v)
#                 missing += v_missing
#                 moves += v_moves
#             missing -= u.val
#             moves += abs(missing)
#             return missing, moves
#         return go(root)[1]

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        return True

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if (len(nums) == 1): return [True]  * len(queries)
        parity = [num % 2 for num in nums]

        results = []
        for query in queries:
            start, end = query
            subarray_parity = set(parity[start:end+1])
            if len(subarray_parity) == end - start + 1:
                results.append(True)
            else:
                results.append(False)

        return results


from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        total_difference = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):

                difference = sum(1 for a, b in zip(str(nums[i]), str(nums[j])) if a != b)
                total_difference += difference
        
        return total_difference


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        deltas = []
        
        for x in nums:
            deltas.append((x ^ k)  -x)
        
        deltas.sort(reverse=True)
        total = sum(nums)
        best = total

        i = 0 
        while (i + 1 < N):
            total += deltas[i] + deltas[i + 1]
            best = max(best, total)
            i += 2
        return best

from functools import reduce
from operator import or_
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << (len(nums) - 1)