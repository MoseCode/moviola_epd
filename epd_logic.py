# from flask import jsonify
import logging
import json
import subprocess
import socket
from epd_code.constants import *
from pathlib import Path


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Load ip addresses and hostnames from ip_config.json into IP_HOSTNAME_MAP
ip_config_path = Path("epd_code/ip_config.json")

if ip_config_path.exists():
    with open(ip_config_path, "r") as file:
        config_json = json.load(file)
        # Create a dictionary mapping from IP addresses to host names
        IP_HOSTNAME_MAP = {
            pod["ip_address"]: pod["hostname"] for pod in config_json["pods"]
        }
else:
    # If the ip_config.json file cannot be found, log an error and proceed with an empty map
    logger.error(f"Cannot locate ip_config.json file at {ip_config_path.absolute()}")
    IP_HOSTNAME_MAP = {}


# Define route for the '/' directory. By default, it will render the 'login.html' file
def login():
    # return render_template('login.html',pass_required=PASS_REQUIRED)
    pass


def is_host_reachable(host: str, port: int = 80, timeout: int = 2) -> bool:
    """
    Check if the specified host is reachable on the provided port.
    This function uses port EP_PORT by default for the ping which results
    in only responding if it's running this epd_code.
    """

    connection_timeout = timeout  # Connection timeout in seconds

    try:
        socket.create_connection((host, port), connection_timeout)  # Try to connect to the host
        return True
    except (socket.timeout, socket.error):
        return False  # Unable to connect to the host on the specified port


def ping_ips():
    # Logs the execution of the `/ping-ips` endpoint
    logger.info("Running /ping-ips")
    # For each IP from the config, ping it, keep it if it is reachable
    responsive_ips = [
        {"ip": ip, "hostname": get_hostname(ip)}
        for ip in IP_HOSTNAME_MAP.keys()
        if is_host_reachable(ip)
    ]
    # Log and return the list of responsive IPs
    logger.info(f"Responsive IP: {responsive_ips}")
    return responsive_ips


def get_hostname(ip):
    """
    Function retrieves the hostname of a given IP.
    If no hostname is found, it returns 'POD-Unknown'
    """
    my_host = IP_HOSTNAME_MAP.get(ip, "POD-UNKNOWN")
    logger.info(f"Hostname Check: {my_host}")
    return my_host


# Define route for '/data_entry'. Accepts GET and POST methods
# TODO: CREATE DIFFERENT LOOKS FOR THE PODS
def data_entry(self, pod: str, ip: str, name: str, info: str):
    # Get the hostname using the socket library
    hostname = socket.gethostname()

    # Open `data.json` file and read the data about the current pod
    with open("epd_code/data.json", "r") as openFile:
        data = json.load(openFile)
    print(f"Pod Name: {pod}")
    print(f"openFile: {openFile}")
    # Log the data about current pod and render it on the page, also passing pod name
    logger.info(data.get(pod, {}))

    # template_name = 'data_entry.html'  # default template
    # return render_template(template_name, data=data.get(hostname, {}), pod=hostname)


# Define route for '/publish'. This route will update the information stored about a pod
def publish():
    # Get the hostname of the current machine
    hostname = socket.gethostname()
    logger.info(hostname)

    # Get the data provided in the form
    client_name = ""
    client_info = ""
    phone_number = ""
    office_hours = ""

    # Open data.json, update the information about the current pod, and save it
    with open("epd_code/data.json", "r") as openFile:
        data = json.load(openFile)
    data[hostname] = {
        "client_name": client_name,
        "client_info": client_info,
        "phone_number": phone_number,
        "office_hours": office_hours,
        "pod_number": hostname,
    }
    with open("epd_code/data.json", "w") as openFile:
        json.dump(data, openFile, indent=4)
        logger.info(f"dumping to json:{data}")

    print(client_name, client_info, phone_number, office_hours, hostname)

    # send data to the e-paper screen to display
    logger.info("Send Data to e-Paper display")
    subprocess.run(
        [
            "python3",
            "epd_code/epd_display.py",
            client_name,
            client_info,
            phone_number,
            office_hours,
            hostname,
        ]
    )

    # Redirect user to login page after publishing data
    # return redirect(url_for("login"))
