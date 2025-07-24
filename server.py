#!/usr/bin/env python3
"""
Simple HTTP server for Medical Dashboard
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    PORT = 8000
    HOST = 'localhost'
    
    # Change to the directory containing the HTML files
    web_dir = Path(__file__).parent
    os.chdir(web_dir)
    
    # Create server
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Medical Dashboard Server running at:")
        print(f"🌐 http://{HOST}:{PORT}")
        print(f"📁 Serving files from: {web_dir}")
        print("\n📊 Open the URL above in your browser to view the dashboard")
        print("Press Ctrl+C to stop the server")
        
        try:
            # Try to open browser automatically
            webbrowser.open(f'http://{HOST}:{PORT}')
        except Exception as e:
            print(f"Could not auto-open browser: {e}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")
            sys.exit(0)

if __name__ == '__main__':
    main()