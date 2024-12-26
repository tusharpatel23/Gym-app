// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt

frappe.query_reports["Monthly Revenue Report"] = {
    filters: [
        {
            fieldname: "month",
            label: __("Month"),
            fieldtype: "Select",
            options: [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
            reqd: 0
        },
        {
            fieldname: "year",
            label: __("Year"),
            fieldtype: "Int",
            default: new Date().getFullYear(),
            reqd: 1
        }
    ]
};
