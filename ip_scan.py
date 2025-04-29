import socket



def scan_hosts(start_ip, end_ip, timeout=1):

    available_hosts = []

    

    for i in range(start_ip, end_ip + 1):

        ip = f"172.16.64.{i}"

        

        try:


            socket.setdefaulttimeout(timeout)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip, 80))

            s.close()

            available_hosts.append(ip)

            print(f"發現主機：{ip}")

        except:

            pass

    

    return available_hosts

start_ip = 1

end_ip = 255

available_hosts = scan_hosts(start_ip, end_ip)

if available_hosts:

    print("可用的主機：", available_hosts)

else:

    print("未找到可用的主機。")