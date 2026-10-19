<div align="center">

# `>_ DANIEL DAYAN`

**Junior SOC Analyst & Junior Penetration Tester (CPTS & CWES Candidate)**

[![Live Site](https://img.shields.io/badge/Portfolio-0xdnd.github.io-00e58d?style=for-the-badge&logo=googlechrome&logoColor=black)](https://0xdnd.github.io)
[![ZeroBox](https://img.shields.io/badge/Open_Source-ZeroBox_(ctftracker.com)-38bdf8?style=for-the-badge&logo=firefoxbrowser&logoColor=white)](https://ctftracker.com)
[![ZeroBox Traction](https://img.shields.io/badge/ZeroBox_Traction-4%2C000%2B_Visitors-00e58d?style=for-the-badge&logo=googlechrome&logoColor=black)](https://ctftracker.com)
[![ZeroBox Stack](https://img.shields.io/badge/Stack-React_%7C_TypeScript_%7C_Tauri-38bdf8?style=for-the-badge&logo=react&logoColor=white)](https://ctftracker.com)
[![GitHub Repo](https://img.shields.io/badge/GitHub-0xdnd%2Fctf--tracker-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/0xdnd/ctf-tracker)
[![CTFs Solved](https://img.shields.io/badge/CTFs_Solved-50%2B_Rooted-00e58d?style=for-the-badge&logo=hackthebox&logoColor=white)](https://0xdnd.github.io/#ctf)

</div>

---

## >_ About

Cybersecurity professional targeting Junior SOC Analyst and Junior Penetration Tester roles, combining hands-on offensive awareness with disciplined blue-team defense:
- **Creator of [ZeroBox](https://ctftracker.com) ([GitHub: 0xdnd/ctf-tracker](https://github.com/0xdnd/ctf-tracker))** — an open-source penetration testing workspace in React & TypeScript reaching 4,000+ visitors (web app and Tauri desktop app). Features a catalog of 1,000+ HTB & THM machines, 131 reverse shell templates, 8-phase methodology, multi-host Nmap XML importer with one-click attack graph generation, masked credential & hash evidence vault, CVSS v3.1 Markdown report generator, and timed exam simulator for OSCP, CPTS, CRTO, OSEP, CRTP with one-click ZIP submission bundle export.
- **50+ Hack The Box machines rooted (2 active: Reactor & Kobold)**, taking each from reconnaissance and initial access through privilege escalation to full system compromise, plus 30 completed HTB Academy modules.
- **Enterprise Active Directory Homelab** — dual-domain Windows Server 2022 forest with Sysmon (Event ID 1/3/10) telemetry, FortiGate NGFW, and Splunk SPL detection rules for Kerberoasting, AS-REP roasting, and DCSync.
- **650-Hour Cyber Security Implementer Program** at ITQ College (2024 - 2025, Cisco and Fortinet specialization): Cisco IOS XE (VLANs, 802.1Q, OSPF, RIPv2, HSRP, ACLs, NAT, GRE & IPsec VPNs), FortiGate NGFW (simulated two-site Israel-USA network), Windows Server 2022 Active Directory & GPO, LPI Linux Essentials & Kali/Ubuntu administration, and IBM Security QRadar SIEM with WinCollect & Splunk SOAR.
- **HTB Academy Candidate** — actively preparing for HTB Certified Penetration Testing Specialist (CPTS) and Certified Web Exploitation Specialist (CWES).
- **3-year IDF military service** — Service Coordinator investigating hundreds of sensitive soldier entitlement cases in SAP, maintaining data confidentiality and resolution accuracy under daily SLAs and CRM workflows.

---

## >_ Flagship Engineering Projects

### 1. [ZeroBox (ctftracker.com)](https://ctftracker.com) — Open Source CTF Tracker & Penetration Testing Workspace
- **Links**: [Live App: ctftracker.com](https://ctftracker.com) · [Open Source Repo: GitHub (0xdnd/ctf-tracker)](https://github.com/0xdnd/ctf-tracker)
- **Problem**: Fragmented progress tracking across 1,000+ HTB & TryHackMe machines, lack of realistic timed certification practice (OSCP, CPTS, CRTO, OSEP, CRTP), manual port transcription during recon, and friction generating reverse shells and managing evidence/notes across drills.
- **Architecture**: Designed, built, and launched an offline-first penetration testing workspace (web app and Tauri desktop app) in React and TypeScript. Features a catalog of 1,000+ Hack The Box and TryHackMe machines, 131 reverse shell templates, an 8-phase methodology, multi-host Nmap XML importer with one-click attack graph generation, masked credential & hash evidence vault, CVSS v3.1 Markdown report generator, and a timed exam simulator for OSCP, CPTS, CRTO, OSEP, and CRTP with one-click ZIP submission bundle export.
- **Impact**: Reached 4,000+ visitors in production at `ctftracker.com` and open source on GitHub (`0xdnd/ctf-tracker`). 100% offline-first execution with zero accounts, zero cloud telemetry, sub-10ms query performance via IndexedDB/LocalStorage, and native desktop builds via Tauri.
- **Stack**: React, TypeScript, Tauri Desktop, 4,000+ Visitors, IndexedDB / LocalStorage, Obsidian `.canvas`, 1,000+ Machine Catalog, 131 Reverse Shells, 8-Phase Methodology, Nmap XML Importer, CVSS v3.1 Reports, OSCP & CPTS Exam Simulator.

### 2. Enterprise Active Directory Homelab & Sysmon SIEM Detection
- **Links**: [GitHub Repository & Detection Rules](https://github.com/0xdnd)
- **Problem**: Inability to safely observe, replicate, and engineer detection rules against real-world Kerberos ticket abuse, credential dumping, and AD privilege escalation without an enterprise domain forest environment.
- **Architecture**: Dual-domain Windows Server 2022 forest with SwiftOnSecurity modular Sysmon telemetry (Event IDs 1, 3, 10) ingested into Splunk SIEM via Universal Forwarders. Attack paths mapped with BloodHound and adversary executions simulated via Kali Linux.
- **Impact**: Engineered and validated 5 production SPL alert rules covering MITRE ATT&CK T1558 (Kerberoasting / AS-REP) and T1003 (OS Credential Dumping), delivering sub-minute offense correlation with zero false positives during normal domain operations.
- **Stack**: Windows Server 2022, Active Directory Forest, Sysmon (EID 1/3/10), Splunk Enterprise (SPL), BloodHound, Mimikatz & Impacket.

---

## >_ CTF & Lab Telemetry (50+ Rooted Machines)

| Metric | Achievement | Scope / Domain |
| :--- | :--- | :--- |
| **50+** | Machines Rooted | Hack The Box, TryHackMe & Custom Labs |
| **2 Active** | Live Season Roots | Reactor & Kobold (Zero Spoilers · Live HTB Targets) |
| **30+ Modules** | HTB Academy | CPTS & CWES Advanced Offensive and Defensive Tracks |
| **100%** | Integrity | Documented Detection Notes & Telemetry Audit Trails |

### Verified Root Roster (50+ Machines)
- **Active Season Solves (HTB)**: 👑 Reactor, 👑 Kobold.
- **Hack The Box Machines (20)**: TwoMillion, Cap, Broker, Knife, Netmon, Jerry, Nibbles, Bashed, Shocker, Blue, Blocky, Bank, Granny, Grandpa, Optimum, Beep, Devel, Legacy, Lame, Connected.
- **HTB Starting Point (7)**: Archetype, Responder, Dancing, Redeemer, Crocodile, Markup, Previse.
- **TryHackMe & Labs (22)**: Pickle Rick, RootMe, Bounty Hacker, Mr Robot CTF, Agent Sudo, Anthem, Simple CTF, Basic Pentesting, Recruit, Lo-Fi, W1seGuy, MD2PDF, TakeOver, Neighbour, Epoch, Corridor, Agent T, CyberHeroes, Intermediate Nmap, Vulnerability Capstone, Investigating Windows, Enterprise Pivot Lab.

Featured attack vectors and detection models:
- **Active Directory**: AS-REP Roasting, Kerberoasting, DCSync, Pass-the-Hash, GPP cPassword Decryption (Event IDs 4768, 4769, 4624, 4662).
- **Web Security**: Hydra Brute-Force, LFI/RFI, Second-Order SQLi, SSTI, Fuel CMS RCE (WAF regex, URI traversal alerts, child process auditing).
- **Privilege Escalation**: Samba 3.0.20 usermap script RCE, Linux SUID capability abuse, unquoted service paths (Sysmon Event ID 1, Linux auditd).
- **Blue Team / Forensics**: PsExec lateral movement, Registry Run Key persistence, Scheduled Tasks, Rogue DHCP/VLAN hopping (Sysmon EID 1/13, Event 4698, DAI/DHCP Snooping).

---

## >_ Skills

### Defensive Security & SOC

![IBM QRadar SIEM](https://img.shields.io/badge/IBM_QRadar_SIEM-0284c7?style=flat-square&logo=ibm&logoColor=white)
![WinCollect](https://img.shields.io/badge/WinCollect_Agent-0284c7?style=flat-square)
![Splunk SOAR](https://img.shields.io/badge/Splunk_SOAR-0284c7?style=flat-square&logo=splunk&logoColor=white)
![Splunk Enterprise](https://img.shields.io/badge/Splunk_Enterprise_(SPL)-0284c7?style=flat-square&logo=splunk&logoColor=white)
![FortiGate NGFW](https://img.shields.io/badge/FortiGate_NGFW_(Two--Site_Israel--USA)-0284c7?style=flat-square&logo=fortinet&logoColor=white)
![Antivirus & Web Filtering](https://img.shields.io/badge/Antivirus_%26_Web_Filtering-0284c7?style=flat-square)
![Windows Audit Policy](https://img.shields.io/badge/Windows_Audit_Policy-0284c7?style=flat-square)
![Syslog Forwarding](https://img.shields.io/badge/Syslog_Forwarding-0284c7?style=flat-square)
![Sysmon](https://img.shields.io/badge/Sysmon_(EID_1%2F3%2F10)-0284c7?style=flat-square)
![Alert Triage](https://img.shields.io/badge/Alert_Triage-0284c7?style=flat-square)
![Log Investigation](https://img.shields.io/badge/Log_Investigation-0284c7?style=flat-square)
![Wireshark](https://img.shields.io/badge/Wireshark-0284c7?style=flat-square&logo=wireshark&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-0284c7?style=flat-square)

### Offensive Tools & Pentesting

![Nmap](https://img.shields.io/badge/Nmap-059669?style=flat-square&logo=nmap&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-059669?style=flat-square&logo=burpsuite&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-059669?style=flat-square&logo=owasp&logoColor=white)
![OWASP Top 10](https://img.shields.io/badge/OWASP_Top_10-059669?style=flat-square)
![BloodHound](https://img.shields.io/badge/BloodHound-059669?style=flat-square)
![Impacket](https://img.shields.io/badge/Impacket-059669?style=flat-square)
![SQLMap](https://img.shields.io/badge/SQLMap-059669?style=flat-square)
![Metasploit](https://img.shields.io/badge/Metasploit-059669?style=flat-square&logo=metasploit&logoColor=white)
![ffuf](https://img.shields.io/badge/ffuf-059669?style=flat-square)
![Hashcat](https://img.shields.io/badge/Hashcat-059669?style=flat-square)
![Hydra](https://img.shields.io/badge/Hydra-059669?style=flat-square)
![CVSS v3.1](https://img.shields.io/badge/CVSS_v3.1-059669?style=flat-square)

### Networking & Systems

![Cisco IOS XE](https://img.shields.io/badge/Cisco_IOS_XE-d97706?style=flat-square&logo=cisco&logoColor=white)
![FortiGate NGFW](https://img.shields.io/badge/FortiGate_NGFW-d97706?style=flat-square&logo=fortinet&logoColor=white)
![802.1Q](https://img.shields.io/badge/802.1Q_VLANs-d97706?style=flat-square)
![OSPF](https://img.shields.io/badge/OSPF-d97706?style=flat-square)
![RIPv2](https://img.shields.io/badge/RIPv2-d97706?style=flat-square)
![HSRP](https://img.shields.io/badge/HSRP-d97706?style=flat-square)
![GRE & IPsec VPNs](https://img.shields.io/badge/GRE_%26_IPsec_VPNs-d97706?style=flat-square)
![ACLs & NAT](https://img.shields.io/badge/ACLs_%26_NAT-d97706?style=flat-square)
![Port Security](https://img.shields.io/badge/Port_Security-d97706?style=flat-square)
![Windows Server 2022](https://img.shields.io/badge/Windows_Server_2022_(AD%2FGPO)-d97706?style=flat-square&logo=windows&logoColor=white)
![LPI Linux Essentials](https://img.shields.io/badge/LPI_Linux_Essentials-d97706?style=flat-square&logo=linux&logoColor=white)
![Kali & Ubuntu](https://img.shields.io/badge/Kali_%26_Ubuntu_(Netplan%2FSSH)-d97706?style=flat-square&logo=linux&logoColor=white)
![VMware](https://img.shields.io/badge/VMware-d97706?style=flat-square&logo=vmware&logoColor=white)

### Scripting & Programming

![React](https://img.shields.io/badge/React-7c3aed?style=flat-square&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-7c3aed?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-7c3aed?style=flat-square&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-7c3aed?style=flat-square&logo=powershell&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-7c3aed?style=flat-square&logo=gnubash&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-7c3aed?style=flat-square&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/Git-7c3aed?style=flat-square&logo=git&logoColor=white)

---

## >_ About this site

- Single `index.html` — pure HTML/CSS/JS, zero frameworks, zero build step
- Modern cyber architecture: Space Grotesk display typography, ambient radial orbs, interactive SOC readiness cards, dynamic CTF filtering
- Fully responsive · respects `prefers-reduced-motion` · accessible WCAG 2.1 AA

---

## >_ Find me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Daniel_Dayan-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-dayan-a66322352/)
[![GitHub](https://img.shields.io/badge/GitHub-@0xdnd-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/0xdnd)
[![ctftracker.com](https://img.shields.io/badge/ctftracker.com-Production_Platform-00e58d?style=flat-square&logo=googlechrome&logoColor=black)](https://ctftracker.com)
[![Live Portfolio](https://img.shields.io/badge/Live_Portfolio-0xdnd.github.io-00e58d?style=flat-square&logo=googlechrome&logoColor=black)](https://0xdnd.github.io/)

</div>
