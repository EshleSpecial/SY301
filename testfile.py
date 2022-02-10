from sylist import *
import time

csv = open("benchmarks.csv", "w")
csv.write(",10000,20000,30000,40000,50000,60000,70000,80000,90000,100000\n")

print("Benchmarking append...")
csv.write("Append,")
for i in range(10000, 110000, 10000):
  print("Trying for n = " + str(i))
  l = SYList()

  start = time.time()
  for j in range(i):
    l.append(j)
  end = time.time()

  diff = end-start
  csv.write(str(diff / float(i)) + ",")
csv.write("\n")

print("Benchmarking append5...")
csv.write("Append5,")
for i in range(10000, 110000, 10000):
  print("Trying for n = " + str(i))
  l = SYList()

  start = time.time()
  for j in range(i):
    l.append5(j)
  end = time.time()

  diff = end-start
  csv.write(str(diff / float(i)) + ",")
csv.write("\n")

csv.write("AppendDouble,")
print("Benchmarking appendDouble...")
for i in range(10000, 110000, 10000):
  print("Trying for n = " + str(i))
  l = SYList()

  start = time.time()
  for j in range(i):
    l.appendDouble(j)
  end = time.time()

  diff = end-start
  csv.write(str(diff / float(i)) + ",")
csv.write("\n")

csv.write("ListAppend,")
print("Benchmarking appendDouble...")
for i in range(10000, 110000, 10000):
  print("Trying for n = " + str(i))
  l = []

  start = time.time()
  for j in range(i):
    l.append(j)
  end = time.time()

  diff = end-start
  csv.write(str(diff / float(i)) + ",")
csv.write("\n")

csv.close()