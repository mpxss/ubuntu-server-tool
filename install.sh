#!/bin/bash
echo "🚀 Installing Ubuntu Server Tool..."
curl -fsSL https://raw.githubusercontent.com/mpxss/helpbox/main/helpbox.py -o helpbox && \
chmod +x helpbox && \
sudo mv toool /usr/local/bin/ && \
echo "✅ toool installed! Run: toool"
