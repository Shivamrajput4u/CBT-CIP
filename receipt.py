from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Function to generate a payment receipt PDF with multiple items
def generate_receipt(customer_name, transaction_id, items, payment_method):
    # Create a new PDF with reportlab
    pdf_file = f"receipt_{transaction_id}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Define PDF Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Payment Receipt")

    # Add Customer Name
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Customer Name: {customer_name}")

    # Add Transaction ID
    c.drawString(100, 700, f"Transaction ID: {transaction_id}")

    # Add Items and their prices
    c.drawString(100, 680, "Items:")
    y_position = 660
    total_amount = 0

    for item, price in items.items():
        c.drawString(100, y_position, f"{item}: ${price:.2f}")
        total_amount += price
        y_position -= 20

    # Add Total Amount
    c.drawString(100, y_position, f"Total Amount: ${total_amount:.2f}")
    y_position -= 20

    # Add Payment Method
    c.drawString(100, y_position, f"Payment Method: {payment_method}")
    y_position -= 20

    # Add Date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(100, y_position, f"Date: {current_date}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, y_position - 40, "Thank you for your payment!")

    # Save the PDF
    c.save()

    print(f"Receipt generated: {pdf_file}")

# Taking input from the user via terminal
customer_name = input("Enter Customer Name: ")
transaction_id = input("Enter Transaction ID: ")
payment_method = input("Enter Payment Method: ")

# Collecting multiple items
items = {}
while True:
    item_name = input("Enter item name (or type 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_price = float(input(f"Enter price for {item_name}: "))
    items[item_name] = item_price

# Generate the receipt using the provided inputs
generate_receipt(customer_name, transaction_id, items, payment_method)
