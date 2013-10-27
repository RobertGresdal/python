import bluetooth

target_name = "Robert Phone"
target_address = None
found_name = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
	found_name = bluetooth.lookup_name( bdaddr )
	print "Device found:: addr: ",bdaddr," name: \"",found_name, "\"","foo"
	if target_name == found_name:
		target_address = bdaddr
#		break

if target_address is not None:
	print "Found target bluetooth device with address ", target_address
else:
	print "Coult not find target"
	
#	 00:11:67:00:02:6F