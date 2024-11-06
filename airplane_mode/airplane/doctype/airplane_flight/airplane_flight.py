# Copyright (c) 2024, airplane and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	
	def on_submit(self):
        # Directly set the status to "Completed" in the database
		self.db_set("status", "Completed")