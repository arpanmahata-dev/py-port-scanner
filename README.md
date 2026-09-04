# 🔎 py-port-scanner

A high-performance, concurrent TCP port scanner written in pure Python. 🚀

![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/py-port-scanner)
![Python Version](https://img.shields.io/badge/python-3.12-blue)

## 📖 What is this?
This is a tool that checks which network ports are open on a given host. Unlike a sequential scanner that checks ports one-by-one (which is very slow), this tool uses **multi-threading** to scan hundreds of ports simultaneously.

## ⚡ Quickstart

### 🛠 Installation
```bash
# 1. Clone the repository
git clone https://github.com/arpanmahata-dev/py-port-scanner.git
cd py-port-scanner

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt



🚀 Usage
Scan the official nmap test server:

Bash

python -m scanner scanme.nmap.org -p 1-1024
Other Options:

Scan specific ports: python -m scanner 127.0.0.1 -p 22,80,443
Custom timeout: python -m scanner scanme.nmap.org -t 1.5
Save to JSON: python -m scanner scanme.nmap.org --json results.json
🛠 How it Works
TCP Handshake: The tool uses socket.connect_ex(), which attempts the TCP three-way handshake. If it returns 0, the port is open.
Concurrency: I used ThreadPoolExecutor from the concurrent.futures module. This allows the program to handle multiple network requests in parallel, reducing scan time from minutes to seconds.
CLI Interface: Built using argparse for a professional command-line experience and rich for a beautiful terminal UI.
📊 Performance Comparison
Method	Ports Scanned	Time Taken
Sequential (1 by 1)	1,024	~8.5 minutes
Concurrent (200 threads)	1,024	~6.2 seconds
🎓 What I Learned
🌐 Networking: The difference between an Open, Closed, and Filtered port.
🧵 Concurrency: How threads work and why they are perfect for I/O-bound tasks (like networking).
🛠 DevOps: Using virtual environments, .gitignore, and publishing a professional project on GitHub.
⚖️ Legal Note
Only scan devices you own or have explicit permission to test. Scanning unauthorized servers can be illegal. Use scanme.nmap.org for practice.