import socket

def scan_ports(ip, start_port, end_port, timeout=0.5):
    try:
        host = socket.gethostbyname(ip)
        open_ports = []

        for port in range(start_port, end_port + 1):
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)

            # Attempt to connect to the port
            result = s.connect_ex((host, port))

            if result == 0:
                open_ports.append(port)
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed')

            s.close()

        return open_ports

    except socket.gaierror:
        print('Hostname could not be resolved')
        return []
    except socket.error:
        print('Server not responding')
        return []
    except KeyboardInterrupt:
        print('Scan interrupted by user')
        return []

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    start_port_number = 1
    end_port_number = 65535

    open_ports = scan_ports(ip_address, start_port_number, end_port_number)

    print(f'Open ports: {open_ports}')
