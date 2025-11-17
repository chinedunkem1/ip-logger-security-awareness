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
