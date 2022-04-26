
# Assumptions:
#   Duplicates should be elimnated
#   End product should be list, not set

def input_lists(l_1, l_2):
    
    merged_list = l_1 + l_2
    merged_list.sort()
    merged_noreapt = set(merged_list)
    final = list(merged_noreapt)
    print(final)

input_lists([1,2,3,4,5,6], [3,4,5,6,7,8,10])
