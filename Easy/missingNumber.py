# find the missing number given an array of consecutive numbers from 1 to n

def missingNumber(numbers):
    n = len(numbers)+1
    actualSum = sum(numbers)
    expectedSum = n * (n+1) // 2
    missingDigit = expectedSum - actualSum
    return missingDigit


numbasdfers = [1,2,3,5,4,7]
print(missingNumber(numbasdfers))
