# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Shop(WebsiteGenerator):
    def setRent(self):
        active = frappe.get_single('Rent Settings').enable_settings
        if active:
            defaultRent = frappe.get_single('Rent Settings').default_rent
            self.rent = defaultRent
    
    def before_validate(self):
        active = frappe.get_single('Rent Settings').enable_settings
        if active:
            defaultRent = frappe.get_single('Rent Settings').default_rent
            self.rent = defaultRent
            
        if self.status == "Available":
            self.is_published = 1
        else:
            self.is_published = 0