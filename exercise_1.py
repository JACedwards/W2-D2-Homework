def under_10_list(input_list):
    output_list = []
    for num in input_list:
        if num < 10:
            output_list.append(num)
        else:
            continue
    print(output_list)

under_10_list([1,11,14,5,8,9])

