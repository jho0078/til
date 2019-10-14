def solution(drum):
    count = 0
    for i in range(len(drum)):
        x = i
        y = 0
        star_cnt = 0
        while 1:
            if y == len(drum):
                count += 1
                break

            if drum[y][x] == '#':
                y += 1
            elif drum[y][x] == '>':
                x += 1
            elif drum[y][x] == '>':
                x -= 1
            else:
                if star_cnt == 0:
                    y += 1
                    star_cnt += 1
                else:
                    break
    return count

drum = ["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
print(solution(drum))