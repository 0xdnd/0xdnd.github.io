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
  <div class="title">SOC Tier 1 Analyst &amp; Penetration Testing Specialist (CPTS Candidate)</div>
  <div class="contacts">
    <span>Israel &nbsp;|&nbsp; 054-912-0911</span>
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
  <div class="section-title">Professional Profile</div>
  <p class="summary-text">
    Adversary-aware cybersecurity practitioner bridging <strong>650 hours of enterprise infrastructure &amp; SOC engineering at ITQ College</strong> with offensive penetration testing tradecraft (<strong>50+ targets rooted</strong> across Hack The Box &amp; TryHackMe, CPTS track in-progress). Hands-on configuring dual-domain Active Directory forests, Sysmon telemetry, and engineering detection rules in both <strong>Splunk (SPL)</strong> and <strong>IBM QRadar</strong>. Creator of <strong>ZeroBox (ctftracker.com)</strong>, an open-source tactical CTF cockpit. Proven operational discipline under strict SLAs and incident escalation from 3 years of military service as an IDF Service Coordinator.
  </p>
</div>

<div class="section">
  <div class="section-title">Technical Proficiencies</div>
  <div class="skills-list">
    <div class="skill-row"><span class="skill-label">SIEM &amp; Detection Engineering:</span> Splunk Enterprise (SPL), IBM QRadar SIEM, Sysmon (EID 1, 3, 10, 13), Windows Security Logs (EID 4624, 4625, 4720, 4769), WinCollect, Wireshark, tcpdump.</div>
    <div class="skill-row"><span class="skill-label">Enterprise Infrastructure &amp; Defense:</span> Cisco IOS XE (VLANs, OSPF, STP, EtherChannel, ACLs, NAT), Fortinet FortiGate NGFW (Stateful Policies, IPsec VPN, WIPS), Active Directory (GPOs, Domain Trees, Kerberos, DNS/DHCP), Linux (Kali, Ubuntu).</div>
    <div class="skill-row"><span class="skill-label">Offensive Security &amp; Exploitation:</span> 50+ Rooted Machines (HTB &amp; THM), 2 Active Live Season Roots (Reactor &amp; Kobold), AD Attacks (Kerberoasting, AS-REP Roasting, BloodHound / SharpHound), Nmap, Burp Suite, ffuf, Metasploit, Hashcat, Hydra, OWASP Top 10.</div>
    <div class="skill-row"><span class="skill-label">Scripting, Tools &amp; Operations:</span> Python 3, Bash, PowerShell, Regular Expressions (RegEx), Git/GitHub, SAP ERP, CRM Incident Ticketing.</div>
    <div class="skill-row"><span class="skill-label">Languages:</span> Hebrew (Native), English (Full Technical &amp; Operational Proficiency).</div>
  </div>
</div>

<div class="section">
  <div class="section-title">Flagship Security Implementations &amp; Homelab</div>
  
  <div class="entry">
    <div class="entry-header">
      <span class="entry-title"><a href="https://ctftracker.com" target="_blank">ZeroBox (ctftracker.com)</a> &mdash; Open Source CTF Cockpit &amp; Exam Simulator</span>
      <span class="entry-dates">2025 &ndash; Present</span>
    </div>
    <div class="entry-role">Creator &amp; Lead Architect | Open Source (<a href="https://github.com/0xdnd/ctf-tracker" target="_blank">github.com/0xdnd/ctf-tracker</a>)</div>
    <ul class="bullets">
      <li>Architected and shipped an offline-first tactical cyber cockpit indexing <strong>1,090+ CTF machines</strong> and <strong>131+ reverse shell vectors</strong> with dynamic parameter injection.</li>
      <li>Engineered 100% client-side data isolation utilizing browser IndexedDB &amp; LocalStorage, achieving <strong>sub-10ms catalog querying</strong> with zero cloud accounts or external telemetry.</li>
      <li>Built 5 timed 24-hour certification exam tracks (OSCP, CPTS, CRTO, OSEP, CRTP), interactive pivot/attack graphing with Obsidian <code>.canvas</code> export, and native desktop builds via Tauri.</li>
    </ul>
  </div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Enterprise Active Directory Homelab &amp; Sysmon Detection</span>
      <span class="entry-dates">2025</span>
    </div>
    <div class="entry-role">Security Architect &amp; Detection Engineer</div>
    <ul class="bullets">
      <li>Deployed a dual-domain Windows Server 2022 Active Directory forest with dedicated Windows 10 endpoints, Kali Linux attack node, and Splunk SIEM via Universal Forwarders.</li>
      <li>Implemented SwiftOnSecurity modular Sysmon telemetry auditing process creation (EID 1), network connections (EID 3), and LSASS memory access (EID 10).</li>
      <li>Engineered 5 production-grade Splunk SPL correlation rules detecting Kerberoasting (EID 4769 with RC4 encryption <code>0x17</code>), AS-REP roasting, and PsExec lateral movement with zero false positives.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Practical Training &amp; Offensive Security</div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">ITQ College &mdash; Cyber &amp; Information Security Specialist</span>
      <span class="entry-dates">2024 &ndash; 2025</span>
    </div>
    <div class="entry-role">650 Hands-on Training Hours | Cisco &amp; Fortinet Specialization</div>
    <ul class="bullets">
      <li>Completed 650 hours of enterprise infrastructure &amp; defense training: Cisco IOS XE routing &amp; switching, Fortinet FortiGate NGFW configuration, and Linux system administration.</li>
      <li>Hardened Windows Server 2022 Active Directory domains via Group Policy Objects (GPOs), remote access, and service account isolation.</li>
      <li>Practiced Tier-1 SOC alert triage and incident correlation in IBM QRadar SIEM, configuring WinCollect log forwarding and FortiGate firewall syslog integration.</li>
    </ul>
  </div>

  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Hack The Box Academy &amp; Continuous CTF Validation</span>
      <span class="entry-dates">2025 &ndash; Present</span>
    </div>
    <div class="entry-role">Offensive Tradecraft &amp; Validation (50+ Rooted Targets)</div>
    <ul class="bullets">
      <li>Compromised <strong>50+ standalone targets</strong> across Hack The Box and TryHackMe, including <strong>2 active live-season HTB roots</strong> (<code>Reactor</code> &amp; <code>Kobold</code>) and the complete HTB Starting Point tier.</li>
      <li>Actively pursuing <strong>Certified Penetration Testing Specialist (CPTS)</strong> and <strong>CWES</strong> tracks, completing 30+ enterprise modules (PrivEsc, Web Proxies, Broken Auth, Footprinting).</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Operational Military Service</div>
  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Service Coordinator &mdash; Soldier Benefits | Israel Defense Forces (IDF)</span>
      <span class="entry-dates">2022 &ndash; 2025 (3 Years)</span>
    </div>
    <ul class="bullets">
      <li>Managed high-volume, sensitive operational requests and entitlements under strict SLAs, confidentiality, and time pressure.</li>
      <li>Executed structured database queries and record processing in SAP ERP; prioritized, documented, and tracked incident lifecycles in CRM ticketing systems.</li>
      <li>Maintained high-urgency stakeholder escalation and cross-functional communication protocols with military commanders and external agencies.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <div class="entry">
    <div class="entry-header">
      <span class="entry-title">Computer Science Specialization (10 Units) &mdash; High School Diploma</span>
      <span class="entry-dates">2020 &ndash; 2022</span>
    </div>
    <p class="summary-text" style="margin-top:1.5px; font-size:8.1pt;">
      Graduation Project: Developed an Android mobile application in Java for real-time cryptocurrency valuation tracking and currency conversion via REST API integration.
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
        await page.screenshot(path='resume_preview.png', full_page=True)
        pdf_bytes = await page.pdf(
            format='A4',
            print_background=True,
            margin={'top': '8mm', 'bottom': '8mm', 'left': '12mm', 'right': '12mm'}
        )
        with open('resume_new.pdf', 'wb') as f:
            f.write(pdf_bytes)
        await browser.close()

asyncio.run(generate())

reader = pypdf.PdfReader('resume_new.pdf')
print(f'NEW RESUME COMPILED! Total pages: {len(reader.pages)}')

