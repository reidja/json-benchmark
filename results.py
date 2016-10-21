import csv

records = {}
with open('results.txt', 'r') as f:
    lines = f.readlines()
    runner = None
    size = None

    p = None
    s = None
    m = None
    u = None
    for line in lines:
        if line.startswith("+"):
            p = None
            s = None
            m = None
            u = None
            runner, size = line[1:].strip().split(",")
            if runner not in records:
                records[runner] = {}

            if size not in records[runner]:
                records[runner][size] = []

        elif line[0:2] in ['p:', 's:', 'm:', 'u:']:
            value = line[2:].replace('PT', '').replace('S', '').replace('KB', '').strip()

            if line[0] == 'p':
                p = float(value)
            elif line[0] == 's':
                s = float(value)
            elif line[0] == 'm':
                m = int(value)
            elif line[0] == 'u':
                u = float(value)

            if p is not None and s is not None and m is not None and u is not None:
                records[runner][size].append(
                    (p,s,m,u,))

    with open('results.csv', 'wb') as summary_file:
        with open('detailed.csv', 'wb') as detailed_file:
            summary_writer = csv.writer(summary_file)
            detailed_writer = csv.writer(detailed_file)

            averaged = {}
            for runner, results in records.iteritems():
                for filesize, runs in results.iteritems():
                    total_p = 0
                    total_s = 0
                    total_m = 0
                    total_u = 0
                    count = len(runs)
                    for run in runs:
                        total_p += run[0]
                        total_s += run[1]
                        total_m += run[2]
                        total_u += run[3]

                        detailed_writer.writerow([
                            runner,
                            filesize,
                            run[0],
                            run[1],
                            run[2],
                            run[3],
                        ])

                    summary_writer.writerow([
                        runner,
                        filesize,
                        count,
                        total_p/count,
                        total_s/count,
                        total_m/count,
                        total_u/count,
                    ])
