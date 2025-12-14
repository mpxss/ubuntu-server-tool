# 🎯 آموزش هلپباکس

ابزار کامل قابل اجرا در اوبونتو 20 به بالا با **یک کلیک**!

## ✨ **ویژگی‌ها**
| گزینه | سرویس | پورت | توضیح |
|-------|--------|------|-------|
| 1 | DNS Settings | - | Google/Cloudflare/OpenDNS/DynX/Unbound |
| 2 | Speed Test | - | bench.sh کامل |
| 3 | CPU Info | - | lscpu |
| 4 | Block IPs | - | 5 کشور (Israel/UK/USA/NL/China) |
| **5** | **Nginx** | **80** | وب سرور کامل |
| 6 | Uptime Kuma | **3001** | مانیتورینگ |
| 7 | n8n | **5678** | اتوماسیون |
| 8 | Update Time | - | NTP sync |
| 9 | SSH Port | - | تغییر پورت |
| 10 | Disable Ping | - | ضد Ping |
| 11 | htop | - | مانیتورینگ سیستم |

## 🚀 **نصب (2 روش)**

### **روش 1: خودکار (1 خط)**
```bash
curl -fsSL https://raw.githubusercontent.com/mpxss/ubuntu-server-tool/main/toool.py -o toool && \
chmod +x toool && \
sudo mv toool /usr/local/bin/toool && \
toool

