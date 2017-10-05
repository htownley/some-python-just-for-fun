'''
Generating lots of primes
'''

import sys
import numpy as np
import time

def list_of_primes(max_prime):
  big_list = list(range(max_prime + 1))
  limit = int((max_prime + 1) ** 0.5) + 1
  for i in range(0, max_prime + 1, 2):
    big_list[i] = 'X'
  big_list[1] = 'X'

  for i in range(3, max_prime + 1, 2):

    # only need to test numbers up to max^1/2
    if isinstance(big_list[i], int) and big_list[i] > limit:
      break

    # loop through all the primes
    if isinstance(big_list[i], int) and (i**2 < max_prime + 1):

      # Don't need to go through every number between prime and max!
      # just skip by multiples of the prime you're currently testing
      # i.e. big_list[i]
      for j in range(i**2, max_prime + 1, big_list[i]):
        if (isinstance(big_list[j], int)) and (big_list[j] % big_list[i] == 0):
          big_list[j] = 'X'

  result = list(filter(lambda x: isinstance(x, int), big_list))
  result.insert(0, 2)
  return result


def main():
  start_time = time.time()

  args = sys.argv[1:]
  if len(args) != 1:
    print("Usage: max_prime")
    return

  max_prime = int(args[0])
  result = list_of_primes(max_prime)

  for i in range(len(result)):
    print("[{}]: {}".format(i+1, result[i]))

  print("My program took", time.time() - start_time, "seconds to run")
  
if __name__ == '__main__':
  main()
