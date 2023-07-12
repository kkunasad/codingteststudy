maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

# 동 서 남 북
moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def move_cal(curr_pos, moves, maps, curr_value):
    if (curr_pos[0] == len(maps[0])) and (curr_pos[1] == len(maps[1])):
        return curr_value
    
    for m in moves:
        new_pos = [curr_pos[0] + m[0], curr_pos[1] + m[1]]
        print(new_pos)    
        if (new_pos[0] >= 1) and (new_pos[0] <= 5) and (new_pos[1] >= 1) and (new_pos[1] <= 5):        
            if maps[new_pos[0]-1][new_pos[1]-1] == 0:
                return
            move_cal(new_pos, moves, maps, curr_value+1)
            
print(move_cal([1, 1], moves, maps, 0))
