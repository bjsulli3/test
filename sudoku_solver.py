# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:29:34 2020

@author: bjsul
"""

import pandas as pd
import numpy as np
import random

index = [11, 12, 13, 21, 22, 23, 31, 32, 33]
allMoves = set(range(1, 10))

grid = np.array([[0, 0, 0, 6, 0, 7, 0, 9, 0],
                 [8, 1, 6, 9, 0, 0, 7, 5, 2],
                 [7, 0, 0, 2, 0, 0, 1, 0, 0],
                 [0, 6, 0, 0, 0, 0, 8, 0, 5],
                 [3, 0, 0, 5, 0, 4, 0, 0, 9],
                 [9, 0, 2, 0, 0, 0, 0, 6, 0],
                 [0, 0, 7, 0, 0, 2, 0, 0, 4],
                 [5, 8, 1, 0, 0, 6, 9, 2, 7],
                 [0, 2, 0, 8, 0, 5, 0, 0, 0]
                 ])

grid = np.array([[0, 7, 0, 9, 5, 0, 0, 0, 0],
                 [0, 0, 5, 0, 0, 8, 4, 0, 0],
                 [9, 0, 0, 0, 0, 3, 0, 7, 1],
                 [0, 3, 0, 0, 0, 9, 0, 0, 4],
                 [0, 1, 0, 0, 2, 0, 0, 9, 0],
                 [4, 0, 0, 5, 0, 0, 0, 1, 0],
                 [7, 4, 0, 8, 0, 2, 0, 0, 3],
                 [0, 0, 1, 6, 0, 0, 7, 0, 0],
                 [0, 0, 0, 0, 1, 7, 0, 2, 0]
                 ])

ogGrid = pd.DataFrame(grid, index=index, columns=index, dtype='int')


def boxSelect(row, column):
    
#### Define the boxRows ####
    if row == 11 or row == 12 or row == 13:
        boxRow = range(0, 3)
        
    elif row == 21 or row == 22 or row == 23:
        boxRow = range(3, 6)
                    
    elif row == 31 or row == 32 or row == 33:
        boxRow = range(6, 9)
                    
#### Define the boxColumns ####
    if column == 11 or column == 12 or column == 13:
        boxCol = range(0, 3)
                    
    elif column == 21 or column == 22 or column == 23:
        boxCol = range(3, 6)
                        
    elif column == 31 or column == 32 or column == 33:
        boxCol = range(6, 9)
    
    return boxRow, boxCol

def checkRowColConditions(row, column, allMoves, updatedGrid):
    rowVals = set(updatedGrid.loc[row, :])
    if 0 in rowVals:
        rowVals.remove(0)
                        
    colVals = set(updatedGrid.loc[:, column])
    if 0 in colVals:
        colVals.remove(0)
                    
    #### Define the boxRows ####
    boxRow, boxCol = boxSelect(row, column)
                    
    boxVals = set(pd.unique(updatedGrid.iloc[boxRow, boxCol].values.ravel()))
    if 0 in boxVals:
        boxVals.remove(0)
                    
    possibleMoves = allMoves - rowVals - colVals - boxVals
    
    return possibleMoves
    
def solve(originalGrid):
    updatedGrid = originalGrid
    move = True
    #lastTryrow, lastTrycol = 0, 0
    
    i = 0
    while 0 in updatedGrid.values and move == True:
        i += 1
        #print(i)
        
        tryAgain = False
        move = False
        
        for row in index:
            for column in index:
                if updatedGrid.loc[row, column] == 0:
                    
                    possibleMoves = checkRowColConditions(row, column, allMoves, updatedGrid)
                    
                    if len(possibleMoves) == 1:
                        #print(True, row, column)
                        move = True
                        updatedGrid.loc[row, column] = possibleMoves
                    
                    #else:
                        #print(possibleMoves, row, column)

        if 0 in updatedGrid.values and move == False:
            for row in index:
                
                if tryAgain == True:
                    break
                
                for column in index:
                    
                    if tryAgain == True:
                        break
                    
                    if updatedGrid.loc[row, column] == 0:
                        
                        possibleMoves = checkRowColConditions(row, column, allMoves, updatedGrid)
                        
                        rowExclusions = updatedGrid.loc[row, :] == 0
                        
                        for indexRow in np.array(index)[rowExclusions]:
                            possibleMovesRow = checkRowColConditions(row, indexRow, possibleMoves, updatedGrid)
                            
                            if len(possibleMovesRow) == 1:
                                if len(possibleMoves - possibleMovesRow) == 1:
                                    move = True
                                    updatedGrid.loc[row, column] = possibleMoves - possibleMovesRow
                            
                        colExclusions = updatedGrid.loc[:, column] == 0
                        
                        for indexCol in np.array(index)[colExclusions]:
                            possibleMovesCol = checkRowColConditions(indexCol, column, possibleMoves, updatedGrid)
                            
                            if len(possibleMovesCol) == 1:
                                if len(possibleMoves - possibleMovesCol) == 1:
                                    move = True
                                    updatedGrid.loc[row, column] = possibleMoves - possibleMovesCol
                                

                        possibleMoves = checkRowColConditions(row, column, allMoves, updatedGrid)
                        
                        if len(possibleMoves) == 1:
                            move = True
                            updatedGrid.loc[row, column] = possibleMoves
                            tryAgain = True
                        
                        if tryAgain == True:
                            break
                        
                        else:
                            boxRow, boxCol = boxSelect(row, column)
                            for boxRowIndex in boxRow:
                                for boxColIndex in boxCol:
                                    if updatedGrid.iloc[boxRowIndex, boxColIndex] == 0:
                                        rowName = updatedGrid.iloc[boxRowIndex, :].name
                                        colName = updatedGrid.iloc[:, boxColIndex].name
                                        possibleMovesBox = checkRowColConditions(rowName, colName, possibleMoves, updatedGrid)
                                        if len(possibleMovesBox) == 1:
                                            if len(possibleMoves - possibleMovesBox) == 1:
                                                move = True
                                                updatedGrid.loc[row, column] = possibleMoves - possibleMovesBox
                            
    
    if 0 in updatedGrid.values and move == False:
        print("Cannot complete: " + str(i) + " iterations taken")
    
    else:
        print(str(i) + " iterations taken")
    
    return updatedGrid

test = solve(ogGrid)


# =============================================================================
# 
#   if 0 in updatedGrid.values and move == False:
#             origGrid = updatedGrid
#             newGrid = updatedGrid
#             tryAgain = 0
#             
#             for row in index:
#                 if tryAgain == 1:
#                     break
#                 
#                 for column in index:
#                     if tryAgain == 1:
#                         break
#                     
#                     if (row == lastTryrow) and (column == lastTrycol):
#                         None
#                     
#                     else:
#                         if updatedGrid.loc[row, column] == 0:
#                             
#                             rowVals = set(newGrid.loc[row, :])
#                             if 0 in rowVals:
#                                 rowVals.remove(0)
#                             
#                             colVals = set(newGrid.loc[:, column])
#                             if 0 in colVals:
#                                 colVals.remove(0)
#                         
#                             #### Define the boxRows ####
#                             boxRow, boxCol = boxSelect(row, column)
#                         
#                             boxVals = set(pd.unique(newGrid.iloc[boxRow, boxCol].values.ravel()))
#                             if 0 in boxVals:
#                                 boxVals.remove(0)
#                         
#                             possibleMoves = allMoves - rowVals - colVals - boxVals
#                             
#                             if len(possibleMoves) == 2:
#                                 move = True
#                                 newGrid.loc[row, column] = random.sample(possibleMoves, 1)[0]
#                                 print(row, column)
#                                 tryAgain = 1
#                                 updatedGrid = newGrid
#                                 lastTryrow, lastTrycol = row, column
#                                 
#                             else:
#                                 move = False
#                                 tryAgain = 0
#                 
#         if 0 in updatedGrid.values and move == False:
#             updatedGrid = origGrid
#             move = True
# 
# =============================================================================
