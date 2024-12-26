# import frappe
# from frappe.utils import today, date_diff

# def check():
#     member_doc = frappe.get_doc("Gym Member", {"full_name": "Vicky"})
#     print(member_doc)
#     print(member_doc.active_plan)

#     # default value ko Initialize kr rha hai aur ye zaruri hai data show krne k liye.
#     plan = None 
#     tra = None

#     if member_doc.active_plan:
#         plan = frappe.get_doc("Gym Membership", member_doc.active_plan)
#         remaining_days = date_diff(plan.end_date, today())
#         print("member",plan.amount)

#     if member_doc.assign_trainer:
#         print(member_doc.assign_trainer)
#         tra = frappe.get_doc("Trainer Subscription", member_doc.assign_trainer)
#         sub_remaining_day = date_diff(tra.end_date, today())
#         print("trainer", tra.trainer)


import frappe
from datetime import datetime, timedelta

def check(): # send_weekly_class_summary():

    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=7)
    # print(end_date, "e-s", start_date)
    # Fetch members who attended classes last week
    members = frappe.get_all(
        "Class Booking",
        filters={"booking_date": ["between", [start_date, end_date]]},
        fields=["member", "class_name", "booking_date"]
    )

    # print(members)

    # Organize data by member
    member_summary = {}
    for entry in members:
        member_summary.setdefault(entry.member, []).append(entry)


#     # Send email to each member
    for member in member_summary:
        email = frappe.db.get_value("Gym Member", member, "email")
        if email:
            print(send_email_to_member(member, email, member_summary[member]))

def send_email_to_member(member, email, classes):
    # Prepare email content
    class_details = "\n".join(
        [f"{entry['class_name']} on {entry['booking_date']}" for entry in classes]
    )
    subject = "Your Weekly Class Summary"
    message = f"""
        Dear {member},
        Here is your weekly summary of the group classes you attended at our gym:
        {class_details}
        Keep up the great work!
        Regards,  
        Your Gym Team
    """
    # Send email
    frappe.sendmail(
        recipients=email,
        subject=subject,
        message=message
    )


