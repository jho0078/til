import sys
sys.stdin = open("덧셈(Plus).txt")

def inspect():
    global result

    for i in range(len(S)-1):
        two_sum = int(S[:i+1]) + int(S[i+1:])
        print(S[:i+1], S[i+1:])
        if two_sum == int(result):
            return f'{str(int(S[:i+1]))}+{str(int(S[i+1:]))}={result}'

    return 'NONE'

S, result = input().split()

print(inspect())

