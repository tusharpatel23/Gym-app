# Copyright (c) 2024, tushar and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestLockerBooking(UnitTestCase):
	"""
	Unit tests for LockerBooking.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestLockerBooking(IntegrationTestCase):
	"""
	Integration tests for LockerBooking.
	Use this class for testing interactions between multiple components.
	"""

	pass


import frappe
from frappe.tests.utils import FrappeTestCase

class TestLockerBooking(FrappeTestCase):
    def test_locker_allocation(self):
        # Set up gym locker settings
        frappe.get_doc({
            "doctype": "Gym Setting",
            "locker_count": 2
        }).insert(ignore_permissions=True)

        # Create 5 locker bookings
        # for i in range(1, 6):
        #     frappe.get_doc({
        #         "doctype": "Locker Booking",
        #         "locker_number": f"L-{i}",
        #         "member": f"Test Member {i}",
        #         "start_date": "2024-01-01",
        #         "end_date": "2024-12-31",
        #     }).insert()

        # # Try to book a 6th locker, expect an exception
        # with self.assertRaises(frappe.ValidationError):
        #     frappe.get_doc({
        #         "doctype": "Locker Booking",
        #         "locker_number": "L-6",
        #         "member": "Test Member 6",
        #         "start_date": "2024-01-01",
        #         "end_date": "2024-12-31",
        #     }).insert()
