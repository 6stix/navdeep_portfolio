"""
This program implements the K-Nearest Neighbors algorithm. It takes in no input
and uses the supplied training data for the tests.

Author: 6stix
Data: January 28th, 2019
"""

import numpy as np
from math import sqrt
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plot

def main():
  """
  Implements K-Nearest Neighbors.
  """

  # Initialize a k value and load training and testing data.
  # The shape of both numpy matrices corresponds to: (number of data points,
  #                                               number of pixels plus one)
  k = 7
  # The shape corresponds to: (number of data points, number of pixels plus one)
  train_data = np.loadtxt(--removed_ARCHETYPE--)
  test_data = np.loadtxt(--removed_ARCHETYPE--)
  
  # Filter data.
  train_data, test_data = filter(train_data, test_data)

  # Run classification on test_data set.
  accuracy(train_data, test_data, k)

def multiple_accuracies(train_data, test_data):
  """
  This function checks accuracies for numerous values of k.
  These accuracies get plotted using Matplotlib.
  """
  x = []
  rangeK = 7
  for i in range(1, rangeK):
    x.append(i * 200)

  y = []
  for i in range(1, rangeK):
    accKNN = accuracy(train_data, test_data, i*200)
    y.append(accKNN)

    with open("MoreAccuracies.txt", "a") as f:
      f.write(str(i*200) + "'s value is: " + str(accKNN) + "\n")

  plot.plot(x, y)
  plot.savefig("coolGraph.png")
  
def test_sklearn(train_data, test_data):
  """
  This function tests Sci-Kit Learn's implementation of K-Nearest
  Neighbors.
  """
  xTrain = []
  yTrain = []
  for dpoint in train_data:
    yTrain.append(dpoint[0])
    xTrain.append(dpoint[1:])

  xTrain = np.array(xTrain)
  yTrain = np.array(yTrain)

  xT = []
  yT = []
  for dp in test_data:
    yT.append(dp[0])
    xT.append(dp[1:])

  xT = np.array(xT)
  yT = np.array(yT)

  neigh = KNeighborsClassifier(n_neighbors=k)
  neigh.fit(xTrain, yTrain)
  
  acc = neigh.score(xT, yT)
  print("sklearn's accuracy:", acc)

def accuracy(train_data, test_data, k):
  """
  Determine the accuracy of our K-Nearest Neighbors algorithm.
  For each test point, determine the K-Nearest Neighbors and calculate the
  number of neighbors with matching labels.
  """
  
  correct = 0
  for testPoint in test_data:
    kNearest = classification(train_data, testPoint, k)
    
    kCheck = int(testPoint[0])
    kCorrectCount = 0
    for i in range(k):
      if kNearest[i] == kCheck:
        kCorrectCount += 1

    kAccuracy = kCorrectCount / k

    if kAccuracy >= 0.5:
      correct += 1
  
  total = test_data.shape[0]
  print("Correctness:", correct, total, correct/total, "%")

  # debug(test_data) -> originally used for debugging  
  return correct/total
  
def classification(train_data, dataPoint, k):
  """
  Calls the distance function on each of the data points in the training data
  and appends the k smallest values.
  """
  distances = []
  for trainingExample in train_data:
    d = distance(trainingExample, dataPoint)
    distances.append((d, int(trainingExample[0])))
  
  distances.sort()

  kNearest = []
  if k < len(train_data):
    for i in range(k):
      kNearest.append(distances[i][1])
  
  else:
    print("Error. Bad value for k entered.")
    print("Length of training data:", len(train_data))
    exit()

  return kNearest

def filter(train_data, test_data):
  """
  Filters training and testing data by removing data points that are not 2 and
  3. Labels marked as "2" are changed to zeroes and points marked as "3" are
  changed to ones.
  """
  train_data = train_data.copy()
  test_data = test_data.copy()

  numTrainingPoints = train_data.shape[0]
  
  # ind iterates through the number of data points and i keeps track of the
  # indexing as the array gets modified.
  i = 0
  ind = 0
  while ind < numTrainingPoints:
    if int(train_data[i][0]) != 2 and int(train_data[i][0]) != 3:
      train_data = np.delete(train_data, i, 0)

      i -= 1
    
    elif int(train_data[i][0]) == 2:
      train_data[i][0] = 0

    elif int(train_data[i][0]) == 3:
      train_data[i][0] = 1

    else:
      print("Error with filtering the training data.")
      exit()

    i += 1
    ind += 1

  numTestPoints = test_data.shape[0]
  i = 0
  ind = 0
  while ind < numTestPoints:
    if int(test_data[i][0]) != 2 and int(test_data[i][0]) != 3:
      test_data = np.delete(test_data, i, 0)

      i -= 1

    elif int(test_data[i][0]) == 2:
      test_data[i][0] = 0

    elif int(test_data[i][0]) == 3:
      test_data[i][0] = 1

    else:
      print("Error with filtering the test data.")
      exit()

    i += 1
    ind += 1
  
  return train_data, test_data
  

def distance(example1, example2):
  """
  Calculates distance from one example data point to another.
  """
  example1 = example1[1:]
  example2 = example2[1:]

  inRootTerm = 0
  for i in range(len(example1)):
    powTerm = (example1[i] - example2[i]) ** 2
    inRootTerm += powTerm
  
  return sqrt(inRootTerm)

def debug(test_data):
  """
  This code here was originally used to help debug the filtering of the data.
  """

  print("checking test data...")
  twos = 0
  threes = 0
  for point in test_data:
    if point[0] == 0:
      twos += 1
    else:
      threes += 1

  print("numtwos threes:", twos, threes)

  twos = 0
  threes = 0
  for pick in train_data:
    if pick[0] == 0:
      twos += 1
    else:
      threes += 1

  print(twos, threes)
  

if __name__ == '__main__':
  main()
