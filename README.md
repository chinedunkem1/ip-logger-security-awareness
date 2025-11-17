📌 Flask Visitor Tracker

A simple and educational Flask web application that logs visitor information such as IP address, user agent, and timestamp. This project is intended for cybersecurity awareness and academic use only, with full consent from all participants.

🔒 Ethical Notice

This project is designed for:

Security awareness

Logging and monitoring demonstrations

Educational experiments

Understanding how web servers process client metadata

⚠️ All testing must be done with consent.
This project does not perform scanning, exploitation, or unauthorized activity.

🚀 Features

Logs visitor IP address

Detects proxied IP (X-Forwarded-For)

Captures browser user agent

Adds timestamps to each visit

Saves entries to visits.log

Returns a friendly confirmation page

🧰 Technologies Used

Python 3

Flask

Ngrok (optional, for external access)

⚠️ Privacy & Consent

This application collects:

IP address

User-agent string

Timestamp

These are standard analytics fields used by websites.
Always obtain user consent before logging this information.

## 🔐 What Can Be Done with a Captured IP Address?

This project logs visitor IP addresses for educational and security-awareness purposes. With user consent, a public IP can be used for:

- Approximate geolocation (city/country)
- Identifying VPN/proxy usage
- Security monitoring and detecting suspicious activity
- Rate limiting or blocking malicious traffic
- Basic network diagnostics

A public IP **cannot** be used to hack, locate someone precisely, access their device, or retrieve personal data.

This project strictly follows ethical and educational guidelines.

## Screen Shots
<img width="1106" height="452" alt="Screenshot 2025-11-17 110358" src="https://github.com/user-attachments/assets/16b6a013-0195-4161-9934-477263fc1f34" />
This screenshot shows ngrok successfully exposing the local Flask server to the internet.
Ngrok assigns a secure public URL (https://jackqueline-preradio-unlugubriously.ngrok-free.dev) which forwards all incoming traffic to the local application

<img width="1875" height="331" alt="Screenshot 2025-11-17 110930" src="https://github.com/user-attachments/assets/1f9e3af8-1286-4ab3-ae8a-b5041c385eec" />
This screenshot shows the raw entries recorded in visits.log. Each line includes the timestamp, the visitor’s IP address (blurred), and the User-Agent information that identifies the device or app making the request. You can also see automated link preview requests from apps like Snapchat and WhatsApp, which appear when the link is shared. This demonstrates that the tracker is capturing and logging all incoming visits correctly.

<img width="1877" height="756" alt="image" src="https://github.com/user-attachments/assets/74366486-9a0d-47e2-a025-27b57f455ca6" />
This screenshot shows the process of installing Flask and starting the application locally. Once Flask finishes installing, the server launches and begins listening on port 8080, confirming that the application is running correctly and ready to receive requests. The lines showing Running on http://127.0.0.1:8080 and http://192.168.0.8:8080 indicate that the server is accessible both locally and on the local network


## How to Use This Project

1)Clone or download the project (git clone https://github.com/YOUR-USERNAME/flask-visitor-tracker.git)

2)Install the required package(pip install flask)

3)Run the Flask app(python tracker.py)
The server will start on:
http://127.0.0.1:8080

4)Expose it using ngrok
If you want others to access it externally, run:
ngrok http 8080

5)Use the HTTPS link that ngrok provides.

6)View the logs
Every visit to /track is recorded in:

visits.log
