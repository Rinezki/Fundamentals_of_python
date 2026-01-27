# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by nnn according to given task

"""
Program that reads reservation details from a file
and prints them to the console:

Reservation number: 123
Booker: Anna Virtanen
Date: 31.10.2025
Start time: 10.00
Number of hours: 2
Hourly price: 19,95 €
Total price: 39,90 €
Paid: Yes
Location: Meeting Room A
Phone: 0401234567
Email: anna.virtanen@example.com
"""


def main():
    # Define the file name directly in the code
    reservations = "reservations.txt"

    # Open the file and read its contents
    with open(reservations, "r", encoding="utf-8") as f:
        reservation = f.read().strip()

    # Print the reservation to the console
    reservation = reservation.split('|')

    reservation_number = int(reservation[0])
    booker = reservation[1]

    from datetime import datetime

    day = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_day = day.strftime("%d.%m.%Y")

    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")

    hours = int(reservation[4])
    hourly_price = float(reservation[5])
    total_price = hours * hourly_price

    paid = reservation[6].strip().lower() == "true"

    location = reservation[7]
    phone = reservation[8]
    email = reservation[9]


    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {booker}")
    print(f"Date: {finnish_day}")
    print(f"Start time: {finnish_time}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {hourly_price:.2f} €".replace('.', ','))
    print(f"Total price: {total_price:.2f} €".replace('.', ','))
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

    # Try these
    #print(reservation.split('|'))
    #reservationId = reservation.split('|')[0]
    #print(reservationId)
    #print(type(reservationId))
    """
    The above should have printed the number 123,
    which is by default text.

    You can also try changing [0] to [1]
    and test what changes.
    """

if __name__ == "__main__":
    main()