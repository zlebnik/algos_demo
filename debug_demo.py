# data = [
#     [1, 'sonnen@yahoo.com'],
#     [2, 'retoh@outlook.com'],
#     [3, 'sonnen@yahoo.com'],
#     [4, 'retoh@outlook.com'],
#     [5, 'retoh@outlook.com'],
# ]
#
# sorted_list = sorted(
#     data,
#     key=lambda x: x[1],
#     reverse=True
# )
# check = set()
#
# for student in sorted_list:
#     if student[1] in check:
#         sorted_list.remove(student)
#     else:
#         check.add(student[1])
#
# print(*sorted_list, sep='\n')
# print(*check, sep='\n')

def add_ten(data={}):
    if data is None:
        data = []
    data.append(10)
    return data

print(add_ten())
print(add_ten())
print(add_ten())
