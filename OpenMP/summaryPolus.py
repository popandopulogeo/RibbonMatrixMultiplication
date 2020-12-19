from glob import glob

stats = {}
files = glob("*.out")

for file in files:
	cur_file = open(file)
	stat = float(cur_file.readlines()[-7])
	ncpus, size, ver = file.split('_')

	if stats.get((ncpus, size)) == None:
		stats[(ncpus, size)] = [stat]
	else:
		stats[(ncpus, size)].append(stat)

results = open('results', 'w')

for pair in stats.keys():
	results.write(str(pair[0])+ ',' +str(pair[1]) + ',' + str(sum(stats[pair])/3) + '\n')

