// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
 	refresh(frm) {
        frm.add_custom_button(__("Make Rent Invoice"), function() {  
            let contractId = frm.doc.name;
            let url = `http://yash.localhost:8000/app/rent-invoice/new-rent-invoice?contract_id=${contractId}`;
            window.open(url, '_blank');
        });
 	},
});