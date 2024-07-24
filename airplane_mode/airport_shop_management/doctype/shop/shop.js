// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
    refresh: function(frm) {
        frm.add_custom_button(__("Make Contract"), function() {
            
            let shop_name = frm.doc.name;
            const siteUrl = window.location.origin;
            let url = `${siteUrl}/app/contract/new-contract?shop=${shop_name}`;
            window.open(url, '_blank');
        });
    },
    status: function(frm) {
        if (frm.doc.status == "Occupied"){
            frm.set_value('is_published', 0)
        }else{
            frm.set_value('is_published', 1)
        }
    },
});