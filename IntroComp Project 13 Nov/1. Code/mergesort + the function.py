
def mergesort(list_of_items,key):
    list_len = len(list_of_items)
    if list_len < 2:
        return list_of_items
    left_list = list_of_items[:list_len//2]
    right_list = list_of_items[list_len//2:]
    
    left_list = mergesort(left_list,key)
    right_list = mergesort(right_list,key)
    
    result_list = []
    
    while left_list and right_list:
        if left_list[0][key] > right_list[0][key]:
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)
    if left_list:
        result_list.extend(left_list)
    else:
        result_list.extend(right_list)
    return result_list

mouse_pos = (4,55)

def distance_list_by_rank(mouse_pos, NTU_Food):     # Takes in user_coordinates, and NTU_Food. Returns a list of lists again, sorted by rank.
    ranked_distance_list = []
    for i in (sort_distance(mouse_pos,NTU_Food)):
        ranked_distance_list.append([i, (NTU_Food[(i[0])]['Votes'])])
    ranked_distance_list = mergesort(ranked_distance_list,1)            #Mergesort done here just to show that we can, haha
    for j in ranked_distance_list:
        j.pop(-1)
    return ranked_distance_list#[0:10]  #You can slice however you want 