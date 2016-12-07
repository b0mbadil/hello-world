#!/usr/bin/python

from ftplib import FTP
import sys, traceback, getopt, os, subprocess

# module to recursively search for files
def fileguess(filelist, ftp): 
	with open(filelist) as t:
		for files in t:
			try:
				if (ftp.size(files)): # if the ftp server responds with a file size
					print"	file found:",files
			except:
				continue
		t.close()

# module to recursively search through directories
def searchloop(lines, inputfile, ftp, filelist):
	try:
		if("success" in ftp.cwd(lines)):
			 print(ftp.pwd()) # if the directory is found, print the directory
			 if(filelist != ''):
				fileguess(filelist, ftp)
			 else:
				pass
			 with open(inputfile)as g: # open directorylist again and search every word in the changed directory
				for words in g:
					searchloop(words, inputfile, ftp, filelist)
			        ftp.cwd('..') # when search hits an end, move back a directory and try again
	except: # if no directory exists, exit the loop
		pass
		

# module to initiate FTP connection and call the recursive function 
def ftpguess(IP, inputfile, filelist):
	ftp = FTP(IP)
	ftp.login()
	with open(inputfile)as f:
		for lines in f: # for each word in the directorylist, do the recursive loop
			searchloop(lines, inputfile, ftp, filelist)

	f.close()
	ftp.cwd('/')
	ftp.pwd()
	fileguess(filelist, ftp)

def main(argv):
	IP = ''
	directorylist = ''
	filelist = ''
	try:
		options, args = getopt.getopt(argv,"hi:d:f:",["IP","directorylist","filelist"])

	except: 
		getopt.GetoptError
		print 'FTPBuster.py -i <ip> -d <input directorylist> -f <input filelist>'
		sys.exit(2)

	for opt, arg in options:
		if opt == "-h":
			print'FTPBuster.py -i <ip> -d <input directorylist> -f <input filelist>'
			sys.exit()
		elif opt in ("-d","--directorylist"):
			directorylist = arg
		elif opt in ("-i","--ip"):
			IP = arg
		elif opt in ("-f","--filelist"):	
			filelist = arg
		else:
			assert False, "unhandled option"

	ftpguess(IP, directorylist, filelist) # call guessing module after taking in options
        
if __name__=="__main__":
	main(sys.argv[1:])
