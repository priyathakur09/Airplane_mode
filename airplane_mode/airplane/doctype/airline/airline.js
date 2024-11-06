// Copyright (c) 2024, airplane and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {
//         if (frm.doc.website) {
//             // Add a custom HTML link
//             frm.dashboard.add_section(`
//                 <a href="${frm.doc.website}" target="_blank" style="text-decoration: underline; color: black;">
//                     Visit Website
//                 </a>
//             `);
//         }
// 	},
// });






frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button(('Visit Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
        }
    },

    on_load: function(frm) {
        // Check if the website field is not empty
        if (frm.doc.website) {
            // Add a web link with the text "Visit Official Website"
            frm.add_web_link(('Visit Official Website'), frm.doc.website);
        }
    }
});






