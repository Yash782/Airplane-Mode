# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import *

class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.db_set('status', 'Completed')
        frappe.db.commit()
