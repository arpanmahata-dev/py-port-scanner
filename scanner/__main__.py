import argparse
import json
import time
from rich.console import Console
from rich.table import Table
from .core import scan

# Common port mappings for the table
COMMON_PORTS = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 
                53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS", 
                3306: "MySQL", 5432: "Postgres", 8080: "HTTP-Proxy"}

def parse_ports(spec: str) -> list[int]:
    """Converts '22,80,1000-1010' into [22, 80, 1000, 1001... 1010]"""
    ports = []
    for part in spec.split(","):
        if "-" in part:
            start, end = part.split("-")
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return ports

def main():
    # 1. Setup Argument Parser (CLI options)
    parser = argparse.ArgumentParser(description="🚀 Concurrent Port Scanner")
    parser.add_argument("host", help="The target IP or hostname (e.g. scanme.nmap.org)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports to scan (e.g. '80,443' or '1-1024')")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout per port in seconds")
    parser.add_argument("-w", "--workers", type=int, default=200, help="Number of parallel threads")
    parser.add_argument("--json", help="Save results to a JSON file")
    
    args = parser.parse_args()
    console = Console()
    
    # 2. Process ports and start scan
    target_ports = parse_ports(args.ports)
    console.print(f"[bold cyan]Scanning {args.host}[/bold cyan] ({len(target_ports)} ports)...")
    
    start_time = time.time()
    open_ports = scan(args.host, target_ports, args.workers, args.timeout)
    duration = time.time() - start_time
    
    # 3. Build a beautiful table using 'rich'
    table = Table(title=f"Scan Results for {args.host}")
    table.add_column("Port", style="cyan", justify="right")
    table.add_column("Service", style="magenta")
    
    for p in open_ports:
        service = COMMON_PORTS.get(p, "Unknown")
        table.add_row(str(p), service)
    
    console.print(table)
    console.print(f"[green]✔ Found {len(open_ports)} open ports in {duration:.2f}s[/green]")
    
    # 4. Optional JSON export
    if args.json:
        data = [{"port": p, "service": COMMON_PORTS.get(p, "Unknown")} for p in open_ports]
        with open(args.json, "w") as f:
            json.dump(data, f, indent=2)
        console.print(f"💾 Results saved to [yellow]{args.json}[/yellow]")

if __name__ == "__main__":
    main()