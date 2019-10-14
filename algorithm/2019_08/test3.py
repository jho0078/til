import re

def solution(emails):
    count = 0
    p = re.compile('^[a-z+.]+@[a-z]+\.[com|net|org]+$')
    for i in range(len(emails)):
        if p.match(emails[i]):
            count += 1

    return count

emails = ["c@.com"]
print(solution(emails))