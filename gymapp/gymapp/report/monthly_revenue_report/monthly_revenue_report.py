# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_first_day, get_last_day

def execute(filters=None):
    columns = [
        {"fieldname": "source", "label": "Revenue Source", "fieldtype": "Data", "width": 200},
        {"fieldname": "amount", "label": "Amount (Currency)", "fieldtype": "Currency", "width": 150},
    ]
    
    data = []
    total_revenue = 0

    year = filters.get("year")
    month = filters.get("month")
    
    if month:
        month_index = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ].index(month) + 1
        start_date = get_first_day(f"{year}-{month_index:02d}-01")
        end_date = get_last_day(start_date)
    else:
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
    
    membership_revenue = frappe.db.sql("""
        SELECT SUM(amount) as total
        FROM `tabGym Membership`
        WHERE start_date BETWEEN %s AND %s
    """, (start_date, end_date), as_dict=True)[0].get('total') or 0
    
    data.append({"source": "Memberships", "amount": membership_revenue})
    total_revenue += membership_revenue

   
    trainer_revenue = frappe.db.sql("""
        SELECT SUM(amount_paid) as total
        FROM `tabGym Trainer Subscription`
        WHERE start_date BETWEEN %s AND %s
    """, (start_date, end_date), as_dict=True)[0].get('total') or 0

    data.append({"source": "Trainer Subscriptions", "amount": trainer_revenue})
    total_revenue += trainer_revenue


    data.append({"source": "Total Revenue", "amount": total_revenue})

    chart = {
        "type": "bar",
        "data": {
            "labels": [row["source"] for row in data[:-1]],
            "datasets": [{
                "name": "Revenue",
                "values": [row["amount"] for row in data[:-1]]
            }]
        },
    }

    return columns, data, None, chart


    # locker_revenue = frappe.db.sql("""
    #     SELECT SUM(locker_price) as total
    #     FROM `tabGym Locker Booking`
    #     WHERE booking_start_date BETWEEN %s AND %s
    # """, (start_date, end_date), as_dict=True)[0].get('total') or 0

    # data.append({"source": "Locker Bookings", "amount": locker_revenue})
    # total_revenue += locker_revenue