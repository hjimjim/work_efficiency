import pprint
data = open("data.txt", 'r')
lines = data.readlines()

hosts = []
print("hello")
for line in lines :
    check_host = []
    check_sw = False
    hostname = line.split("/")[0]
    switch = line.split("/")[1]
    nic = line.split("/")[2]

    if len(hosts) == 0 :
        host_dic = {
            'name' : hostname,
            'switches' : [{
                'name' : switch,
                'nic' : [nic],
                'vlan' : []
            }]
        }
        hosts.append(host_dic)
    else :
        for host in hosts :
            if hostname == host.get('name') :
                check_host = [host]
                for sw in host.get('switches') :
                    if switch == sw.get('name') :
                        sw.get('nic').append(nic)
                        check_sw = True
        
        if len(check_host) == 0 :
            host_dic = {
                'name' : hostname,
                'switches' : [{
                    'name' : switch,
                    'nic' : [nic],
                    'vlan' : []
                }]
            }
            hosts.append(host_dic)
        elif not check_sw :
            new_switch = { 
                'name' : switch,
                'nic' : [nic],
                'vlan' : []
            }
            check_host.pop().get('switches').append(new_switch)

                

data = open("data2.txt", 'r')
lines = data.readlines()

for line in lines :
    hostname = line.split("/")[0]
    switch = line.split("/")[1]
    vlan = line.split("/")[2]

    for host in hosts :
        if hostname == host.get('name') :
            for sw in host.get('switches') :
                if switch == sw.get('name') :
                    sw.get('vlan').append(vlan)


pprint.pprint(hosts)
