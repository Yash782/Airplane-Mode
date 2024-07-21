# Copyright (c) 2024, Yash Wadgaonkar and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import random
from frappe import *

class AirplaneTicket(Document):
    def validate(self):
        # Calculate total amount
        total = 0
        seen_items = set()
        unique_add_ons = []

        for add_on in self.add_ons:
         
            if add_on.item not in seen_items:
                unique_add_ons.append(add_on)
                seen_items.add(add_on.item)
           
            total += add_on.amount

        self.add_ons = unique_add_ons
        self.total_amount = total + self.flight_price
               
    def on_submit(self):
        if self.status != "Boarded":
            frappe.msgprint(
                msg = "Can't Submit Passenger is not boarded",
                title = "Error",
                raise_exception= frappe.ValidationError
            )
    
    def validate(self):
        self.check_seat_availability()

    def check_seat_availability(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)

        airplane = frappe.get_doc("Airplane", flight.airplane)

        capacity = airplane.capacity

        tickets_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

        if tickets_count >= capacity:
            frappe.throw(f"Cannot create ticket. The airplane '{airplane.name}' for flight '{flight.name}' has only {capacity} seats and all are booked.")