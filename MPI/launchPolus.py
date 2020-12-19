import itertools
import os

nCpusList = [1, 2, 4, 8, 16, 32, 64]
sizesList = [512, 1024, 1536, 2048, 2560]

os.system("mpixlC -o prog MPI.cpp")

for nCpus in nCpusList:
    for size in sizesList:
        for v in range(3):
            fName = str(nCpus) + "_" + str(size) + "_" + str(v)

            if os.path.exists(fName + ".out") or os.path.exists(fName + ".err"):
                continue

            os.system("mpisubmit.pl -p " + str(nCpus) + " -w 00:15" + \
                      " -stdout " + fName + ".out" + \
                      " -stderr " + fName + ".err" + \
                      " prog -- " + str(size))