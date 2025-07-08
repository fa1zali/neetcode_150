# Determine if a 9x9 sudoku board is valid. Only filled cells need to be validated based on below rules:
# 1. Each row must contain the digits from 1-9 without repetition
# 2. Each column must contain the digits from 1-9 without repetition
# 3. Each of the 9 3x3 subboxes of the grid must contain the digits from 1-9 without repetition

def valid_sudoku(sdk):
    for elm in sdk:
        row_set = set()
        for i in range(9):
            if elm[i] != '':
                if elm[i] not in row_set:
                    row_set.add(elm[i])
                else:
                    return False

    for i in range(9):
        col_set = set()
        for j in range(9):
            if sdk[j][i] != '':
                if sdk[j][i] not in col_set:
                    col_set.add(sdk[j][i])
                else:
                    return False

    box_dict = {i:set() for i in range(9)}

    for i in range(9):
        for j in range(9):
            
            value = sdk[i][j]

            if value == '':
                pass
            else:
                category = int(i/3) * 3 + int(j/3)

                if value not in box_dict[category]:
                    box_dict[category].add(value)
                else:
                    print(box_dict)
                    return False
        
    return True


print(valid_sudoku([[1,2,'','','','','','',''], ['','',3,4,'','','','',''], ['','','','',5,6,'','',''], 
                    ['','','','','','',7,8,''], ['','','','','','','','',9], [3,4,'','','','','','',''],
                    ['','',5,6,'','','','',''], ['','','','',7,8,'','',''], ['','','','','','','','',1]]))