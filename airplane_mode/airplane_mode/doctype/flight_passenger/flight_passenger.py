# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

#import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
    
    def before_save(self):
        if self.first_name:
            if self.last_name is None:
                self.full_name = f"{self.first_name}"
            else:
                self.full_name = f"{self.first_name} {self.last_name}"
             