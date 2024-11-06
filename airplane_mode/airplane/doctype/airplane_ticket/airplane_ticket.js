// Copyright (c) 2024, airplane and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button('Assign Seat', function(){
            let dlg = new frappe.ui.Dialog({
                title : 'Select Seat',
                fields :[{
                    label : 'Seat Number',
                    fieldname : 'seat_number',
                    fieldtype : 'Data'
                }], 
                primary_action_label : 'Submit',
                primary_action(values){
                    frm.set_value('seat', values.seat_number);
                    dlg.hide()
                }  
            })
            dlg.show()
        })
	},
});


frappe.ui.form.on("Airplane Ticket Add-on Item", {
    refresh(frm){
        
    }
})