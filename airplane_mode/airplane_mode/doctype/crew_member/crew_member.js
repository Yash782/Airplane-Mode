// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt
frappe.ui.form.on("Crew Member", {
    last_name(frm, cdt, cdn) {
        set_full_name(frm, cdt, cdn);
    },
    first_name(frm, cdt, cdn) {
        set_full_name(frm, cdt, cdn);
    }
});

function set_full_name(frm, cdt, cdn) {
    let row = locals[cdt][cdn];

    let firstName = row.first_name || '';
    let lastName = row.last_name || '';

    let fullName = `${firstName} ${lastName}`;

    frappe.model.set_value(cdt, cdn, 'full_name', fullName);
}
