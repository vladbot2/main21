# def compare(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()

#         if lines1 == lines2:
#             print("All rows match.")
#         else:
#             for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
#                 if line1 != line2:
#                     print(f"Row {i} does not match:")
#                     print(f"{file1}: {line1.strip()}")
#                     print(f"{file2}: {line2.strip()}")

# compare('file1.txt', 'file2.txt')

# 3
# def remove(input_file, output_file):
#     with open(input_file, 'r') as f:
#         lines = f.readlines()

#     if lines:
#         lines = lines[:-1] 

#     with open(output_file, 'w') as f:
#         f.writelines(lines)


# remove('input.txt', 'output.txt')

# 4
# def longest(file):
#     with open(file, 'r') as f:
#         lines = f.readlines()

#     length = max(len(line) for line in lines)
#     print(f"Dovzhina of the found row: {length}")

# longest('input.txt')

# 5
# def count(file, word):
#     with open(file, 'r') as f:
#         text = f.read()

#     count = text.count(word)
#     print(f"Quantity of words '{word}': {count}")

# count('input.txt', 'word')

# 6
# def replace(file, old, new):
#     with open(file, 'r') as f:
#         text = f.read()

#     new = text.replace(old, new)

#     with open(file, 'w') as f:
#         f.write(new)

# replace('input.txt', 'old', 'new')
