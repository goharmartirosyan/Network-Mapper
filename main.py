import socket

def get_service_name(port):
    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL Database",
        69: "TFTP",
        119: "NNTP",
        161: "SNMP",
        179: "BGP",
        389: "LDAP",
        636: "LDAPS",
        8080: "HTTP Proxy",
        8443: "HTTPS",
    }
    return services.get(port, "Unknown")

def scan_ports(target, start_port, end_port):
    open_ports = []
    for i in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, i))
            if result == 0:
                service_name = get_service_name(i)
                open_ports.append((service_name, i))
            s.close()
        except Exception as e:
            print(f"Error: {e}")
    return open_ports

if __name__ == "__main__":
    host_ip = input("Do you want to scan your IP address? (yes/no)")
    if host_ip == "yes":
        target_host = socket.gethostbyname(socket.gethostname())
    else:
        target_host = input("Enter target host or IP address: ")

    port_count = input("Do you want to scan all ports? (yes/no)")
    if port_count == "yes":
        open_ports = scan_ports(target_host, 1, 65535)
    else:
        start_port = int(input("Enter starting port number: "))
        end_port = int(input("Enter ending port number: "))
        open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("PORT  SERVICE   STATE")
        for service_name, port in open_ports:
            print(f"{port}     {service_name}      OPEN")
    else:
        print("No open ports found.")
