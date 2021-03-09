frappe.ui.form.on('Purchase Receipt', {
    refresh(frm) {
        if (frm.doc.docstatus === 0) {
            frm.page.add_menu_item(__("Submit in Background"), function() {
                frappe.call('express.events.background_update.submit', {
                doctype: frm.doc.doctype,
                docname: frm.doc.name
                })
                .then(r=> {
                    frappe.show_alert("Document is submitting in background");
                })
            });
        } else if (frm.doc.docstatus === 1) {
            frm.page.add_menu_item(__("Cancel in Background"), function() {
                frappe.call('express.events.background_update.cancel', {
                    doctype: frm.doc.doctype,
                    docname: frm.doc.name
                    })
                .then(r=> {
                    frappe.show_alert("Document is canceling in background");
                })
            });
        }
        
    }
})