
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
daniel@daniel-desktop:~/Attess# ./attess.py account 123123123123
[-] Invalid AWS Account: 123123123123
```
#TODO Accounts Module

# Credits
Ascii (ANSI Shadow) art generated using patorjk.com