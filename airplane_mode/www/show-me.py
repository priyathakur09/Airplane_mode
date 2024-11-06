import frappe

def get_context(context):
    color = frappe.form_dict.get('color','black')

    context.background_color = color
    context.rectangle_width = '700px'
    context.rectangle_height = '500px'