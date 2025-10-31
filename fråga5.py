# Second best is not first place!


def second_smallest_and_largest(num_list):
    unique_list = []
    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)

    unique_list.sort()

    if len(unique_list) == 1:
        return f"({unique_list[0]}, {unique_list[0]})"

    elif len(unique_list) == 2:
        return f"({unique_list[0]}, {unique_list[1]})"

    elif len(unique_list) == 0:
        return None

    else:
        return f"({unique_list[1]}, {unique_list[-2]})"



print(second_smallest_and_largest([2,2,2,4,6,-1]))
print(second_smallest_and_largest([-1,-1]))
print(second_smallest_and_largest([]))
print(second_smallest_and_largest([3]))
