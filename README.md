# Sentinel-Static-Forensics
I developed this tool to support law enforcement in the initial phases of a cyber investigation. It automates the extraction of digital fingerprints to ensure evidence integrity and performs static analysis to identify malicious IP addresses and URLs within a secure VirtualBox environment.

# Sentinel-Static: Forensic Triage & Malware Analysis Tool

## 📌 Project Overview
Sentinel-Static is a lightweight digital forensics utility developed to assist law enforcement during the initial "triage" phase of a cybercrime investigation. It allows investigators to safely analyze suspicious artifacts in an isolated environment (such as Kali Linux or VirtualBox) to gather intelligence without risking system infection.

## ✨ Key Features
*   **Evidence Integrity (Hashing):** Automatically generates MD5 and SHA256 cryptographic hashes to ensure the "Chain of Custody" and prove evidence has not been tampered with.
*   **Static Analysis:** Performs non-invasive "X-ray" scans of binary data to extract readable strings, IP addresses, and URLs.
*   **Indicator of Compromise (IOC) Detection:** Uses pattern matching to identify potential command-and-control (C2) infrastructure hidden within files.
*   **Robust Error Handling:** Designed for production use with path-validation and safe-reading protocols.

## 🛠️ Built With
*   **Python 3.x**
*   **Regex** (Pattern Matching)
*   **Hashlib** (Cryptographic Hashing)

## 🚀 Getting Started
### Prerequisites
Ensure you have Python installed. This tool uses standard libraries, so no external installations are required.

### Execution
Run the script from your terminal (VS Code, Kali, or CMD) by passing the target file as an argument:
```bash
python sentinel.py <target_file_name>
