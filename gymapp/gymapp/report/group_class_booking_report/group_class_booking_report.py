# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "class_name", "label": "Class Name", "fieldtype": "Data", "width": 150},
        {"fieldname": "total_bookings", "label": "Total Bookings", "fieldtype": "Int", "width": 150}
    ]
    
    data = frappe.db.sql("""
        SELECT class_name, COUNT(name) AS total_bookings
        FROM `tabClass Booking`
        GROUP BY class_name
        ORDER BY total_bookings DESC
    """, as_dict=True)

    chart_data = [{
        'value': item['total_bookings'],
        'label': item['class_name']
    } for item in data]

    chart = {
        "type": "donut",
        "data": {
            "labels": [item['class_name'] for item in data],
            "datasets": [{
                "name": "Bookings",
                "values": [item['total_bookings'] for item in data]
            }]
        },
        "height": 700
    }

    return columns, data, None, chart
