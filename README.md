SMTP-Client-and-Logger
This project is a simple SMTP email client combined with a local message logger. It sends emails using Gmail’s SMTP server and simultaneously sends message details (sender, subject, body preview, host information like IP/MAC address) to a local TCP server for logging. This demonstrates network programming, socket communication, and email sending over SMTP in Python. It can be extended into a forensics tool, internal audit logger, SMTP security tester, or SOC email event tracker.

Core features:
-Sends emails via Gmail’s SMTP over SSL
-Logs email metadata to a local server over TCP
-Demonstrates socket programming basics
-Simple message forwarding + host fingerprinting
-Educational example of client-server communication
