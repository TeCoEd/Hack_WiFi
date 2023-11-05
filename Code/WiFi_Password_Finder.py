import subprocess
import re

def run_command(command):
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return None

def get_ssid():
    ssid_output = run_command('netsh wlan show interfaces | findstr SSID')
    return re.search(r'SSID\s+:\s(.+)', ssid_output).group(1) if ssid_output else None

def get_psk(ssid):
    psk_output = run_command('netsh wlan show profile name="{0}" key=clear'.format(ssid))
    return re.search(r'Key\sContent\s+:\s(.+)', psk_output).group(1) if psk_output else None

ssid = get_ssid()
psk = get_psk(ssid) if ssid else None

print("SSID:", ssid if ssid else "SSID not found")
print("PSK:", psk if psk else "PSK not found")
