# a = [[]]*3
# b = a.pop()
# b.append(42)
# print(a)
# print(b)
# a = 0
# default_val = 10
# x = 5
#
# if a:
#     val = default_val
# else:
#     val = x
# # print(val)


# def make_dict(keys, values):
#     result = {}
#     for i, key in enumerate(keys):
#         if i < len(values):
#             result[key] = values[i]
#         else:
#             result[key] = None
#     return result
#
#
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# result = make_dict(keys, values)
# print(result)

# sentence = 'i want to be a python developer'
# print(sentence [5])

# words = 'i want to be a python developer'.split(" ")
# print(sentence[7])

# #text = "Winter is coming"
#
# words = text.split()
#
# print(words)
# def combine_lists(list1, list2):
#     return list(zip(list1, list2 + ["N/A"] * (len(list1) - len(list2)))) if len(list1) > len(list2) else list(
#         zip(list1 + ["N/A"] * (len(list2) - len(list1)), list2))
#
#
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c']
#
# result = combine_lists(list1, list2)
# print(result)
# import re
#
#
# class WordCounter:
#     def __init__(self):
#         self.word_count = {}
#
#     def load_file(self, filename):
#
#         try:
#             with open(filename, 'r') as file:
#                 text = file.read()
#                 words = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', text)
#                 for word in words:
#                     word_lower = word.lower()
#                     if word_lower in self.word_count:
#                         self.word_count[word_lower] += 1
#                     else:
#                         self.word_count[word_lower] = 1
#             print(f"Loaded words from file '{filename}'")
#         except FileNotFoundError:
#             print(f"Error: File '{filename}' not found.")
#
#     def get_word_count(self, word):
#
#         word_lower = word.lower()
#         return self.word_count.get(word_lower, 0)
#
#     def clear_memory(self):
#
#         self.word_count = {}
#         print("Memory cleared.")
#
#
# def main():
#     word_counter = WordCounter()
#     while True:
#         command = input("Enter a command (load, wordcount, clear-memory, exit): ")
#         if command.startswith("load "):
#             filename = command[5:]
#             word_counter.load_file(filename)
#         elif command.startswith("wordcount "):
#             word = command[10:]
#             count = word_counter.get_word_count(word)
#             print(f"The word '{word}' was found {count} times.")
#         elif command == "clear-memory":
#             word_counter.clear_memory()
#         elif command == "exit":
#             break
#         else:
#             print("Invalid command. Try again.")
#
#
# if __name__ == '__main__':
#     main()
