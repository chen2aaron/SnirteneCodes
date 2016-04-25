import heapq

a = [2, 4, 5, 6]
b = [1, 3, 55, 100]

print(list(heapq.merge(a, b)))
# with open('sorted_file_1', 'rt') as file1, open('sorted_file_2', 'rt') as file2, open('merged_file', 'wt') as outf:
#     for line in heapq.merge(file1, file2):
#         outf.write(line)
