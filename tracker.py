from flask import Flask, request
import datetime
import os

app = Flask(__name__)


@app.route('/track')
def track_visitor():
    # Get visitor's IP address
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        visitor_ip = request.environ['REMOTE_ADDR']
    else:
        visitor_ip = request.environ['HTTP_X_FORWARDED_FOR']

    # Log the visit with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {visitor_ip} | User-Agent: {request.user_agent.string}\n"

    # Save to file
    with open('visits.log', 'a') as log_file:
        log_file.write(log_entry)

    # Display confirmation (for the visitor)
    return "<h1>Security Awareness Exercise</h1><p>This is a controlled academic exercise.</p>"


if __name__ == '__main__':
    # Make sure the log file exists
    if not os.path.exists('visits.log'):
        open('visits.log', 'w').close()

    app.run(host='0.0.0.0', port=8080)