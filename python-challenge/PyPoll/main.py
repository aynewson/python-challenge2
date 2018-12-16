import csv
import os


def recover_key(dicty, value):
    for a_key in dicty.keys():
        if (dicty[a_key] == value):
            return a_key


def get_poll_counts(poll_list):
    poll_counts = {}
    for event in poll_list:
        if event['Candidate'] not in poll_counts:
            poll_counts[event['Candidate']] = 0

        poll_counts[event['Candidate']] = poll_counts[event['Candidate']]+1

    return poll_counts


def print_poll_counts(poll_counts):
    print('Election Results')
    poll_output.write('Election Results'+'\n')

    print('-----------------------------')
    poll_output.write('-----------------------------'+'\n')

    TotalVotes = sum(poll_counts.values())
    print('Total Votes:', TotalVotes)
    poll_output.write('Total Votes:'+str(TotalVotes)+'\n')

    print('-----------------------------')
    poll_output.write('-----------------------------'+'\n')

    MaxVotes = max(poll_counts.values())
    Winner = recover_key(poll_counts, MaxVotes)

    for key in sorted(poll_counts, key=poll_counts.get, reverse=True):
        value = poll_counts[key]
        percent = round(float((value/TotalVotes)*100), 3)
        print(key+':'+' '+str(percent)+'%'+' '+'('+str(value)+')')
        poll_output.write(key+':'+' '+str(percent)+'%' +
                          ' '+'('+str(value)+')'+'\n')

    print('-----------------------------')
    poll_output.write('-----------------------------'+'\n')

    print('Winner:', Winner)
    poll_output.write('Winner:'+Winner+'\n')

    print('-----------------------------')
    poll_output.write('-----------------------------'+'\n')


#Main Program#####
poll_list = csv.DictReader(open('poll_csv.csv', 'r'))
poll_output = open('poll_output.txt', 'w')

poll_counts = get_poll_counts(poll_list)
print(poll_counts)
print_poll_counts(poll_counts)
poll_output.close()
