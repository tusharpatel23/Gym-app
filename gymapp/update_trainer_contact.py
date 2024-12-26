import frappe

def execute():
    trainers = frappe.get_all(
        "Gym Trainer",
        filters={"contact_number": ["is", "not set"]},
        fields=["name"]
    )

    for trainer in trainers:
        frappe.db.set_value("Gym Trainer", trainer["name"], "contact_number", "0000000000")
        frappe.db.commit()

    frappe.log("Updated {0} trainers with default contact numbers.".format(len(trainers))) 


# 1. Fetch all trainers without contact number
# 2. Update each trainer with a placeholder contact number
# 3. bench --site gym.site migrate
