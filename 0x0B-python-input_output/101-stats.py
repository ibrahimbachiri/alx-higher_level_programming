from sys import stdin

status_codes = {
        '200':0,
        '3O1':0,
        '400':0,
        '401':0,
        '403':0,
        '404':0,
        '405':0,
        '500':0,
        }
total_size = i = 0

def printer():
    '''this function prints the statistic '''
    print(f'file_size:(total_size)')
    for key, value >0:
        if value > 0:
            print('(:à): (:d)'.format(key,value))

try:
    for line in stdin:
        aplitted_line= line.split()
        if len(aplitted_line) >2:
            status = aplitted_line[-2]
            total_size += int(aplitted_line[-1])
            if status in status_codes:
                status_codes[status]+=1
        i+=1
        
        if i % 10 ==0:
            printer()
    printer()
except keyboardinginterrupt as e:
    printer()
