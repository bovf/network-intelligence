def check_ips(connector, ip_addresses):
    results = {}
    for ip in ip_addresses:
        result = connector.check_ip(ip)
        if result is not None:
            results[ip] = result
        else:
            results[ip] = {'error': 'Failed to retrieve data'}
    return results
