import argparse
import kubedata
import kubedisplay

"""Different arguments and their actions:

'-p', '--period' : passed in as the period over which the data is collected
'-w', '--walltime' : gets wallclock time data
'-g', '--gpu' : gets gpu data
'-c', '--cpu' : gets cpu data
'-m', '--memory' : gets memory usage data
'-n', '--network' : gets network data
'--all' : ensures all data is displayed, including zero values
'-s', '--sortby' : indicates if to sort alphabetically ("0"), or numerically ("1")
'-o', '--offset' : how much time in the past data is collected from
'-r', '--reverse' : sorting is reversed if passed through the command line
'--requested' : gets the total cpu or gpus requested as opposed to used if passed in through the command line along with '-c' or '-g'
'--transmit' : gets the total transmitted network as opposed to the default received network if passed through the commandline along with '-n'
'-u', '--unit' : unit by which to convert the data, if not passed in data is automatically converted to the best fit unit

"""

parser = argparse.ArgumentParser(description='displays kubernetes data queried from prometheus')
parser.add_argument('-p', '--period', required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument('-w', '--walltime', action='store_true')
group.add_argument('-g', '--gpu', action='store_true')
group.add_argument('-c', '--cpu', action='store_true')
group.add_argument('-m', '--memory', action='store_true')
group.add_argument('-n', '--network', action='store_true')
parser.add_argument('--all', action='store_true')
parser.add_argument('-s', '--sortby')
parser.add_argument('-o', '--offset')
act = parser.add_mutually_exclusive_group()
act.add_argument('-r', '--reverse', action='store_true')
act.add_argument('--requested', action='store_true')
act.add_argument('--transmit', action='store_true')
act.add_argument('-u', '--unit')
args = parser.parse_args()

if __name__ == '__main__':
    queryurl = kubedata.Promdata('prometheus.nautilus.optiputer.net')
    if args.walltime:
        offset = ""
        if args.offset:
            offset = args.offset
        wall_dat = queryurl.wallclock(args.period, args.offset)
        unit = ""
        sortby = ""
        reverse = False
        all = False
        if args.unit:
            unit = args.unit
        if args.sortby:
            sortby = args.sortby
        if args.reverse:
            reverse = True
        if args.all:
            all = True
        kubedisplay.walltime(wall_dat, sortby, unit, reverse, all)

    elif args.gpu:
        requested = False
        offset = ""
        if args.requested:
            requested = args.requested
        if args.offset:
            offset = args.offset
        gpu_dat = queryurl.gpu(args.period, args.requested, args.offset)
        unit = ""
        sortby = ""
        reverse = False
        all = False
        if args.unit:
            unit = args.unit
        if args.sortby:
            sortby = args.sortby
        if args.reverse:
            reverse = True
        if args.all:
            all = True
        kubedisplay.gpu(gpu_dat, sortby, unit, reverse, all)

    elif args.cpu:
        requested = False
        offset = ""
        if args.requested:
            requested = args.requested
        if args.offset:
            offset = args.offset
        cpu_dat = queryurl.cpu(args.period, requested, offset)
        unit = ""
        sortby = ""
        reverse = False
        all = False
        if args.unit:
            unit = args.unit
        if args.sortby:
            sortby = args.sortby
        if args.reverse:
            reverse = True
        if args.all:
            all = True
        kubedisplay.cpu(cpu_dat, sortby, unit, reverse, all)

    elif args.memory:
        offset = ""
        if args.offset:
            offset = args.offset
        memory_dat = queryurl.memory(args.period, offset)
        unit = ""
        sortby = ""
        reverse = False
        all = False
        if args.unit:
            unit = args.unit
        if args.sortby:
            sortby = args.sortby
        if args.reverse:
            reverse = True
        if args.all:
            all = True
        kubedisplay.memory(memory_dat, sortby, unit, reverse, all)

    elif args.network:
        offset=""
        transmit=""
        if args.offset:
            offset=args.offset
        if args.transmit:
            transmit = "transmit"
        network_dat = queryurl.network(args.period, offset, transmit)
        unit=""
        sortby = ""
        reverse = False
        all = False
        if args.unit:
            unit = args.unit
        if args.sortby:
            sortby = args.sortby
        if args.reverse:
            reverse = True
        if args.all:
            all = True
        kubedisplay.network(network_dat, sortby, unit, reverse, all)
