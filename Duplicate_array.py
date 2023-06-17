arr=[0,0,1,1,1,2,2,3,3,4]
def duplicate_array(duplicate):
    no_duplicate_arr=[]
    for element in duplicate:
        if element not in no_duplicate_arr:
            no_duplicate_arr.append(element)
            s = len(no_duplicate_arr)
    # return s
    return no_duplicate_arr    
print(duplicate_array(arr))

    