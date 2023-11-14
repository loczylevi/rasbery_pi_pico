import network
wlan = network.WLAN(network.STA_IF) 
wlan.active(True)     
wlan.scan()    


for sor in wlan.scan():
    print(f"SSID: {sor[0]}\t\tMAC: {sor[1]}")
    
