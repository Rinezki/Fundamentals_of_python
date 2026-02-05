from datetime import datetime, date
from collections import defaultdict
from typing import List, Dict, Tuple
import csv

def read_data(filename: str) -> list[dict]:

    rows: list[dict] = []

    with open (filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    
    return rows

def finnish_weekday(d: date) -> str:

    weekdays: List[str] = [
        "Maanantai",
        "Tiistai",
        "Keskiviikko",
        "Torstai",
        "Perjantai",
        "Lauantai",
        "Sunnuntai",
    ]
    return weekdays[d.weekday()]

def format_kwh(value: float) -> str:
   
    return f"{value:.2f}".replace(".", ",")

def calculate_daily_totals(rows: List[dict]) -> Dict[date, Dict[str, List[float]]]:
     
    daily: Dict[date, Dict[str, List[float]]] = defaultdict(
        lambda: {"cons": [0.0, 0.0, 0.0], "prod": [0.0, 0.0, 0.0]}
    )

    for row in rows:
        dt = datetime.fromisoformat(row["Time"])
        d = dt.date()
        daily[d]["cons"][0] += float(row["Consumption phase 1 Wh"]) / 1000
        daily[d]["cons"][1] += float(row["Consumption phase 2 Wh"]) / 1000
        daily[d]["cons"][2] += float(row["Consumption phase 3 Wh"]) / 1000

        daily[d]["prod"][0] += float(row["Production phase 1 Wh"]) / 1000
        daily[d]["prod"][1] += float(row["Production phase 2 Wh"]) / 1000
        daily[d]["prod"][2] += float(row["Production phase 3 Wh"]) / 1000

    return daily

def print_report(daily_data: Dict[date, Dict[str, List[float]]]) -> None:
   
    if not daily_data:
        print("No data available.")
        return

    sorted_days: List[date] = sorted(daily_data.keys())
    week_number: int = sorted_days[0].isocalendar().week

    print(f"\nWeek {week_number} electricity consumption and production (kWh, by phase)\n")
    print("Day          Date        Consumption [kWh]               Production [kWh]")
    print("            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3")
    print("---------------------------------------------------------------------------")

    for d in sorted_days:
        weekday_name = finnish_weekday(d)
        date_str = d.strftime("%d.%m.%Y")
        cons = daily_data[d]["cons"]
        prod = daily_data[d]["prod"]

        print(
            f"{weekday_name:<12} {date_str:<10}   "
            f"{format_kwh(cons[0]):>6}  {format_kwh(cons[1]):>6}  {format_kwh(cons[2]):>6}        "
            f"{format_kwh(prod[0]):>6}  {format_kwh(prod[1]):>6}  {format_kwh(prod[2]):>6}"
        )

def main() -> None:
    
    filename = "week42.csv"

    rows = read_data(filename)
    daily_totals= calculate_daily_totals(rows)
    print_report(daily_totals)

if __name__ == "__main__":
    main()