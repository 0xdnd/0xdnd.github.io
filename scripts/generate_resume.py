import asyncio
from playwright.async_api import async_playwright
import pypdf

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Daniel Dayan - Resume</title>
<style>
  @page {
    size: A4;
    margin: 8mm 12mm 8mm 12mm;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.28;
    font-size: 8.5pt;
    -webkit-font-smoothing: antialiased;
  }
  a {
    color: #0284c7;
    text-decoration: none;
  }
  .header {
    text-align: center;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 7px;
  }
  .name {
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: 1.8px;
    color: #0f172a;
    text-transform: uppercase;
    margin-bottom: 2px;
  }
  .title {
    font-size: 9.8pt;
    font-weight: 700;
    color: #0284c7;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    text-transform: uppercase;
  }
  .contacts {
    font-size: 8.2pt;
    color: #475569;
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
  }
  .contacts span {
    display: inline-flex;
    align-items: center;
  }
  .contacts a {
    color: #334155;
    font-weight: 600;
  }
  .section {
    margin-bottom: 6px;
  }
  .section-title {
    font-size: 8.8pt;
    font-weight: 800;
    text-transform: uppercase;
    color: #0f172a;
    letter-spacing: 0.8px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-bottom: 3.5px;
  }
  .summary-text {
    font-size: 8.3pt;
    color: #334155;
    text-align: justify;
    line-height: 1.3;
  }
  .skills-list {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .skill-row {
    font-size: 8.1pt;
    line-height: 1.25;
    color: #334155;
  }
  .skill-label {
    font-weight: 700;
    color: #0f172a;
  }
  .entry {
    margin-bottom: 4.5px;
  }
  .entry:last-child {
    margin-bottom: 0;
  }
  .entry-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    font-size: 8.6pt;
    font-weight: 700;
    color: #0f172a;
  }
  .entry-title {
    font-weight: 700;
  }
  .entry-role {
    font-weight: 600;
    color: #0284c7;
    font-size: 8.1pt;
  }
  .entry-dates {
    font-size: 8.1pt;
    color: #64748b;
    font-weight: 600;
  }
  ul.bullets {
    margin-top: 1.5px;
    padding-left: 14px;
  }
  ul.bullets li {
    font-size: 8.1pt;
    color: #334155;
    margin-bottom: 1.2px;
    line-height: 1.25;
  }
  ul.bullets li strong {
    color: #0f172a;
  }
</style>
</head>
<body>

<div class="header">
  <div class="name">Daniel Dayan</div>
  <div class="title">Junior SOC Analyst &amp; Junior Penetration Tester</div>
  <div class="contacts" style="margin-bottom:3px;">
    <span>Central Israel &middot; Available immediately &middot; Hebrew &amp; English</span>
  </div>
  <div class="contacts">
    <span>054-912-0911</span>
    <span>&bull;</span>
    <span><a href="mailto:danieldayan2512@gmail.com">danieldayan2512@gmail.com</a></span>
    <span>&bull;</span>
    <span><a href="https://linkedin.com/in/daniel-dayan-a66322352" target="_blank">LinkedIn</a></span>
    <span>&bull;</span>
    <span><a href="https://github.com/0xdnd" target="_blank">GitHub (@0xdnd)</a></span>
    <span>&bull;</span>
    <span><a href="https://ctftracker.com" target="_blank">ctftracker.com</a></span>
    <span>&bull;</span>
    <span><a href="https://0xdnd.github.io" target="_blank">Portfolio (0xdnd.github.io)</a></span>
  </div>
</div>

<div class="section">
  <div class="section-title">Profile</div>
  <p class="summary-text">
    Junior SOC analyst and junior penetration tester. Graduate of the <strong>Cyber Security Implementer Program at ITQ College (650 hours, Cisco and Fortinet specialization)</strong>, where I trained on SIEM/SOC tooling (IBM QRadar SIEM, Splunk SOAR), Cisco and Fortinet. In my own Active Directory lab I practise attack paths such as Kerberoasting and BloodHound recon, and I have rooted <strong>50+ machines across Hack The Box, TryHackMe and picoCTF</strong>. Creator of <strong>ZeroBox (ctftracker.com)</strong>, an open-source pentest workspace with 4,000+ visitors. 3 years as an IDF Service Coordinator working under strict SLAs in SAP ERP and CRM ticketing systems.
  </p>
</div>

<div class="section">
  <div class="section-title">Technical Proficiencies</div>
  <div class="skills-list">
    <div class="skill-row"><span class="skill-label">Defensive Security &amp; SOC:</span> IBM QRadar SIEM, WinCollect Agent, Splunk SOAR, FortiGate NGFW, Antivirus &amp; Web Filtering, Windows Audit Policies, Syslog Forwarding, Alert Triage &amp; Containment, Wireshark, MITRE ATT&amp;CK Mapping.</div>
    <div class="skill-row"><span class="skill-label">Networking &amp; Systems:</span> Cisco IOS XE (VLANs, 802.1Q, OSPF, RIPv2, HSRP, GRE &amp; IPsec VPNs, ACLs, NAT, Port Security), Windows Server 2022 (AD / GPO), DNS / DHCP, LPI Linux Essentials, Kali &amp; Ubuntu (tcpdump, SSH, Netplan), VMware.</div>
    <div class="skill-row"><span class="skill-label">Offensive Security &amp; Pentesting:</span> Nmap, Burp Suite, OWASP ZAP, OWASP Top 10, ffuf, SQLMap, Metasploit, Hydra, Hashcat, Privilege Escalation, Kerberoasting, BloodHound, CVSS v3.1.</div>
    <div class="skill-row"><span class="skill-label">Scripting &amp; Operations:</span> React, TypeScript, Python, Bash, PowerShell, SQL, Git, SAP ERP Workflows, CRM Ticket Triage.</div>
  </div>
</div>

<div class="section">
  <div class="section-title">Projects &amp; Homelab</div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title"><a href="https://ctftracker.com" target="_blank">ZeroBox (ctftracker.com)</a> &mdash; CTF Tracker &amp; Penetration Testing Workspace</span>
      <span class="entry-dates">Open Source</span>
    </div>
    <div class="entry-role">Creator | 4,000+ visitors | <a href="https://github.com/0xdnd/ctf-tracker" target="_blank">github.com/0xdnd/ctf-tracker</a></div>
    <ul class="bullets">
      <li>Offline-first workspace in React and TypeScript, shipped as a web app and a Tauri desktop app: a <strong>1,000+ machine catalog</strong>, <strong>131 reverse shell templates</strong> and an 8-phase methodology.</li>
      <li>Multi-host Nmap XML importer with one-click attack graphs, a masked credential and hash vault, and a CVSS v3.1 Markdown report generator.</li>
      <li>Timed exam simulator (OSCP, CRTO, OSEP, CRTP) with ZIP submission export. Runs fully offline with no accounts and no cloud telemetry; data stays in the browser (IndexedDB / LocalStorage).</li>
    </ul>
  </div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Active Directory Homelab</span>
      <span class="entry-dates">Personal Lab</span>
    </div>
    <ul class="bullets">
      <li>Built an Active Directory domain with <strong>two domain-joined Windows machines</strong>, plus a <strong>Linux VPN server</strong> for remote access to the lab.</li>
      <li>Practise AD attack paths end to end, including <strong>Kerberoasting</strong> and <strong>BloodHound recon</strong>.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Training &amp; Offensive Practice</div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Cyber Security Implementer Program, ITQ College</span>
      <span class="entry-dates">2024 &ndash; 2025</span>
    </div>
    <div class="entry-role">650 hours | Cisco &amp; Fortinet Specialization | Completed alongside the final year of IDF service (IDF-funded civilian program)</div>
    <ul class="bullets">
      <li><strong>Cisco IOS XE</strong> routers &amp; switches: VLANs and 802.1Q trunking, inter-VLAN routing, DHCP, OSPF, RIPv2, HSRP, ACLs, port security, NAT, and GRE and IPsec VPN tunnels.</li>
      <li><strong>FortiGate NGFW</strong>: configured for a simulated two-site enterprise network (Israel and USA): firewall policies, Virtual IPs (static NAT), antivirus and web filtering profiles, and a site-to-site IPsec VPN.</li>
      <li><strong>Windows Server 2022 &amp; Linux</strong>: Active Directory, Group Policy (GPO), NTFS permissions, DHCP with MAC filtering; studied LPI Linux Essentials and administered Kali and Ubuntu.</li>
      <li><strong>IBM QRadar SIEM &amp; Splunk SOAR</strong>: configured QRadar SIEM with the WinCollect agent, Windows audit policies, and syslog forwarding through the FortiGate, and set up Splunk SOAR.</li>
    </ul>
  </div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">CTFs &amp; Hack The Box Academy</span>
      <span class="entry-dates">Ongoing</span>
    </div>
    <ul class="bullets">
      <li><strong>50+ machines rooted</strong> across Hack The Box, TryHackMe and picoCTF, including <strong>2 active-season HTB machines</strong> (Reactor &amp; Kobold); <strong>30 HTB Academy modules</strong> completed (AD, web exploitation &amp; post-exploitation).</li>
      <li><strong>TwoMillion</strong> (HTB): API enumeration, admin via API, command injection in the VPN generator, CVE-2023-0386 OverlayFS kernel privesc. <strong>Blue</strong> (HTB): MS17-010 EternalBlue, SMBv1 (srv.sys) RCE to SYSTEM.</li>
      <li><strong>Cap</strong> (HTB): IDOR on PCAP export, plaintext credential sniffing, Python cap_setuid privesc. <strong>Support</strong> (TryHackMe): web app pentest from vulnerability discovery to remote code execution.</li>
      <li>Currently learning: HTB Academy CPTS and CWES paths.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Military Service</div>
  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Service Coordinator, Soldier Benefits &mdash; Israel Defense Forces (IDF)</span>
      <span class="entry-dates">2022 &ndash; 2025 (3 Years)</span>
    </div>
    <ul class="bullets">
      <li>Investigated and resolved hundreds of sensitive soldier entitlement cases in SAP, maintaining strict data confidentiality and high accuracy under daily SLAs.</li>
      <li>Prioritized and tracked complex escalations through CRM and ticketing workflows, writing clear case notes that sped up coordination between soldiers, commanders and external agencies.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">High School Diploma, Computer Science Major (10 Units)</span>
      <span class="entry-dates">2020 &ndash; 2022</span>
    </div>
    <p class="summary-text" style="margin-top:1.5px; font-size:8.1pt;">
      Final graduation project: native Android app in Java for real-time cryptocurrency prices and currency conversion (USD/EUR/ILS); web development with HTML and CSS.
    </p>
  </div>
</div>

</body>
</html>
"""

async def generate():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 794, 'height': 1123})
        await page.set_content(html_content)
        pdf_bytes = await page.pdf(
            format='A4',
            print_background=True,
            margin={'top': '8mm', 'bottom': '8mm', 'left': '12mm', 'right': '12mm'}
        )
        with open('resume.pdf', 'wb') as f:
            f.write(pdf_bytes)
        await browser.close()

asyncio.run(generate())

reader = pypdf.PdfReader('resume.pdf')
print(f'NEW RESUME COMPILED! Total pages: {len(reader.pages)}')

