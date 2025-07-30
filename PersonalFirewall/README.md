# 🔥 Personal Firewall for Windows

A custom-built personal firewall application using Python and Scapy.  
It captures, analyzes, and logs network traffic in real-time and allows dynamic IP blocking via a simple GUI interface.

---

## 📌 Features

- 🔍 **Real-time packet monitoring**
- 📁 **Logs all traffic** (source, destination, protocol)
- 🛑 **Custom IP blocking** (toggle from GUI)
- 🧠 Built using **Scapy + Tkinter**
- ⚙️ Fully functional on **Windows OS**

---

## 📷 GUI Screenshot

> ![GUI Screenshot](screenshot.png)  
> *(Optional: Add a screenshot of the GUI in your repo)*

---

## 🛠️ Tools & Technologies

- **Python 3.x**
- **Scapy**
- **Tkinter** (for GUI)
- **WinDivert** (optional for deeper Windows filtering)

---

## 📂 Project Structure

PersonalFirewall/
├── firewall_gui.py # GUI and control logic
├── scapy_firewall_core.py # Core firewall logic (Scapy)
├── logs/
│ └── traffic_log.txt # Captured packet logs

yaml
Copy
Edit

---

## ▶️ How to Run

### 🔧 Prerequisites

- Python 3.8 or later installed
- Install dependencies:
  ```bash
  pip install scapy
🚀 Run the Firewall GUI
Open Terminal or CMD

Navigate to the project folder:

bash
Copy
Edit
cd path\to\PersonalFirewall
Run the GUI:

bash
Copy
Edit
python firewall_gui.py
📖 How It Works
The firewall captures packets using Scapy's sniff() method.

Each packet is parsed and logged to logs/traffic_log.txt.

You can block any IP address by entering it in the GUI and toggling it.

Blocked packets are dropped and logged as [BLOCKED].

🧠 Skills Gained
Packet sniffing & filtering

GUI application development

Network traffic analysis

Real-time logging & system security

Windows OS firewall-level architecture

💡 Future Improvements
Add persistent rule saving (JSON or SQLite)

Port blocking and protocol filtering

Dark theme for the GUI

System tray integration

📜 License
MIT License © Rahul R.