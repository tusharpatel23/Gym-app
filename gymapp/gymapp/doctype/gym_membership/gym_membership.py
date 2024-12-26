# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembership(Document):
	def validate(self):
		today = frappe.utils.today()

		m_amount = frappe.db.get_single_value("Gym Setting", "monthly_amount")
		if self.membership_plan == "Monthly":
			self.amount = m_amount
		elif self.membership_plan == "Quarterly":
			self.amount = m_amount*3
		else:
			self.amount = m_amount*12
		
		if today == self.end_date:
			self.status = "Expired"
		else:
			self.status = "Active"
