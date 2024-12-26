# Copyright (c) 2024, tushar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainerSubscription(Document):
	pass
	# def before_insert(self):
	# 	endDate = frappe.db.get_all("Gym Membership", fields = ["member", "end_date"]) 
	# 	for d in endDate:
	# 		if self.member == d.member:
	# 			self.end_date = d.end_date # ye membership k end date ko put karega is doc ke end date mein
			
	# def validate(self):
	# 	dif = frappe.utils.date_diff(self.end_date, self.start_date)
	# 	self.total_rate = self.hourly_rate * self.total_hours * dif
		# endDate = frappe.db.get_all("Gym Membership", fields = ["end_date"]) 
		# for d in endDate:
		# 	if self.end_date > d.end_date:
		# 		frappe.throw(
		# 			msg = "End date is grater than Membership end date. Put valid date!"
		# 		)

# ye code men mujhe bss str ko date mein convert krna hai.