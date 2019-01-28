# for j in range(10):
#     globals()['count_{}'.format(j)] = 0
# print(count_0)
#
# for j in range(10):
#     'count_{}'.format(j) = 0
# print(count_0)

for j in range(10):
    globals()[f"count_{j}"] = 0
print(count_0)

