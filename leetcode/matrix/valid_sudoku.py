#!/usr/bin/env python
# coding: utf-8

# In[95]:


from typing import List


# In[93]:


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row and column
        for i in range(9): # hardcode since its sudoku
            row_check_range = []
            for j in range(9):
                cell = board[i][j]
                if cell != ".": 
                    cell_int = int(cell) # cast
                    if cell_int not in row_check_range:
                        row_check_range.append(cell_int)
                    else:
                        return False
        for j in range(9):
            col_check_range = [] 
            for i in range(9):
                cell = board[i][j]
                if cell != ".": 
                    cell_int = int(cell) # cast
                    if cell_int not in col_check_range:
                        col_check_range.append(cell_int)
                    else:
                        return False
        
        row_offset = 0
        col_offset = 0
        while col_offset <=6:
            sub_box_range = []
            out_str = ''
            for i in range(3):
                for j in range(3):
                    cell = board[row_offset+i][col_offset+j]
                    out_str += cell + " "
                    if cell != ".":
                        cell_int = int(cell)
                        if cell_int not in sub_box_range:
                            sub_box_range.append(cell_int)
                        else:
                            return False
                out_str += "\n"
            #print(out_str)
            #print('-------')
            if row_offset +3 >=9: 
                col_offset +=3
                row_offset = 0
            else:
                row_offset +=3
        return True