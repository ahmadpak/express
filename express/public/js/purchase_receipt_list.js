frappe.listview_settings['Purchase Receipt'] = {
    onload: function (listview) {
        listview.page.add_action_item('Submit In Background', function() {
            const selections = listview.get_checked_items();
            frappe.call({
                method: "express.events.background_update.submit_multiple",
                args:{
                    "doctype": 'Purchase Receipt',
                    "docs": selections
                },
                callback: function (r) {
                    if (r.message) {
                        const flag = r.message.pop()
                        for (let row of r.message) {
                            frappe.show_alert(`Skipping ${row}`)
                        }
                        if (flag) {
                            frappe.show_alert('Documents are Submitting in the Background')
                        }
                    }
                }
            });
        });
        listview.page.add_action_item('Cancel In Background', function() {
            const selections = listview.get_checked_items();
            frappe.call({
                method: "express.events.background_update.cancel_multiple",
                args:{
                    "doctype": 'Purchase Receipt',
                    "docs": selections
                },
                callback: function (r) {
                    if (r.message) {
                        const flag = r.message.pop()
                        for (let row of r.message) {
                            frappe.show_alert(`Skipping ${row}`)
                        }
                        if (flag) {
                            frappe.show_alert('Documents are Cancelling in the Background')
                        }
                    }
                }
            });
        });
    }
};