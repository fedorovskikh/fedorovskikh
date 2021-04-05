from datetime import datetime

task = 0
task_num = 0
dict_id = 0
deltas = []

with open('/home/fedorovskih/sorm1/dacha/start_task') as file_start:
    for line in file_start:
        task_id = line[line.find('id=') + 3:line.find('}')]
        start_time = datetime.strptime(line[1:23], "%Y-%m-%d %H:%M:%S,%f")
        with open('/home/fedorovskih/sorm1/dacha/finish_task') as file_end:
            for line2 in file_end:
                if task_id in line2:
                    end_time = datetime.strptime(line2[1:23], "%Y-%m-%d %H:%M:%S,%f")
                    delta = end_time - start_time
                    # print('Task id:    ' + task_id + '\n' + "Duration:" + str(delta) + '\n')
                    deltas.append(str('Duration: ' + str(delta) + '; Task: ' + str(task_id)))
                    task_num += 1

deltas = sorted(deltas)

while task < len(deltas):
    print(str(deltas[task]) + '\n')
    task += 1
