# Network_Packet_Sniffer

A beginner-friendly Network Packet Sniffer built using Python + Scapy.  
It captures live network traffic and displays important details like IP addresses, ports, protocol types, and payload.  

This tool is designed for ethical cybersecurity learning.  

🚀 Features:-
-----------------
📌 Capture live network packets

📌 Extract source & destination IPs

📌 Identify protocols (TCP, UDP, ICMP)

📌 Display port numbers

📌 Show raw payload (if available)

📌 Windows-friendly (requires Npcap)

📌 Lightweight & easy to understand

Installation
-----------------
📌 Install Python (3.10 or above)  

  * Download: https://www.python.org/downloads/  

📌 Install Required Python Library  

  * pip install scapy. (In Bash)  

📌 Install Npcap (Required for Windows Packet Sniffing)  

  * Download from: https://npcap.com/#download  

During installation, enable:  
------------------------------
✔ Install Npcap in WinPcap API-compatible Mode    
✔ Recommended: Restart computer after installation    

▶️ Usage
------------
* Run the sniffer:  
* (In Bash)  
* python packet_sniffer.py  
* The program will start capturing packets immediately.  

🧪 Sample Output  
------------------
---------------- PACKET CAPTURED ----------------  
    Source IP: 192.168.1.10  
    Destination IP: 142.250.193.78  
    Protocol: TCP  
    Source Port: 51522  
    Destination Port: 443  
    Payload: b'GET / HTTP/1.1...'  

❌ How to Stop the Sniffer
----------------------------
* Press CTRL + C in the terminal.


⚠️ Legal & Ethical Notice
--------------------------------
This tool is for:  

✔ Learning  
✔ Cybersecurity practice  
✔ Analyzing your own network  
 
❗ Do NOT sniff networks without explicit permission.
Unauthorized sniffing is illegal and punishable under cyber laws.
