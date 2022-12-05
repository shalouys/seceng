# seceng
Security engineering tools

Log Analyzer

1. Only works in Linux Environments. Must have tshark installed
2. run the command pip install -r requirements.txt to install the required libraries
3. Then run the command python3 code.py <input path to pcap file>

Passwd Bruteforcer:

1. Mimics CEWL, which generates word list from the target website. This wordlist is then used to bruteforce against passwords and/or usernames. 
2. This code assumes you have an already known correct admin username
3. Run the command python3 code.py <input target URL>

PDF parser

1. run the command pip install -r requirements.txt to install the required libraries
2. Then run the command python3 code.py <input path to PDF file>
