student_number = int(input("please input student number:")) + 1
final_array=list(range(1, student_number))
while(1):
    if len(final_array) <= 1:
        print("The lucky student is:", final_array[0])
        break
    temp_list = final_array.copy()
    for i in range(0,len(temp_list)):
        if i%2 ==0:
            final_array.remove(temp_list[i])
