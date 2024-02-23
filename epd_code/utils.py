import os
from PIL import Image, ImageDraw, ImageFont
from constants import *
import time

def schedule_shutdown(minutes):
    """Shutdown system after specific minutes."""
    # Check if shutdown has been turned off in constants.py
    if SHUTDOWN_SYSTEM == False:
        return None
    # Windows specific command. Use 'shutdown -h {time}' for Unix
    shutdown_command = f'shutdown -h +{minutes}'

    # Execute the command
    os.system(shutdown_command)


# Function to reduce font size until text fits
def adjust_font_size(text, font_path, initial_font_size, max_width):
    """
    Adjusts the font size based on the length of the text.

    Parameters:
    text (str): The text whose font size is to be adjusted.
    baseline_size (int): The size of the font at the beginning.

    Returns:
    int: The adjusted font size.
    """

    try:
        font = ImageFont.truetype(font_path, initial_font_size)
        while font.getsize(text)[0] > max_width:
            font = ImageFont.truetype(font_path, font.size - 1)
        return font
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error or return a default font
        return ImageFont.truetype(font_path, 20)  # Example default font size
    finally:
        print("Done finding width of font")


def calculate_text_sizes(font, text):
    """Calculates and returns the size of a text given a font"""
    return font.getsize(text)


def calculate_phone_number_x(is_client_size_larger, client_name_x, phone_number_size):
    """Calculates and returns the X coordinate of the phone number"""
    if is_client_size_larger:
        return client_name_x + 20
    else:
        phone_number_x = client_name_x - (phone_number_size[0] / 2)
        return max(phone_number_x, 10)


def calculate_office_hours_x(is_client_size_larger, client_name_x, client_name_size, office_hours_size):
    """Calculates and returns the X coordinate of the office hours"""
    if is_client_size_larger:
        return client_name_x + client_name_size[0] - office_hours_size[0] - 20
    else:
        office_hours_x = client_name_x + client_name_size[0] - (office_hours_size[0] / 2)
        return min(office_hours_x, MAX_WIDTH - office_hours_size[0])


def calculate_client_info_x(client_info_size):
    """Calculates and returns the X coordinate of the client information"""
    return ((SCREEN_WIDTH /2) - (client_info_size[0]/2))

