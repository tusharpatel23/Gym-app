import frappe

def after_save_hook(doc, method):
    # frappe.msgprint(f"saving my bro")
    frappe.log_error("error")
