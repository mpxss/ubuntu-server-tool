#!/bin/bash
echo "🚀 Installing Ubuntu Server Tool..."
curl -fsSL https://raw.githubusercontent.com/mpxss/ubuntu-server-tool/main/toool -o toool && \
chmod +x toool && \
sudo mv toool /usr/local/bin/ && \
echo "✅ toool installed! Run: toool"
