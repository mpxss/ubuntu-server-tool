#!/usr/bin/env python3
import os

def clear_screen():
    os.system('clear')

def wait_for_enter():
    input("\nPress Enter to return to the menu...")

def run_cmd(cmd, show_output=True):
    exit_code = os.system(cmd)
    if exit_code == 0 and show_output:
        print("✓ Command executed successfully.")
    elif show_output:
        print("✗ Error executing command.")

# ===========================================
# DNS SETTINGS
# ===========================================
def dns_menu():
    while True:
        clear_screen()
        print("DNS Menu:\n")
        print("1. Google DNS (8.8.8.8)")
        print("2. Cloudflare DNS (1.1.1.1)") 
        print("3. OpenDNS (208.67.222.222)")
        print("4. DynX Anti-Sanction")
        print("5. Unbound DNS (Advanced)")
        print("6. Back")
        
        choice = input("\nSelect option: ")
        
        if choice == '1':
            dns_google()
        elif choice == '2':
            dns_cloudflare()
        elif choice == '3':
            dns_opendns()
        elif choice == '4':
            dns_dynx()
        elif choice == '5':
            setup_unbound_advanced()
        elif choice == '6':
            break

def dns_google():
    cmds = [
        "sudo chattr -i /etc/resolv.conf",
        "sudo systemctl stop systemd-resolved",
        "sudo systemctl disable systemd-resolved", 
        "sudo rm /etc/resolv.conf",
        "bash -c 'echo -e \"nameserver 8.8.8.8\\nnameserver 8.8.4.4\" > /etc/resolv.conf'",
        "sudo chattr +i /etc/resolv.conf"
    ]
    for cmd in cmds: run_cmd(cmd, False)
    print("\n✓ Google DNS applied successfully!")
    wait_for_enter()

def dns_cloudflare():
    cmds = [
        "sudo chattr -i /etc/resolv.conf",
        "sudo systemctl stop systemd-resolved",
        "sudo systemctl disable systemd-resolved",
        "sudo rm /etc/resolv.conf", 
        "bash -c 'echo -e \"nameserver 1.1.1.1\\nnameserver 1.0.0.1\" > /etc/resolv.conf'",
        "sudo chattr +i /etc/resolv.conf"
    ]
    for cmd in cmds: run_cmd(cmd, False)
    print("\n✓ Cloudflare DNS applied successfully!")
    wait_for_enter()

def dns_opendns():
    cmds = [
        "sudo chattr -i /etc/resolv.conf",
        "sudo systemctl stop systemd-resolved",
        "sudo systemctl disable systemd-resolved",
        "sudo rm /etc/resolv.conf",
        "bash -c 'echo -e \"nameserver 208.67.222.222\\nnameserver 208.67.220.220\" > /etc/resolv.conf'",
        "sudo chattr +i /etc/resolv.conf"
    ]
    for cmd in cmds: run_cmd(cmd, False)
    print("\n✓ OpenDNS applied successfully!")
    wait_for_enter()

def dns_dynx():
    cmds = [
        "sudo chattr -i /etc/resolv.conf",
        "sudo systemctl stop systemd-resolved",
        "sudo systemctl disable systemd-resolved",
        "sudo rm /etc/resolv.conf",
        "bash -c 'echo -e \"nameserver 10.139.177.18\\nnameserver 10.139.177.16\" > /etc/resolv.conf'",
        "sudo chattr +i /etc/resolv.conf"
    ]
    for cmd in cmds: run_cmd(cmd, False)
    print("\n✓ DynX DNS applied successfully!")
    wait_for_enter()

# ===========================================
# UNBOUND DNS
# ===========================================
def setup_unbound_advanced():
    clear_screen()
    print("Installing Unbound DNS (Advanced)...\n")
    
    os.system("sudo apt update -y && sudo apt install -y unbound")
    
    unbound_conf = """server:
    interface: 127.0.0.1
    port: 53
    do-ip4: yes
    do-udp: yes
    do-tcp: yes
    cache-max-ttl: 86400
    prefetch: yes
    access-control: 127.0.0.0/8 allow
    
    forward-zone:
        name: "."
        forward-addr: 8.8.8.8
        forward-addr: 1.1.1.1
"""
    
    with open("/tmp/unbound.conf", "w") as f:
        f.write(unbound_conf)
    os.system("sudo cp /tmp/unbound.conf /etc/unbound/unbound.conf")
    os.system("sudo unbound-checkconf")
    os.system("sudo systemctl restart unbound")
    
    cmds = [
        "sudo chattr -i /etc/resolv.conf",
        "sudo rm /etc/resolv.conf",
        "echo 'nameserver 127.0.0.1' | sudo tee /etc/resolv.conf",
        "sudo chattr +i /etc/resolv.conf"
    ]
    for cmd in cmds: os.system(cmd)
    
    print("\n✓ Unbound DNS installed & configured!")
    wait_for_enter()

# ===========================================
# UPTIME KUMA
# ===========================================
def install_uptime_kuma():
    clear_screen()
    print("Installing Uptime Kuma (Port 3001)...\n")
    
    uptime_compose = """version: '3.3'
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    volumes:
      - /opt/uptime-kuma:/app/data
    ports:
      - 3001:3001
    restart: always
"""
    
    with open("/tmp/uk.yml", "w") as f:
        f.write(uptime_compose)
    
    cmds = [
        "sudo apt install -y docker.io docker-compose",
        "sudo systemctl enable docker --now",
        "sudo mkdir -p /opt/uptime-kuma",
        "sudo chown -R 1000:1000 /opt/uptime-kuma",
        "sudo cp /tmp/uk.yml /opt/uptime-kuma/docker-compose.yml",
        "cd /opt/uptime-kuma && sudo docker-compose up -d",
        "sudo ufw allow 3001/tcp comment 'Uptime Kuma'"
    ]
    
    for cmd in cmds:
        print(f"Running: {cmd}")
        os.system(cmd)
    
    print("\n✓ Uptime Kuma Ready!")
    print("URL: http://YOUR_IP:3001")
    print("Data: /opt/uptime-kuma")
    wait_for_enter()

# ===========================================
# N8N
# ===========================================
def install_n8n():
    clear_screen()
    print("Installing n8n (Port 5678)...\n")
    
    n8n_compose = """version: '3.3'
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: always
    ports:
      - 5678:5678
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=n8n123456
      - N8N_HOST=0.0.0.0
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - N8N_SECURE_COOKIE=false
    volumes:
      - /opt/n8n:/home/node/.n8n
"""
    
    with open("/tmp/n8n.yml", "w") as f:
        f.write(n8n_compose)
    
    cmds = [
        "sudo mkdir -p /opt/n8n",
        "sudo chown -R 1000:1000 /opt/n8n",
        "sudo cp /tmp/n8n.yml /opt/n8n/docker-compose.yml",
        "cd /opt/n8n && sudo docker-compose up -d",
        "sudo ufw allow 5678/tcp comment 'n8n'"
    ]
    
    for cmd in cmds:
        print(f"Running: {cmd}")
        os.system(cmd)
    
    print("\nWaiting for n8n (30s)...")
    os.system("sleep 30")
    
    print("\n✓ n8n Ready!")
    print("URL: http://YOUR_IP:5678")
    print("Login: admin / n8n123456")
    wait_for_enter()

# ===========================================
# NGINX
# ===========================================
def install_nginx():
    clear_screen()
    print("Installing Nginx Webserver...\n")
    
    cmds = [
        "sudo apt update -y",
        "sudo apt install -y nginx",
        "sudo systemctl enable nginx --now",
        "sudo ufw allow 'Nginx Full'",
        "sudo rm -f /var/www/html/index.nginx-debian.html",
        "echo '<h1>Nginx Ready!</h1><p>Your Ubuntu Server Tool installed Nginx successfully!</p>' | sudo tee /var/www/html/index.html"
    ]
    
    for cmd in cmds:
        print(f"Running: {cmd}")
        os.system(cmd)
    
    print("\n✓ Nginx Ready!")
    print("URL: http://YOUR_IP")
    print("Files: /var/www/html")
    wait_for_enter()

# ===========================================
# OTHER TOOLS
# ===========================================
def speed_test():
    clear_screen()
    print("Running Speed Test...\n")
    os.system("wget -qO- bench.sh | bash")
    wait_for_enter()

def show_cpu_info():
    clear_screen()
    os.system("lscpu")
    wait_for_enter()

def task_running():
    clear_screen()
    os.system("sudo apt install -y htop && htop")
    wait_for_enter()

def block_ip_menu():
    clear_screen()
    print("Block Country IPs:\n1. Israel\n2. UK\n3. USA\n4. Netherlands\n5. China/India\n6. Back")
    urls = {
        '1': 'https://mtpstatus.ir/blockips-is.sh',
        '2': 'https://mtpstatus.ir/block-ips-uk.sh', 
        '3': 'https://mtpstatus.ir/blockipusa.sh',
        '4': 'https://mtpstatus.ir/blocknl.sh',
        '5': 'https://mtpstatus.ir/block_ch-in-hg-ips.sh'
    }
    choice = input("Choice: ")
    if choice in urls:
        os.system(f"wget -q {urls[choice]} && chmod +x $(basename {urls[choice]}) && sudo ./$(basename {urls[choice]})")
        print("\n✓ IP blocking applied!")
    wait_for_enter()

def update_time():
    os.system("sudo timedatectl set-ntp true")
    print("\n✓ Time synchronized!")
    wait_for_enter()

def change_ssh_port():
    clear_screen()
    port = input("New SSH port: ")
    os.system(f"sudo sed -i '/^#*Port /d' /etc/ssh/sshd_config")
    os.system(f"echo 'Port {port}' | sudo tee -a /etc/ssh/sshd_config")
    os.system("sudo systemctl restart sshd")
    print(f"\n✓ SSH port changed to {port}!")
    print("Update your firewall rules!")
    wait_for_enter()

def disable_ping():
    os.system("sudo sed -i 's/ACCEPT/DROP/g' /etc/ufw/before.rules -i '/icmp/'")
    print("\n✓ Ping disabled!")
    wait_for_enter()

# ===========================================
# MAIN MENU
# ===========================================
def main_menu():
    while True:
        clear_screen()
        print("=== Ubuntu Server Tool v2.0 ===\n")
        print("1. DNS Settings")
        print("2. Speed Test (bench.sh)")
        print("3. CPU Info")
        print("4. Block Country IPs")
        print("5. Nginx Webserver (Port 80)")
        print("6. Uptime Kuma (Port 3001)")
        print("7. n8n Automation (Port 5678)")
        print("8. Update Time")
        print("9. Change SSH Port")
        print("10. Disable Ping")
        print("11. htop")
        print("12. Exit")
        print()
        
        choice = input("Select option: ")
        
        if choice == '1': dns_menu()
        elif choice == '2': speed_test()
        elif choice == '3': show_cpu_info()
        elif choice == '4': block_ip_menu()
        elif choice == '5': install_nginx()
        elif choice == '6': install_uptime_kuma()
        elif choice == '7': install_n8n()
        elif choice == '8': update_time()
        elif choice == '9': change_ssh_port()
        elif choice == '10': disable_ping()
        elif choice == '11': task_running()
        elif choice == '12': break

if __name__ == "__main__":
    main_menu()
