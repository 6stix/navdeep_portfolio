"""
This file reads in files of accuracies and creates corresponding line graphs.

Authors(s): 6stix
Data: January 29th, 2019
"""

import matplotlib.pyplot as plot

def main():
  data = ""
  with open("Accuracies.txt", "r") as f:
    data = f.read()
    data = data.split('\n')
    data.pop(-1)
  
  y = []
  for line in data:
    line = line.split()
    print(line)
    y.append(round(float(line[-1]), 3))

  x = []
  for i in range(1, 500):
    x.append(i)

  plot.plot(x, y)
  plot.savefig("AccuraciesUntil500.png")

  data = ""
  with open("MoreAccuracies.txt", "r") as f:
    data = f.read()
    data = data.split('\n')
    data.pop(-1)

  y = []
  for line in data:
    line = line.split()
    y.append(round(float(line[-1]), 3) )

  x = []
  for i in range(1, 7):
    x.append(i*200)

  plot.plot(x, y)
  plot.savefig("AccuraciesThrough500.png")

if __name__ == '__main__':
  main()
