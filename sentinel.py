import hashlib
import sys
import re
import os

def analyze_file(file_path):
    # Check if file exists to avoid crashes
    if not os.path.exists('V:\AIML\CS1_Keys.pdf'):
        print(f"Error: File '{'file_path'}' not found.")
        return

    # Use raw strings (fr"") to prevent Windows path escape character warnings
    print(fr"--- Analyzing: {'file_path'} ---")
    
    try:
        with open('file_path', "rb") as f:
            data = f.read()
            
            # 1. Evidence Integrity: Generate Digital Fingerprints
            md5_hash = hashlib.md5(data).hexdigest()
            sha256_hash = hashlib.sha256(data).hexdigest()
            
            print(f"MD5: {md5_hash}")
            print(f"SHA256: {sha256_hash}")

            # 2. Forensic Triage: Extract Potential Indicators of Compromise (IOCs)
            # This regex searches for printable strings, IPs, and basic URLs
            strings = re.findall(rb"[a-zA-Z0-9\.\:\/]{4,}", data)
            
            print("\n--- Potential Indicators of Compromise (IOCs) ---")
            if not strings:
                print("No clear string indicators found.")
            else:
                # Show unique findings to keep output clean for investigators
                unique_strings = sorted(list(set(strings)))
                for s in unique_strings[:20]: # Display top 20 unique indicators
                    print(s.decode('ascii', errors='ignore'))
                    
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_file(sys.argv[1])
    else:
        print("Usage: python sentinel.py <file_to_scan>")
