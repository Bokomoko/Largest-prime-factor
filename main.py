def largestPrimeFactor(number):
  divisor = 2
  largest = 1
  while number > 1 :
    if (number % divisor ) : # not a divisor
        divisor += 1
    else:
      largest = divisor
      number = number / divisor
  return largest


print(largestPrimeFactor(2))
print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))

