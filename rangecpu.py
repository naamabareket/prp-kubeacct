import requests
import pickle

#dict_ = requests.get("https://prometheus.nautilus.optiputer.net/api/v1/query_range?query=container_cpu_usage_seconds_total&start=2019-07-17T11:20:00.781Z&end=2019-07-17T11:25:00.781Z&step=1m").json()
dict = pickle.load(open("save.p", "rb"))
values = []
namespace = []
name_n_val = []
#dict = dict_["data"]["result"]
total_network = []
namespace = []


for i in range(len(dict)):
    values = dict[i].get("values")
    namespace.append(dict[i].get("metric").get("namespace"))
    start = float(values[0][1])
    j = 0
    differences = []
    while j < len(values)-2:
        while float(values[j][1]) <= float(values[j+1][1]) and j < len(values)-2:
            j += 1
        end = float(values[j][1])
        difference = end - start
        differences.append(difference)
        start = float(values[j+1][1])
        j += 1
    total_network.append(sum(differences))

print(total_network)


x, y = 0, 1
pairs = []
already_used = []
for x in range(len(namespace)):
    if namespace[x] not in already_used:
        if namespace[x] != None:
            already_used.append(namespace[x])
            name_tot = total_network[x]
            for y in range(len(namespace)):
                if (namespace[x] == namespace[y]) and (x != y):
                    name_tot += total_network[y]
            pairs.append((namespace[x], name_tot))

i = 0
while i < len(pairs):
    if pairs[i][1] == 0:
        pairs.pop(i)
        i -= 1
    i += 1

def sorter(e, sortby=0):
    return e[sortby]

pairs.sort(key=sorter, reverse=False)

header = [("namespace:", "network:"), ("------------", "------------")]

for h in header:
    format = "%-40s %20s"
    n = format%(h)
    print(n)

for pair in pairs:
    format = "%-40s %20s"
    n = format%(pair)
    print(n)
