import json
import requests

headers = {
    'Authorization': 'Bearer undefined',
    'Content-Type': 'application/json',
}

resp = requests.get('https://api.cloudflare.com/client/v4/ips', headers=headers).json()

ipv4 = []
ipv6 = []

if resp['success'] == True:
  ipv4 = resp['result']['ipv4_cidrs']
  ipv6 = resp['result']['ipv6_cidrs']
  print('successfully got ips \n')
else:
  print('error getting ips')
  quit()

with open('./custom_access/cloudflare.conf', 'w') as f:
    for line in ipv4:
        f.write(f"set_real_ip_from {line};\n")
    f.write("\n")
    for line in ipv6:
        f.write(f"set_real_ip_from {line};\n")
    f.write("\nreal_ip_header CF-Connecting-IP;")
    print('file updated, all ok')
    
