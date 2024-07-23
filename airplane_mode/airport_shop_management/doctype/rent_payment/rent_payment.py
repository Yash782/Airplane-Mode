# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RentPayment(Document):
    def before_submit(self):
        if self.invoice_number:
            try:
                frappe.db.set_value('Rent Invoice', self.invoice_number, 'status', 'Paid')
            except Exception as e:
                frappe.throw(_("Failed to update Rent Invoice status: {0}").format(str(e)))
        else:
            frappe.logger().info("No linked Rent Invoice found for Rent Payment.")