from datetime import datetime, date, time

def read_reservations(filename):
    reservations = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            row = line.split("|")
            converted = convert_reservation_data(row)
            reservations.append(converted)

    return reservations


def convert_reservation_data(row):
    reservation_id = int(row[0])
    name = row[1]
    email = row[2]
    phone = row[3]

    reservation_date = datetime.strptime(row[4], "%Y-%m-%d").date()
    reservation_time = datetime.strptime(row[5], "%H:%M").time()


    duration_hours = int(row[6])
    price = float(row[7])

    confirmed = (row[8] == "True")

    reserved_resource = row[9]
    created_at = datetime.strptime(row[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id,
        name,
        email,
        phone,
        reservation_date,
        reservation_time,
        duration_hours,
        price,
        confirmed,
        reserved_resource,
        created_at
    ]

def format_date(d):
    return d.strftime("%d.%m.%Y")


def format_time(t):
    return t.strftime("%H.%M")

def confirmed_reservations(reservations):
    print("1) Confirmed Reservations")
    for r in reservations:
        if r[8]:
            print(f"- {r[1]}, {r[9]}, {format_date(r[4])} at {format_time(r[5])}")
    print()

def long_reservations(reservations):
    print("2) Long Reservations (≥ 3 h)")
    for r in reservations:
        if r[6] >= 3:
            print(
                f"- {r[1]}, {format_date(r[4])} at {format_time(r[5])}, "
                f"duration {r[6]} h, {r[9]}"
            )
    print()

def confirmation_statuses(reservations):
    print("3) Reservation Confirmation Status")
    for r in reservations:
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{r[1]} → {status}")
    print()

def confirmation_summary(reservations):
    confirmed_count = 0
    not_confirmed_count = 0

    for r in reservations:
        if r[8]:
            confirmed_count += 1
        else:
            not_confirmed_count += 1

    print("4) Confirmation Summary")
    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")
    print()

def total_revenue(reservations):
    total = 0.0
    for r in reservations:
        if r[8]:
            total += r[7]

    amount_str = f"{total:.2f}".replace(".", ",")

    print("5) Total Revenue from Confirmed Reservations")
    print(f"Total revenue from confirmed reservations: {amount_str} €")

def main():
    reservations = read_reservations("reservations.txt")

    confirmed_reservations(reservations)
    long_reservations(reservations)
    confirmation_statuses(reservations)
    confirmation_summary(reservations)
    total_revenue(reservations)


if __name__ == "__main__":
    main()
