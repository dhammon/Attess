
```
 █████╗ ████████╗████████╗███████╗███████╗███████╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔════╝██╔════╝
███████║   ██║      ██║   █████╗  ███████╗███████╗
██╔══██║   ██║      ██║   ██╔══╝  ╚════██║╚════██║
██║  ██║   ██║      ██║   ███████╗███████║███████║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝

Blackbox testing AWS public services
```                                               

> Pronounced "uh-tes" almost like attest, which is the play on words we are looking for under the context of attesting to the security.  The name is derived from combining "attack" and "access" and this tool suite's objective is to fill the gap where so many awesome tools fall short when approaching AWS account's public internet posture.



# Installation
```
git clone https://github.com/dhammon/Attess
cd Attess
pip install -r requirements.txt
```


# Use
`./attess.py --help`



## Account Module
Test a single AWS account number is valid (in use).
```
./attess.py account 123123123123

[-] Invalid AWS Account: 123123123123
```

## Accounts Module
Test a range of AWS account numbers for use.
```
 ./attess.py accounts 123123123123 123123123173 --threads=10

[!] 100% complete
Seconds spent: 2
```

## ECR Module
Identify misconfigured open container repositories through bruteforce.  Not stealthy and requires `principal: *` misconfigured policy.
```
./attess.py containers 123123123123

[!] Completed
```

## Surface Module
Requires AWS credentials set:
```bash
export AWS_ACCESS_KEY_ID=SOME_KEY
export AWS_SECRET_ACCESS_KEY=SOME_KEY
```


# Test
```bash
python3 -W ignore:ImportWarning -m unittest discover -s tests/ -p test_surface.py
python3 -W ignore:ImportWarning -m unittest discover -s tests/ -p test_surface.py -k test_reservations
```

# Credits
Ascii (ANSI Shadow) art generated using patorjk.com