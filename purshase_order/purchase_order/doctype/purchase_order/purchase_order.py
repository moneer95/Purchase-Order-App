# Copyright (c) 2023, monir and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from weasyprint import HTML
import requests


class PurchaseOrder(Document):
    pass


# Get the HTML content of the print format for a specific document
def get_print_format(name):
    return frappe.get_print(doctype="Purchase Order", name=name, print_format="format builder PO")


@frappe.whitelist()
def send_email(name, subject, message):
    html_content = get_print_format(name)
    pdf_content = HTML(string=html_content).write_pdf()

    attachment = [{
        "fname": f'{name}.pdf',
        "fcontent": pdf_content
    }]
    frappe.sendmail(recipients='mnyrskyk@gmail.com', subject=subject, message=message, attachments=attachment)

@frappe.whitelist()
def send_WhatsApp(name, subject, message):
    html_content = get_print_format(name)
    pdf_content = HTML(string=html_content).write_pdf()

    attachment = [{
        "fname": f'{name}.pdf',
        "fcontent": pdf_content
    }]

    # Construct the URL for the WhatsApp Share Screen
    url = f"https://api.whatsapp.com/send?text={message}&attachment={attachment}"

    # Redirect the user to the URL
    return requests.get(url)
