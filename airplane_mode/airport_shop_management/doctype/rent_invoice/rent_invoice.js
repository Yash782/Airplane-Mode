// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Invoice", {
	refresh: function(frm) {
        frm.add_custom_button(__("Make Payment Entry"), function() {
            
            let invNumber = frm.doc.contract_id;
            const siteUrl = window.location.origin;
            let url = `${siteUrl}/app/rent-payment/new-rent-payment?invoice_number=${invNumber}`;
            window.open(url, '_blank');
        });
    },
});
