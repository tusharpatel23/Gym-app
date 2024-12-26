// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt

// frappe.query_reports["Group Class Booking Report"] = {
// 	filters: [
//         {
//             fieldname: "class_name",
//             label: __("Class Name"),
//             fieldtype: "Data",
//             reqd: 0
//         }
//     ],
//     onload: function(report) {
//         report.page.add_sidebar_item(__('Instructions'), 'fa fa-info', function() {
//             frappe.msgprint('This report shows the most popular group classes based on total bookings. Use the filter to select a specific class or leave it empty for all.');
//         });
//     },
//     formatter: function(value, row, column, data, default_formatter) {
//         // Add logic if you want to format the values (optional)
//         return default_formatter(value, row, column, data);
//     }
// };
