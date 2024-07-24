import psutil


def get_active_connections():
    connections = psutil.net_connections(kind='inet')
    ip_addresses = set()
    for conn in connections:
        if conn.raddr and conn.raddr.ip:
            ip_addresses.add(conn.raddr.ip)
    return list(ip_addresses)


def get_connections_from_log(log_file):
    ip_addresses = set()
    with open(log_file, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                ip_addresses.add(ip)
    return list(ip_addresses)
