import sys

import requests
import cv2
import numpy as np

# Replace with the IP address of your GoPro (usually 10.5.5.9)
gopro_ip = "10.5.5.9"
timeout_duration = 5  # Set timeout duration in seconds


# Function to switch to photo mode
def switch_to_photo_mode():
    switch_mode_url = f"http://{gopro_ip}/gp/gpControl/command/mode?p=1"
    try:
        response = requests.get(switch_mode_url, timeout=timeout_duration)
        response.raise_for_status()
        print("Switched to photo mode")
    except requests.exceptions.Timeout:
        print("The request timed out. Please check your connection and try again.")
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the GoPro. Ensure the camera is on and Wi-Fi is connected.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


# Function to capture a photo
def capture_gopro_photo():
    capture_photo_url = f"http://{gopro_ip}/gp/gpControl/command/shutter?p=1"
    try:
        response = requests.get(capture_photo_url, timeout=timeout_duration)
        response.raise_for_status()
        print("Photo captured")
    except requests.exceptions.Timeout:
        print("The request timed out. Please check your connection and try again.")
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the GoPro. Ensure the camera is on and Wi-Fi is connected.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


# Function to download the latest photo
def download_latest_photo():
    media_list_url = f"http://{gopro_ip}/gp/gpMediaList"
    try:
        response = requests.get(media_list_url, timeout=timeout_duration)
        response.raise_for_status()
        media_list = response.json()

        # Get the URL of the latest photo
        media = media_list['media'][0]
        last_folder = media['d']
        last_file = media['fs'][-1]['n']
        photo_url = f"http://{gopro_ip}:8080/videos/DCIM/{last_folder}/{last_file}"

        # Download the photo
        photo_response = requests.get(photo_url, timeout=timeout_duration)
        photo_response.raise_for_status()
        photo_data = np.frombuffer(photo_response.content, np.uint8)
        image = cv2.imdecode(photo_data, cv2.IMREAD_COLOR)

        return image
    except requests.exceptions.Timeout:
        print("The request timed out. Please check your connection and try again.")
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the GoPro. Ensure the camera is on and Wi-Fi is connected.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


# Function to display the photo
def display_photo(image):
    cv2.imshow('GoPro Photo', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


import time


# Connect to wifi with ssid network1
# password network1_password


import subprocess


def connect_to_wifi_macos(ssid, password):
    print(f"Connect to wifi {ssid=}")
    # Check if the os is macos:
    if sys.platform == "darwin":
        # Disconnect from any current Wi-Fi networks
        subprocess.run(['networksetup', '-setairportpower', 'en0', 'off'])
        subprocess.run(['networksetup', '-setairportpower', 'en0', 'on'])

        # Connect to the specified network
        subprocess.run(['networksetup', '-setairportnetwork', 'en0', ssid, password])
    elif sys.platform == "linux":
        subprocess.run(['nmcli', 'd', 'wifi', 'connect', ssid, 'password', password], check=True)

connect_to_wifi_macos("GP24903298", "b2b-qGC-mQk")
time.sleep(5)

# Example usage
switch_to_photo_mode()
time.sleep(2)
# capture_gopro_photo()
# time.sleep(5)
capture_gopro_photo()
time.sleep(5)


photo = download_latest_photo()
if photo is not None:
    display_photo(photo)

# Wait a few seconds to ensure the photo is saved
connect_to_wifi_macos("Landgoed Kakelbont", "29222EEC3D")
