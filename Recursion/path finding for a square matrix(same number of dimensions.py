def path_finder(Matrix,position,N):
    if position ==(N-1,N-1):
        return [(position[0],position[1])]


    x,y=position
    if x+1 <N and Matrix[x+1][y]==1:
        a=path_finder(Matrix,(x+1,y),N)
        if a!=None:
            return [(x,y)]+a

    if y+1<N and Matrix[x][y+1]==1:
        b=path_finder(Matrix,(x,y+1),N)
        if b!=None:
            return [(x,y)]+b


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

print(path_finder(grid, (0, 0), n))
