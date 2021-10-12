import sys, requests, argparse
from colorama import Fore
import httpx


#       Filter by Status Codes
def filter_statuscode(url, wl, sc, proxy, ext):
    with open(wl, 'r') as wordlist:
        lines = wordlist.readlines()        #making list
        word = [w.strip() for w in lines]   #removing \n
        for i in word:
            u = url.replace("FUZZ", i)
            timeout = httpx.Timeout(10.0)
            proxy = args.proxy
            with httpx.Client(proxies=proxy, timeout=timeout, verify=False, http2=True) as client:
                r = client.get(u)
                #if the status code is not mentioned do this+
                if sc == None:                  
                        print(str(i)+ "\t\t\t\t" + str(r.url) + "\t\t\t\t" + str(r.status_code), flush=True)
                # Else filter according to status code        
                else:                           
                    for c in sc:
                        if r.status_code == c:
                            print(str(i)+ "\t\t\t\t" + str(r.url) + "\t\t\t\t" + str(r.status_code), flush=True)


if __name__ == '__main__':
    banner = """
                                   (                       
                               (   )\ )         *   )      
                             ( )\ (()/(    (  ` )  /( (    
                             )((_) /(_))   )\  ( )(_)))\   
                            ((_)_ (_))  _ ((_)(_(_())((_)  
                             | _ )| _ \| | | ||_   _|| __| 
                             | _ \|   /| |_| |  | |  | _|  
                             |___/|_|_\ \___/   |_|  |___| v1.0  
    """
    print(banner, flush=True)
    parser = argparse.ArgumentParser()

    # Creating cmdline arguments
    parser.add_argument("-u", metavar="URL", type=str, help="URL to brute-force")
    parser.add_argument("-w",metavar="Wordlist ", type=str, help="Wordlist")
    parser.add_argument("-sc", type=int, help="Filter HTTP code Example: -sc 200 404 403 will only print url with 200,404,403 status codes [need to be saperated by space]", nargs='+')
    parser.add_argument("-proxy", type=str, help="Proxy Example:         --proxy http://127.0.0.1:8080")
    parser.add_argument("-e", type=str, help="File Extentions Example: -e php txt aspx [need be saperated by space]", nargs='+')
    args = parser.parse_args()

    print(str(args))

    if sys.version_info < (3,0):
        sys.stdout.write("Sorry, Brute requires python versions 3.0 onwards. Please Run it with python3")
        sys.exit(1)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    # FUZZ word must be in url
    if "FUZZ" not in args.u:
        print(Fore.RED + "Please Enter 'FUZZ' Keyword at the place you want to bruteforce!")
        sys.exit()
    elif not (args.u).startswith(("http://" , "https://" )):
        print("Please Enter valid protocol in url. Example. http , https", flush=True)
    else:
        # Print banner and Run accordingly
        print('\n' + Fore.LIGHTCYAN_EX + "Number of words in a File : \t" + str(sum(1 for line in open(args.w)) - 1) 
            + "\n" + "URL : " + str(args.u) 
            + "\n" + "Extensions : " + str(args.e)
            + "\n" + "Wordlist : " + str(args.w), flush=True)
        print( "\n-----------------------------------------------------------------------------------\n")
        try:
            filter_statuscode(args.u, args.w, args.sc, args.proxy, args.e)
        except KeyboardInterrupt:
            sys.stdout.write(Fore.RED + "\nUser interruption! 'ctrl+c' detected!\n")
            sys.exit(0)
            
            
