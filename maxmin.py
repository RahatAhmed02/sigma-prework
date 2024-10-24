test_array = [24, 5, 23, -8, 90, 14]


def max_min_array(array):
    max_value = float("-inf")
    min_value = float("inf")

    for i in array:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    return [min_value, max_value]


print(f"The default test array is: {test_array}.")
print("Minimum and maximum values are: ")
print(max_min_array(test_array))
