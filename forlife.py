# -*- coding: UTF-8 -*-
for myday in range(1, 6):
    print('study..%d....' % myday)
    for clock in range(7, 17):
        print('study at school at %d clock' % clock)
    for clock in range(16, 19):
        print('CCA at school at %d clock' % clock)
    for clock in range(18, 20):
        print('Self study at night at %d clock' % clock)
    for clock in range(19, 23):
        print('rest in room at %d clock' % clock)
    for clock in range(22, 31):
        if clock > 24:
            print('sleep at room at %d clock' % (clock - 24))
        else:
            print('sleep at room at %d clock' % clock)
