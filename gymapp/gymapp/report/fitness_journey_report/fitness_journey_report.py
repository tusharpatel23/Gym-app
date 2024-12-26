# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt


import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "date", "label": "Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "weight_kg", "label": "Weight (kg)", "fieldtype": "Float", "width": 120},
        {"fieldname": "calories_intake_kcal", "label": "Calories Intake (kcal)", "fieldtype": "Int", "width": 150},
        {"fieldname": "workout_duration_mins", "label": "Workout Duration (mins)", "fieldtype": "Int", "width": 150},
        {"fieldname": "custom_notes", "label": "Notes", "fieldtype": "Data", "width": 200},
    ]

    data = []

    if filters and filters.get("member"):
        data = frappe.db.get_all(
            "Gym Fitness Metrics",
            filters={"member": filters.get("member")},
            fields=["date", "weight_kg", "calories_intake_kcal", "workout_duration_mins", "custom_notes"],
            order_by="date asc"
        )

    return columns, data

# def execute(filters=None):
#     columns = [
#         {"fieldname": "trainer_name", "label": "Data", "fieldtype": "Data", "width": 150},
#     ]

#     data = []

#     if filters and filters.get("Trainer"):
#         data = frappe.db.get_all(
#             "Gym Trainer",
#             filters={"trainer_name": filters.get("trainer_name")},
#             fields=["trainer_name",],
#             # order_by="date asc"
#         )

#     return columns, data

