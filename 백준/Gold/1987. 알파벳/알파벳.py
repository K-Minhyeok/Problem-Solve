import sys
input= sys.stdin.readline
MAX = -1

def search(i,j,cnt,alphabet):
    global MAX
    MAX = max(cnt,MAX)
    for wi,wj in wij:
        ni,nj = i+wi,j+wj
        if 0<=ni<R and 0<=nj<C and not alphabet[ord(l[ni][nj]) -ord('A')]  :
            alphabet[ord(l[ni][nj]) -ord('A')] = 1
            search(ni,nj,cnt+1,alphabet)
            alphabet[ord(l[ni][nj]) -ord('A')] = 0
            # print("used ",ni,nj,l[ni][nj],i,j)


R,C = map(int,input().split())
l = [input().strip() for _ in range(R)]
wij = [(1,0),(0,1),(-1,0),(0,-1)]
alphabet = [0]*26
alphabet[ord(l[0][0]) - ord('A')] = 1
search(0,0,1,alphabet)
print(MAX)