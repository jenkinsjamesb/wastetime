#!/usr/bin/env python3
import sys, time

def waste(n):
	if float(n) > 0:
		print("Waiting...")
		time.sleep(float(n))
		print("Done.")
		return 0
	else:
		print("Invalid time. Usage: waste <seconds>")
		return 1

if __name__ == "__main__":
	try:
		waste(sys.argv[1])
	except:
		print("No valid argument. Usage: waste <seconds>")