# Create set information for server

home_lab = [
    {
        "name": "Primary-Mac",
        "ip": "100.105.68.115",
        "os": "macOS",
        "services": ["Monitoring", "Terminal", "Tailscale"],
        "ports": [22, 443, 8080]
    },
    {
        "name": "Linux-Server",
        "ip": "100.105.68.118",
        "os": "Ubuntu 24.04",
        "services": ["Docker", "Nginx", "PostgreSQL"],
        "ports": [22, 80, 5432, 8080]
    }
]

# find the unique ports
unique_ports =  set()

for sever in home_lab:
    for port in sever["ports"]:
         unique_ports.add(port)


# print each data
print("------------ Home lab Servers ----------")

for sever in home_lab:
      print(f"\n[Server Name: {sever['name']}]")
      print(f"IP Addres: {sever["ip"]}")
      print(f"Operating System: {sever["os"]}")
      print(f"Services: {sever["services"]}")

# print unique ports
print("\n","-"*36)

print(f"Unique Port: {sorted(unique_ports)}")

print("\n","-"*36)