// Copyright (c) 2024, tushar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Fitness Metrics', {
    member: function (frm) {
        if (frm.doc.member) {

            frm.set_value('date', frappe.datetime.get_today());
            frm.set_value('weight_kg', (50 + Math.random() * 50).toFixed(2));
            frm.set_value('calories_intake_kcal', Math.floor(1500 + Math.random() * 1000));
            frm.set_value('workout_duration_mins', Math.floor(30 + Math.random() * 90));
            frm.set_value('custom_notes', 'Auto-filled data for testing purposes.');

            frm.msgprint(`Your Metrics for today ${date} updated`)

            a = Math.floor(1500 + Math.random() * 1000)
            console.log("check calories", a);
        }
    }
});
