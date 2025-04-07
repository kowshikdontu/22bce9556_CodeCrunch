def nextstate(board):
    newboard = [i+[] for i in board]
    n = len(board)
    m = len(board[0])
    dir =[(0,1),(-1,0),(0,-1),(-1,-1),(-1,1)]
    below_dir =[(1,-1),(1,1),(1,0)]
    for i in range(n):
        for j in range(m):
            live1=0
            live2 =0
            for k in dir:
                new_i=i+k[0]
                new_j = j+k[1]
                if 0<=new_i<n and 0<=new_j<m and board[new_i][new_j]:
                    live1+=1
            for k in below_dir:
                new_i = i + k[0]
                new_j = j + k[1]
                if 0 <= new_i < n and 0 <= new_j < m and board[new_i][new_j]==1:
                    live2 += 1
            total = live1+live2
            # print(live1, live2, total,i,j)
            if board[i][j]:
                if  total<2 or total>3:
                    newboard[i][j]=0
                else:
                    newboard[i][j]=1
            else:
                if total==3:
                    newboard[i][j]=1
                else:
                    newboard[i][j]=0
            # for p in newboard:
            #     print(*p)
            # print()
    for i in range(n):
        for j in range(m):
            board[i][j]=newboard[i][j]
row = int(input())
col = int(input())
board =[]
for i in range(row):
    board.append([int(i) for i in input().split()])
nextstate(board)

for j in board:
    print(*j)
