// Copyright (c) 2023, monir and contributors
// For license information, please see license.txt

frappe.ui.form.on("Purchase Order", {
	 refresh: function(frm) {
      frm.add_custom_button(__('Send Email'), function(){
      frappe.call({
        method: "purshase_order.purchase_order.doctype.purchase_order.purchase_order.send_email",
        args: {
          name:frm.doc.name,
          subject:frm.doc.subject,
          message:frm.doc.message
        },
        callback: function(r) {
          frappe.throw(r.toSetString)
        }
      });    });


      frm.add_custom_button(__('Send WhatsApp'), function(){
      frappe.call({
        method: "purshase_order.purchase_order.doctype.purchase_order.purchase_order.send_WhatsApp",
        args: {
          name:frm.doc.name,
          subject:frm.doc.subject,
          message:frm.doc.message
        },
        callback: function(r) {
          frappe.throw(r.toSetString)
        }
      });    });

  }
});
