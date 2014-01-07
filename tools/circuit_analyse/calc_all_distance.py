import os, re, sys
import itertools
import Distance

files = set(file for file in list(os.listdir('.')) if re.match(r'.*\.log', file))

for f1,f2 in itertools.combinations(files, 2):
    distance_obj = Distance.Distance()
    distance_obj.parse_logfile(f1, f2)
    print(f1, f2, distance_obj.calc_score())
    sys.stdout.flush()


