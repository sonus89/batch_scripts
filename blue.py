#!/usr/bin/python
import os
import sys 
import time 			
import bluetooth 	# PyBluez 

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

#######################################################

def LoadingSignal():
	print("Please wait! Processing...\n")
	
#######################################################

def DiscoverDevices():
	# This function returns the list of nearby_devices
	
	LoadingSignal()
	
	nearby_devices = bluetooth.discover_devices(
			duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
	return nearby_devices

#######################################################
	
def PrintList(nearby_devices):
	# This function prints the list of nearby_devices
	
	print 'The following devices have been found:\n'
	for addr, name in nearby_devices:
		try:
			print ("  %s - %s" % (addr, name))
		except UnicodeEncodeError:
			print ("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
	print '\n\n\n'
	
#######################################################

def Connect():	
	name = 'DestinationHost'      				# Device name
	addr = '70:BB:E9:96:CE:96'      			# Device Address
	port = 1         									# RFCOMM port
	passkey = "1111" 								# passkey of the device you want to connect

	socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	socket.connect((addr,port))
	
#######################################

os.system('cls')
PrintList(DiscoverDevices())

