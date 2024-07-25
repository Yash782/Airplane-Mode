// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
    refresh: function(frm) {
        frm.add_custom_button(__("Make Contract"), function() {
            
            let contractId = frm.doc.name;
            const siteUrl = window.location.origin;
            let url = `${siteUrl}/app/rent-invoice/new-rent-invoice?contract_id=${contractId}`;
            window.open(url, '_blank');
        });
        frm.set_query("shop", function(){
            return {
                "filters": [
                    ["Shop", "status", "=", "Available"]
                ]
            };
        });
    },
});