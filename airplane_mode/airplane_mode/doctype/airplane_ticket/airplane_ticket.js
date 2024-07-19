// Copyright (c) 2024, Yash Wadgaonkar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    add_ons: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    flight_price: function(frm) {
        frm.trigger('calculate_total_amount');
    },
    calculate_total_amount: function(frm) {
        let total_add_ons_amount = frm.doc.add_ons.reduce((sum, add_on) => sum + add_on.amount, 0);
        frm.set_value('total_amount', frm.doc.flight_price + total_add_ons_amount);
    },

    // Adding Custom Button:

   
});

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button('Assign Seat', () => {
            frappe.prompt([
                {
                    label: 'Seat',
                    fieldname: 'seat',
                    fieldtype: 'Data',
                    reqd: 1
                }
            ],
            function(values) {
                frm.set_value('seat', values.seat);
                frm.save();
            },
            'Assign Seat',
            'Assign');
        }, 'Actions'); 
    }
});