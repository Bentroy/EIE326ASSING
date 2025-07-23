#
# # def caesar_cipher(text, shift):
# #     result = ""
# #
# #     for char in text:
# #         if char.isalpha():
# #             # Shift within A-Z or a-z
# #             start = ord('A') if char.isupper() else ord('a')
# #             result += chr((ord(char) - start + shift) % 26 + start)
# #         else:
# #             # Leave non-alphabet characters unchanged
# #             result += char
# #
# #     return result
# #
# # # Example usage
# # text = input("Enter text to encrypt: ")
# # shift = int(input("Enter shift amount: "))
# #
# # encrypted = caesar_cipher(text, shift)
# # print(f"Encrypted text: {encrypted}")
#
#
# # matrix = [[1, 2, 3], [4, 5, 6]]
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[i])):
# #         print(matrix[i][j], end=" ")
# # print()
#
#
# def linear_search(arr, key):
#  for i in range(len(arr)):
#  if arr[i] == key:
#  return i
#  return -1
#  arr = [10, 20, 30, 40, 50]
#  key = 30
#  result = linear_search(arr, key)
#  print(f"Element {key} found at index
# {result}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22]
bubble_sort(arr)
print("Sorted array:", arr)
