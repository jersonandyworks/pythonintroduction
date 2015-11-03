# CREATING LISTS
tools = [[123],"NMAP","SCRATCH",[123,"PortScanner"]]

for tool in range(0,len(tools)):
    if tool == 3:
        for x in range(0,len(tools[tool])):
            print tools[tool][x]
        break
    print tools[tool]

print tools[0:3] # slicing lists