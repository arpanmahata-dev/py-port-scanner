import socket
from concurrent.futures import ThreadPoolExecutor

def probe(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def scan(host: str, ports: list[int], workers: int = 200, timeout: float = 0.5) -> list[int]:
    """Check many ports at once using a ThreadPool."""
    open_ports = []
    # ThreadPoolExecutor runs the 'probe' function on many ports in parallel
    with ThreadPoolExecutor(max_workers=workers) as pool:
        # map returns the results in order
        results = pool.map(lambda p: (p, probe(host, p, timeout)), ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    import time
    # a legal target for scanning
    target = "scanme.nmap.org" 
    ports_to_scan = range(1, 1025) # Scan ports 1 to 1024
    
    print(f"Scanning {target}...")
    start = time.time()
    found = scan(target, ports_to_scan)
    end = time.time()
    
    print(f"Open ports: {found}")
    print(f"Time taken: {end - start:.2f} seconds")