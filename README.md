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