# -*- coding: UTF-8 -*-
f = open('my_yearlylife.txt','w')


for mymonth in range(1,12):
    for myweek in range(1,5):
        print('week %d' %myweek)
        f.write('week %d\n' %myweek)
        for myday in range(1, 6):
            print('study..%d....' % myday)
            f.write('study..%d....\n' % myday)
            for clock in range(7, 17):
                print('study at school at %d clock' % clock)
                f.write('study at school at %d clock\n' % clock)
            for clock in range(16, 19):
                print('CCA at school at %d clock' % clock)
                f.write('CCA at school at %d clock\n' % clock)
            for clock in range(18, 20):
                print('Self study at night at %d clock' % clock)
                f.write('Self study at night at %d clock\n' % clock)
            for clock in range(19, 23):
                print('rest in room at %d clock' % clock)
                f.write('rest in room at %d clock\n' % clock)
            for clock in range(22, 31):
                if clock > 24:
                    print('sleep at room at %d clock' % (clock - 24))
                    f.write('sleep at room at %d clock\n' % (clock - 24))
                else:
                    print('sleep at room at %d clock' % clock)
                    f.write('sleep at room at %d clock\n' % clock)

f.close()
