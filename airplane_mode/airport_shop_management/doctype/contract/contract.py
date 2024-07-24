# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Contract(Document):

	def before_submit(self):
		
		shop = frappe.get_doc("Shop", self.shop)
		shopStatus = shop.status
		newTenant = self.tenant

		if shopStatus == "Available":
			shop.status = "Occupied"
			shop.tenant = newTenant
			shop.save()

	def before_save(self):
		shop = frappe.get_doc("Shop", self.shop)
		shopStatus = shop.status
		if shopStatus == "Occupied":
			frappe.throw("Shop is already occupied")

	def on_cancel(self):

		shop = frappe.get_doc("Shop", self.shop)
		shopStatus = shop.status

		if shopStatus == "Occupied":
			shop.status = "Available" 
			shop.tenant = None
			shop.save()
			
