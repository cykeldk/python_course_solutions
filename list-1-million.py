import timeit

#first
million_list = list(range(1000000))
print(min(million_list))
print(max(million_list))

timeit.timeit(sum(million_list))

sum = sum(million_list)

#second
gaussian_result = (million_list[0] + million_list[-1]) * (len(million_list)/2)


print('gaussian method result' + str(gaussian_result))


#third


print('the sum is: ' + str(sum))


odds = list(range(1, 20, 2))
for val in odds:
	print(val)

#fourth
multiples_of_3 =[val * 3 for val in range(3, 30)]

print(multiples_of_3)

#fifth
ten_first_cubes = [val ** 3 for val in range(1, 10)]

print(ten_first_cubes)
