from scapy.all import sniff, IP, TCP, UDP
import datetime
import threading

blocked_ips = []
blocked_ports = []
log_file_path = "logs/traffic_log.txt"

running = False

def log_packet(pkt, status):
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {status} {pkt[IP].src}:{pkt.sport} -> {pkt[IP].dst}:{pkt.dport} | Proto: {pkt.proto}\n")

def process_packet(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        port = pkt.dport if pkt.haslayer(TCP) or pkt.haslayer(UDP) else None
        status = "[BLOCKED]" if src_ip in blocked_ips or port in blocked_ports else "[ALLOWED]"
        log_packet(pkt, status)

def start_sniffing():
    global running
    running = True
    sniff(filter="ip", prn=process_packet, store=0, stop_filter=lambda x: not running)

def stop_sniffing():
    global running
    running = False

def start_firewall():
    thread = threading.Thread(target=start_sniffing, daemon=True)
    thread.start()
