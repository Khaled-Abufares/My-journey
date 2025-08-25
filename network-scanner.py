import argparse
import ipaddress
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import socket
import csv
import logging
from tqdm import tqdm
#~~~~~~~~Logging~~~~~~~~~~#
logging.basicConfig(filename='network_scanner.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#~~~~~~~~Parse CLI arguments~~~~~~~~~~#
def parse_network(s):
    try:
        return ipaddress.ip_network(s, strict=False)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid network '{s}': {e}")
parser = argparse.ArgumentParser(description="Simple network scanner (iterate hosts of a CIDR).")
parser.add_argument("-c", "--cidr",
                    dest="network",
                    nargs="?",
                    default="192.168.1.0/24",
                    const="192.168.1.0/24",
                    type=parse_network,
                    help="CIDR (e.g. 192.168.1.0/24). If flag provided without value, uses default.")
parser.add_argument("--threads", type=int, default=100, help="Max number of threads")
parser.add_argument("--timeout", type=float, default=0.5, help="Timeout for socket connections")
parser.add_argument("--ports", type=str, default="22,80,443,445", help="Comma-separated ports to scan")
args = parser.parse_args()
net = args.network  # IPv4Network/IPv6Network
max_threads = args.threads
timeout = args.timeout
ports_to_scan = list(map(int, args.ports.split(",")))
print(f"Network: {net}, Threads: {max_threads}, Timeout: {timeout}, Ports: {ports_to_scan}")
if net.num_addresses > 4096:
    parser.error("Network too large. Please use a more specific prefix (e.g. /24).")
#~~~~~~~~Ping function~~~~~~~~~~#
def ping(ip):
    plat = platform.system()
    if plat == "Windows":
        cmd = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]
    try:
        subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False
#~~~~~~~~Port scanning function~~~~~~~~~~#
def scan_ports(ip, ports=[22, 80, 443, 445]):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            if sock.connect_ex((str(ip), port)) == 0:
                open_ports.append(port)
        except Exception as e:
            logging.error(f"Error scanning port {port} on {ip}: {e}")
        sock.close()
    return open_ports
#~~~~~~~~Scan hosts~~~~~~~~~~#
results = []
with ThreadPoolExecutor(max_workers=max_threads) as ex:
    futures = {ex.submit(ping, str(ip)): ip for ip in net.hosts()}
    for fut in tqdm(as_completed(futures), total=net.num_addresses-2, desc="Scanning Hosts"):
        ip = futures[fut]
        try:
            if fut.result():
                open_ports = scan_ports(ip, ports=ports_to_scan)
                results.append((str(ip), "up", open_ports))
                print(f"{ip} is up | Open ports: {open_ports}")
                logging.info(f"{ip} is up | Open ports: {open_ports}")
        except Exception as e:
            print(f"Error scanning {ip}: {e}", file=sys.stderr)
            logging.error(f"Error scanning {ip}: {e}")
#~~~~~~~~Save results~~~~~~~~~~#
def save_results(results, filename="scan_results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Status", "Open Ports"])
        for ip, status, ports in results:
            writer.writerow([ip, status, ",".join(map(str, ports))])
save_results(results)
print(f"Scan complete. Results saved to scan_results.csv")
logging.info("Scan complete. Results saved to scan_results.csv")
