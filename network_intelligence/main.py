import argparse
import psutil
import json
import os
from .connections import get_active_connections, get_connections_from_log
from .connectors.abuseipdb_connector import AbuseIPDBConnector
from .threat_checker import check_ips
from .config import load_config


def perform_ip_check(source, logfile, output_file, detailed):
    config = load_config()
    api_key = config.get('api_key')

    if source == 'active':
        try:
            ip_addresses = get_active_connections()
        except (psutil.AccessDenied, PermissionError) as e:
            print(f"Error: {e}. "
                  "This script requires elevated permissions to "
                  "access network connections.")
            print("Try executing the program with elevated privileges.")
            return
    else:
        ip_addresses = get_connections_from_log(logfile)

    print(f"Found {len(ip_addresses)} unique IP addresses.")

    connector = AbuseIPDBConnector(api_key)
    results = check_ips(connector, ip_addresses)

    for ip, result in results.items():
        if 'error' in result:
            print(f"IP: {ip}, Error: {result['error']}")
        else:
            print(f"IP: {ip}, Reports: {result['data']['totalReports']}")
            if detailed:
                print(f"Details: {json.dumps(result['data'], indent=2)}")

    if output_file:
        if os.path.exists(output_file):
            print(f"Error: File '{output_file}' already exists."
                  "Results will not be saved to avoid overwriting.")
        else:
            try:
                with open(output_file, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"Results saved to {output_file}")
            except PermissionError as e:
                print(f"Error: {e}. Unable to write to file '{output_file}'."
                      "Results will not be saved.")


def main():
    parser = argparse.ArgumentParser(description="Network Intelligence Tool")
    parser.add_argument('--source',
                        choices=['active', 'log'],
                        required=True,
                        help="Source of IP addresses")
    parser.add_argument('--logfile',
                        type=str,
                        help="Path to the log file \
                        (required if source is 'log')")
    parser.add_argument('--output',
                        type=str,
                        help="Path to save the output file")
    parser.add_argument('--detailed',
                        action='store_true',
                        help="Display detailed reports")

    args = parser.parse_args()

    if args.source == 'log' and not args.logfile:
        parser.error("--logfile is required when source is 'log'")

    perform_ip_check(args.source, args.logfile, args.output, args.detailed)


if __name__ == "__main__":
    main()
