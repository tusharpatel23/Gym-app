// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt


frappe.query_reports["Fitness Journey Report"] = {
    filters: [
        {
            fieldname: "member",
            label: __("Member"),
            fieldtype: "Link",
            options: "Gym Member",
            reqd: 1 // ye 12 line mandatory ke liye hota hai.
        }
    ],
};