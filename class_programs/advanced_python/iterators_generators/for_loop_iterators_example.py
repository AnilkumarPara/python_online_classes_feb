nums = [1,2,3,4]
# for num in nums:
#     print(num)
# print(dir(nums))

# num_obj = nums.__iter__()
num_obj = iter(nums)
# # print(num_obj)
# # print(dir(num_obj))
# print(next(num_obj))
# print(next(num_obj))
# print(next(num_obj))
# print(next(num_obj))
# print(next(num_obj))

while True:
    try:
        next(num_obj)
    except StopIteration:
        break
for num in nums:
    print(num)














