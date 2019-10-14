def solve(s, curSum, numbers, target):
    if s == len(numbers):
        return curSum == target
    return solve(s + 1, curSum + numbers[s], numbers, target) + solve(s + 1, curSum - numbers[s], numbers, target)


def solution(numbers, target):
    return solve(0, 0, numbers, target)