import frappe
from frappe.utils import today, date_diff

@frappe.whitelist()
def get_member_data(member):
    member_doc = frappe.get_doc("Gym Member", {"email": member})

    # default value ko Initialize kr rha hai aur ye zaruri hai data show krne k liye.
    plan = None 
    tra = None

    if member_doc.active_plan:
        plan = frappe.get_doc("Gym Membership", member_doc.active_plan)
        remaining_days = date_diff(plan.end_date, today())

    if member_doc.assign_trainer:
        tra = frappe.get_doc("Trainer Subscription", member_doc.assign_trainer)
        sub_remaining_day = date_diff(tra.end_date, today())

    return {
        "member_name": member_doc.full_name,
        "img": member_doc.profile_image,

        "start_date": plan.start_date,
        "remaining_days": remaining_days or 0,
        "active_plan": plan.membership_plan if plan else "None",
        "gym_amount" : plan.amount,

        "trainer_name": tra.trainer or "None",
        "sub_start" : tra.start_date,
        # "sub_end": tra.end_date,
        # "total_days": tra.total_days,
        "sub_remaining_day": sub_remaining_day,
        "total_hours": tra.total_hours,
        "total_rate": tra.total_rate,
        # "sub_amount" : trainer_amount_paid,
        # "trainer_contact": member_doc.allocated_trainer_contact or "None"
    }