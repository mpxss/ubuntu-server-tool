#!/bin/bash
echo "🚀 Installing helpbox..."
curl -fsSL https://raw.githubusercontent.com/mpxss/helpbox/main/helpbox.py -o helpbox && \
chmod +x helpbox && \
sudo mv toool /usr/local/bin/ && \
echo "✅ helpbox installed! Run: helpbox"
