# brute-beta
**This project is still under development!** My goal of this project/tool to aid InfoSec and bug bounty community find better, faster, equipped with latest and more reliable librabries with positive outcome in their workflow.

Brute is a cmdline Fuzzer. It scans for web pages by engulfing wordlist and URL to scan. It also has latest `httpx` library to handle HTTP2 requests. I had a lot of problems handling HTTP2 requests. So after googling and reading plethora of documents I finally started working with `httpx` library and traditional `requests` library doesn't work well with HTTP2 requests.

                                 
                               (   )\ )         *   )      
                             ( )\ (()/(    (  ` )  /( (    
                             )((_) /(_))   )\  ( )(_)))\   
                            ((_)_ (_))  _ ((_)(_(_())((_)  
                             | _ )| _ \| | | ||_   _|| __| 
                             | _ \|   /| |_| |  | |  | _|  
                             |___/|_|_\ \___/   |_|  |___| v1.0



Usage:
1. `python3 brute-beta.py --help`
2. `python3 brute-beta.py`

Arguments:
* -u URL        : Enter a URL to bruteforce with FUZZ keyword. Example: `-u http://google.com/FUZZ`
* -w wordlist   : Enter wordlist file. Example: `-w wordlist.txt`
* -sc int       : Show URL with status code. Example: `-sC 200,301` etc.
* -proxy URL    : Proxy. Example: `-proxy http://127.0.0.1:8000`
* -e Extention  : File extentions to add at the end of a FUZZ keyword. Example: `-e php,txt,aspx` etc.

Working:
1. Simple Scan : `python3 brute-beta.py -w wordlist.txt -u http://google.com/FUZZ`

![presentation](https://user-images.githubusercontent.com/62895723/136960233-77babed9-4625-4227-8770-e56c5c4e01f2.png)


2. Show 200 only: `python3 brute-beta.py -w wordlist -u http://google.com/FUZZ -sc 200`
 
![sc](https://user-images.githubusercontent.com/62895723/136962200-26b71fa8-438d-4e72-81a5-cbbf96ea4f5c.png)
