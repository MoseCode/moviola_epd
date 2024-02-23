#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static/images/"
)
fontdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "static/fonts/"
)

libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from epd_driver import epd7in5b_V2
import time
from constants import *
from PIL import Image, ImageDraw, ImageFont
from utils import *
import traceback

logging.basicConfig(level=logging.INFO)

try:
    # Default values for client information
    client_name = "__PRODUCTION NAME__"
    client_info = "__Client Info__"
    phone_number = "__Client Phone__"
    office_hours = "__Hours of Operation__"
    pod_number = "POD-_"

    # Ensure enough arguments are provided
    if len(sys.argv) != 6:
        print("System did not receive 6 arguments.")
        print(f"number of arguments: {len(sys.argv)}")
    else:
        # Extract the 5 arguments directly into variables
        _, client_name, client_info, phone_number, office_hours, pod_number  = sys.argv

    # Print the updated values
    logging.info(f"Client Name: {client_name}")
    logging.info(f"Client Info: {client_info}")
    logging.info(f"Phone Number: {phone_number}")
    logging.info(f"Office Hours: {office_hours}")
    logging.info(f"POD Number: {pod_number}")

    epd = epd7in5b_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    # Drawing on the Horizontal image
    logging.info("Creating image containers for Black and Red")
    black_Image = Image.new("1", (epd.width, epd.height), 255)  # 255: clear the frame
    red_Image = Image.new("1", (epd.width, epd.height), 255)  # 255: clear the frame
    draw_blkImage = ImageDraw.Draw(black_Image)
    draw_redImage = ImageDraw.Draw(red_Image)

    # Black Background Image
    blk_bg = Image.open(os.path.join(picdir, "black_swipe.bmp"))
    blk_bg = blk_bg.resize((800, 480), Image.LANCZOS)
    black_Image.paste(blk_bg, (0, 0))

    # Red Background Image
    red_bg = Image.open(os.path.join(picdir, "red_swipe.bmp"))
    red_bg = red_bg.resize((800, 480), Image.LANCZOS)
    red_Image.paste(red_bg, (0, 0))

    # Moviola Logo pasted to Red
    m_logo = Image.open(os.path.join(picdir, "moviola_blk.png"))
    m_logo = m_logo.resize((70, 70), Image.LANCZOS)
    red_Image.paste(m_logo, (465, 120))


    # Load Fonts and adjust the font size to account for client name width.
    font_client_info = ImageFont.truetype(
        os.path.join(fontdir, "Metropolis-Regular.otf"), 30
    )
    font_extra_bold = ImageFont.truetype(
        os.path.join(fontdir, "Metropolis-ExtraBold.otf"), 110
    )
    font_semi_bold = ImageFont.truetype(
        os.path.join(fontdir, "Metropolis-SemiBold.otf"), 20
    )
    font_client_name = adjust_font_size(
        client_name, os.path.join(fontdir, "Metropolis-Black.otf"), 110, MAX_WIDTH
    )

    client_name_size = calculate_text_sizes(font_client_name, client_name)
    phone_number_size = calculate_text_sizes(font_client_info, phone_number)
    office_hours_size = calculate_text_sizes(font_client_info, office_hours)

    client_name_x = (MAX_WIDTH - client_name_size[0]) // 2 + 20
    client_name_y = 280

    is_client_size_larger = client_name_size[0] > ((office_hours_size[0] + phone_number_size[0]) + 20)

    phone_number_x = calculate_phone_number_x(is_client_size_larger, client_name_x, phone_number_size)
    office_hours_x = calculate_office_hours_x(is_client_size_larger, client_name_x, client_name_size, office_hours_size)

    shared_y = (client_name_y + client_name_size[1]) + 25

    # Now you can draw the text using these positions
    # Draw the blkImage Text
    draw_blkImage.text(
        (client_name_x, client_name_y), client_name, font=font_client_name, fill=1
    )
#     draw_blkImage.text(
#         (phone_number_x, shared_y), phone_number, font=font_client_info, fill=1
#     )
#     draw_blkImage.text(
#         (office_hours_x, shared_y), office_hours, font=font_client_info, fill=1
#     )

    # Draw the redImage text
    draw_redImage.text(
        (415, 5), pod_number, font=font_extra_bold, fill=1
    )
    draw_redImage.text(
        (545, 125), "Moviola Post", font=font_semi_bold, fill=1
    )
    draw_redImage.text(
        (545, 145), "1115 N. Hollywood Way", font=font_semi_bold, fill=1
    )
    draw_redImage.text(
        (545, 165), "Burbank, CA 91605", font=font_semi_bold, fill=1
    )

    logging.info("Ready to display all from buffers...")
    epd.display(epd.getbuffer(black_Image), epd.getbuffer(red_Image))
    time.sleep(1)

    logging.info("Setting display to sleep")
    epd.sleep()

    # Schedule a shutdown in 1 minute
    schedule_shutdown(1)  # minutes

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5b_V2.epdconfig.module_exit()
    exit()
