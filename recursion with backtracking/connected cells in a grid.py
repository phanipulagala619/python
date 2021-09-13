

def cellcounter(grid,i,j,maxcount,a,a1):
    count=1
    grid[i][j]=0
    directions=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    if (i>a or j>a):
        return 0
    for k in range(0,8):
        newi=i+directions[k][0]
        newj=j+directions[k][1]
        if (newi>=0 and newj>=0 and newi<a and newj<a1):
            if (grid[newi][newj])==1:
                count+=cellcounter(grid,newi,newj,maxcount,a,a1)
    if count>maxcount:
        maxcount=count

    return maxcount


count=0
maxcount=0
arr=[]
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(grid)
a=len(grid)
a1=len(grid[0])
print(a)
print(a1)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (grid[i][j]==1):
            c=cellcounter(grid,i,j,maxcount,a,a1)
            arr.append(c)

print(arr)
print(max(arr))
