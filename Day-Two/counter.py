def counter(start_value, end_value):
  """Returns the number of numbers from start_value to end_value, inclusive."""
  counter = 0
  for i in range(start_value, end_value + 1):
    counter += 1
  return counter

def main():
  print(counter(1, 10))

if __name__ == "__main__":
  main()
