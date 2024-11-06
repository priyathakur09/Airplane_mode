import frappe

def execute():
    flight_passenger = frappe.db.get_all("Flight Passenger", pluck="name")
    for p in flight_passenger:
        flight_passenger = frappe.get_doc("Flight Passenger", p)
        flight_passenger.setname()
        flight_passenger.save()

    frappe.db.commit()