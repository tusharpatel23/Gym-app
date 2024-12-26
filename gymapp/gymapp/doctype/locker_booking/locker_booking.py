# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LockerBooking(Document):

	def before_insert(self):
		endDate = frappe.db.get_all("Gym Membership", fields = ["member", "end_date"]) 
		for d in endDate:
			if self.member == d.member:
				self.end_date = d.end_date

	def validate(self):
		today = frappe.utils.today()

		locker = frappe.get_all("Locker Booking", filters={"locker_number": self.locker_number, "status": "Booked"})
		if locker and self.status == "Booked":
			frappe.throw("This locker is already booked.")

		c = frappe.db.get_single_value("Gym Setting", "locker_count")
		count = frappe.db.count("Locker Booking", {"status" : "Booked"})

		if count >= c:
			frappe.throw(
				msg = "All locker booked"
			)
