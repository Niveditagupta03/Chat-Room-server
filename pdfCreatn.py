from reportlab.pdfgen import canvas
from datetime import datetime

class InvoiceGenerator:
    def __init__(self, invoice_data):
        self.invoice_data = invoice_data

    def generate_invoice(self, output_file):
        c = canvas.Canvas(output_file)

        # Set font styles
        c.setFont("Helvetica-Bold", 16)

        # Add shop name
        c.drawString(10, 800, "VASAVI COMPUTERS (LAPTOP STORE)")

        # Add message
        message = "INVOICE"
        message_font = "Helvetica"
        message_font_size = 12
        message_width = c.stringWidth(message, message_font, message_font_size)
        page_width = c._pagesize[0]
        message_x = page_width - message_width - 10
        message_y = 800
        c.setFont(message_font, message_font_size)
        c.drawString(message_x, message_y, message)

        # Add date on the right top side
        date = datetime.now().strftime("%Y-%m-%d")
        date_font = "Helvetica"
        date_font_size = 10
        date_width = c.stringWidth(date, date_font, date_font_size)
        date_x = page_width - date_width - 5
        date_y = 780
        c.setFont(date_font, date_font_size)
        c.drawString(date_x, date_y, "Date:" + date)

        # Add client information
        client_font = "Helvetica"
        client_font_size = 12
        client_x = 10
        client_y = 750
        c.setFont(client_font, client_font_size)
        c.drawString(client_x, client_y, "Client Information")
        c.drawString(client_x, client_y - 20, f"Name: {self.invoice_data['client_name']}")
        c.drawString(client_x, client_y - 40, f"Address: {self.invoice_data['client_address']}")

        # Add itemized billing
        billing_x = 10
        billing_y = 680
        c.setFont("Helvetica-Bold", 12)
        c.drawString(billing_x, billing_y, "Itemized Billing")
        item_font_size = 10
        item_y = billing_y - 20
        for item in self.invoice_data['items']:
            c.setFont("Helvetica", item_font_size)
            c.drawString(billing_x, item_y, f"Item: {item['name']}")
            c.drawString(billing_x + 100, item_y, f"Quantity: {item['quantity']}")
            c.drawString(billing_x + 200, item_y, f"Price: {item['price']}")
            item_y -= 20

        # Add total and taxes
        total_y = item_y - 20
        c.drawString(billing_x, total_y, f"Total: {self.invoice_data['total']}")
        c.drawString(billing_x, total_y - 20, f"Taxes: {self.invoice_data['taxes']}")

        c.showPage()
        c.save()

# Example usage
invoice_data = {
    'client_name': 'XYZ',
    'client_address': 'CMR IT, BANGALORE',
    'items': [
        {'name': 'Apple laptop', 'quantity': 1, 'price': 203500},
        {'name': 'Dell laptop 2', 'quantity': 1, 'price': 200000}
    ],
    'total': 35,
    'taxes': 3.5
}

invoice_generator = InvoiceGenerator(invoice_data)
invoice_generator.generate_invoice('invoice.pdf')
