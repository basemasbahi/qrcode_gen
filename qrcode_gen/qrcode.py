import frappe
import pyqrcode




@frappe.whitelist()
def gen_qrcode(text):
    txt = text.encode('utf-8', 'replace').decode('latin-1')
    data = pyqrcode.create(txt)

    return f'data:image/png;base64,{data.png_as_base64_str(scale=5)}'
