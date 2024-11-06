# Copyright (c) 2024, airplane and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class AirplaneTicket(Document):
# 	def validate(self):
# 		total = 0
# 		for item in self.add_ons:
# 			total += item.amount


# 		self.total_amount = total + self.flight_price


# 	def before_submit(self):
#         # Check if the status is not equal to "Boarded"
# 		if self.ticket_status != "Boarded":
#             # Throw an error with a custom message
# 			frappe.throw(f"Cannot submit Airplane Ticket unless status is 'Boarded'. Current status: {self.status}")
	
	
	



import frappe
from frappe.model.document import Document
import random

    




class AirplaneTicket(Document):

    def validate(self):
        # Ensure no duplicate add-ons and calculate the total price
        total = self.flight_price
        if self.add_ons:
            unique_add_ons = set()
            valid_add_ons = []

            # Validate each add-on and calculate total price
            for add_on in self.add_ons:
                if add_on.item in unique_add_ons:
                    frappe.msgprint(f"Duplicate add-on: {add_on.item}")
                else:
                    unique_add_ons.add(add_on.item)
                    valid_add_ons.append(add_on)
                    total += add_on.amount
            
            # Set valid add-ons without duplicates
            self.add_ons = valid_add_ons
        
        # Set the total amount after add-ons
        self.total_amount = total


        self.validate_seat()


    def before_submit(self):
        # Check if the status is not 'Boarded', throw an error
        if self.ticket_status != "Boarded":
            frappe.throw("This Airplane Ticket cannot be submitted because its status is not 'Boarded'.")

    def before_insert(self):
        # Assign a random available seat before inserting the document
        available_seats = self.get_available_seats()
        if not available_seats:
            frappe.throw("All seats are booked or not available.")
        self.seat = random.choice(available_seats)

    def get_available_seats(self):
        """Generate random seat and check if it's already booked."""
        available_seats = []
        letters = ['A', 'B', 'C', 'D', 'E']

        # Create a list of all possible seat combinations
        for number in range(1, 100):  # Seat numbers from 1 to 99
            for letter in letters:
                seat = f"{number}{letter}"
                # Check if the seat is already booked for the same flight
                if not frappe.db.exists('Airplane Ticket', {'flight': self.flight, 'seat': seat}):
                    available_seats.append(seat)

        return available_seats







    def validate_seat(self):
        # Get the airplane linked to this ticket
        airplane = frappe.get_doc('Airplane', self.airplane)
        
        # Get the total number of tickets already booked for this flight
        total_tickets = frappe.db.count('Airplane Ticket', {'Flight': self.flight})
        
        # Check if total tickets exceed airplane capacity
        if total_tickets >= airplane.capacity:
            frappe.throw(f"Cannot book ticket as the flight has only {airplane.capacity} seats, and all are booked.")
