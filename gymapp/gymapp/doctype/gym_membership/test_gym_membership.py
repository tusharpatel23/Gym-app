# Copyright (c) 2024, tushar and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestGymMembership(UnitTestCase):
	"""
	Unit tests for GymMembership.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestGymMembership(IntegrationTestCase):
	"""
	Integration tests for GymMembership.
	Use this class for testing interactions between multiple components.
	"""

	pass


import frappe
from frappe.tests.utils import FrappeTestCase

class TestGymMembership(FrappeTestCase):
    def test_membership_creation(self):
        # Create a test member
        member = frappe.get_doc({
            "doctype": "Gym Member",
            "full_name": "Test Member",
            "email": "test_member@example.com"
        }).insert()

        # Create a test membership
        membership = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": member.name,
            "plan_name": "Basic Plan",
            "start_date": "2024-01-01",
            "end_date": "2024-03-31",
            "plan_price": 5000
        }).insert()

        # Assert the membership was created correctly
        self.assertEqual(membership.plan_name, "Basic Plan")
        self.assertEqual(membership.plan_price, 5000)



# tushar@asus:~/bench-gym$ bench run-tests --app gymapp  #command for testing
# Testing is disabled for the site!
# You can enable tests by entering following command:
# bench --site gym.site set-config allow_tests true
