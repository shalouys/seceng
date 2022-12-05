import os
import sys
from scapy.utils import *
import pyshark
import subprocess

#Must have Tshark installed.
#Total number of pkts
def analyzePcap(logFile):
    cnt = 0
    for (pkt_data, pkt_metadata,) in RawPcapReader(logFile):
        cnt += 1
    print(f'[+][+][+] The log {logFile} has {cnt} packets [+][+][+]')
    #Use Tshark to read the file
    csvFile = logFile + '.csv'
    # data = subprocess.run(['tshark', '-N', 'n', '-r', f'{logFile}', '-T', 'fields', '-e', 'frame.number', '-e', '_ws.col.Time', '-e', '_ws.col.Source','-e', '_ws.col.Destination', 
    # '-e', '_ws.col.Protocol', '-e', '_ws.col.Length', '-e', '_ws.col.Info', '-E', 'header=y', '-E', 'separator=\t'])# '>', f'{logFile}'])
    with open (f'{csvFile}', 'w+') as outfile:
        data = subprocess.Popen(['tshark', '-N', 'n', '-r', f'{logFile}', '-T', 'fields', '-e', 'frame.number', '-e', '_ws.col.Time', '-e', '_ws.col.Source','-e', '_ws.col.Destination', 
        '-e', '_ws.col.Protocol', '-e', '_ws.col.Length', '-e', '_ws.col.Info', '-E', 'header=y', '-E', 'separator=\t'], stdout=outfile)# '>', f'{logFile}'])
def main():    
    #Read filename from commandline
    cmnd = sys.argv
    #Check whether files exists and execute the various above commands
    if not os.path.exists(cmnd[1]):
        print(cmnd[1])
        print('Log file not found')
    else:
        print('[+][+][+] Analyzing File...[+][+][+]')
        fileToRead = analyzePcap(cmnd[1])

if __name__ == '__main__':
    main()

