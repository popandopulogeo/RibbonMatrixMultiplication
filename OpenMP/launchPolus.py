import itertools
import os

nThreadsList = [1, 2, 4]
sizesList = [512, 1024, 1536, 2048, 2560]

os.system("xlc++_r -qsmp=omp -o prog OpenMP.cpp")

for nThreads in nThreadsList:
    for size in sizesList:
        for v in range(3):
            fName = str(nThreads) + "_" + str(size) + "_" + str(v)

            if os.path.exists(fName + ".out") or os.path.exists(fName + ".err"):
                continue

            os.system("mpisubmit.pl -t " + str(nThreads) + " -w 00:15" + \
                      " -stdout " + fName + ".out" + \
                      " -stderr " + fName + ".err" + \
                      " prog -- " + str(size) + " " + str(nThreads))