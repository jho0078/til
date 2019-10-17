
R, C = map(int, input().split())
lake = [list(input()) for i in range(R)]
swanQ = []
waterQ = []

for r in range(R):
    for c in range(C):
        if lake[r][c] == ".":
            waterQ.append((r, c))

        elif lake[r][c] == "L":
            waterQ.append((r, c))
            swanQ.append()
