output = []

output.append([1,2,3])
output.append([4,5,6])
output.append([7,8,9])
print(output)
#output=[[1,2,3],[4,5,6],[7,8,9]]
test_x = []
test_x.append([output])
print(test_x)
#test_x=[[[1,2,3],[4,5,6],[7,8,9]]]
test_word = []
test_pos1 = []
test_pos2 = []
for i in range(len(test_x)):
    word = []
    pos1 = []
    pos2 = []
    #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for j in test_x[i]:
        #[1, 2, 3], [4, 5, 6], [7, 8, 9]中的每一个
        temp_word = []
        temp_pos1 = []
        temp_pos2 = []
        for k in j:
            temp_word.append(k[0])
            temp_pos1.append(k[1])
            temp_pos2.append(k[2])
        print(temp_word)
        print(temp_pos1)
        print(temp_pos2)
        word.append(temp_word)
        pos1.append(temp_pos1)
        pos2.append(temp_pos2)
    test_word.append(word)
    test_pos1.append(pos1)
    test_pos2.append(pos2)