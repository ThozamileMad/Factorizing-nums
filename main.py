num = int(input("Enter number: "))
solution = 2 
index_num = 0 
run = True
lst = [num + 1 for num in range(num)][2:] 
while run: 
    lst_value = lst[index_num] 
    solution *= lst_value 
    index_num += 1
    
    if len(lst) == index_num:
        print(solution)
        run = False
