import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Ensure destination directory exists
output_dir = os.path.join("..", "Data", "Input")
os.makedirs(output_dir, exist_ok=True)

# Dataset covering clean, business rule errors, and structural anomalies
invoices = [
    # 1. Clean cases
    {"filename": "INV-2026-001.pdf", "id": "INV-2026-001", "vendor": "Apex Logistics Pvt Ltd", "date": "10-09-2026", "taxable": 10000.00, "tax": 1800.00, "total": 11800.00, "valid": True},
    {"filename": "INV-2026-002.pdf", "id": "INV-2026-002", "vendor": "Nexus IT Solutions", "date": "08-09-2026", "taxable": 25000.00, "tax": 4500.00, "total": 29500.00, "valid": True},
    {"filename": "INV-2026-003.pdf", "id": "INV-2026-003", "vendor": "CloudByte Infotech", "date": "07-09-2026", "taxable": 15000.00, "tax": 2700.00, "total": 17700.00, "valid": True},
    {"filename": "INV-2026-004.pdf", "id": "INV-2026-004", "vendor": "Apex Logistics Pvt Ltd", "date": "05-09-2026", "taxable": 8200.00, "tax": 1476.00, "total": 9676.00, "valid": True},
    {"filename": "INV-2026-005.pdf", "id": "INV-2026-005", "vendor": "Nexus IT Solutions", "date": "04-09-2026", "taxable": 40000.00, "tax": 7200.00, "total": 47200.00, "valid": True},
    {"filename": "INV-2026-006.pdf", "id": "INV-2026-006", "vendor": "Starlight Supplies", "date": "02-09-2026", "taxable": 12500.00, "tax": 2250.00, "total": 14750.00, "valid": True},

    # 2. Duplicate Invoice ID (matches 001 to trigger DB uniqueness failure)
    {"filename": "INV-2026-001-DUP.pdf", "id": "INV-2026-001", "vendor": "Apex Logistics Pvt Ltd", "date": "10-09-2026", "taxable": 10000.00, "tax": 1800.00, "total": 11800.00, "valid": True},

    # 3. Calculation Mismatch (Taxable 20,000 + Tax 3,600 != Total 25,000)
    {"filename": "INV-2026-007-MATH-ERR.pdf", "id": "INV-2026-007", "vendor": "CloudByte Infotech", "date": "01-09-2026", "taxable": 20000.00, "tax": 3600.00, "total": 25000.00, "valid": True},

    # 4. Unknown Vendor (Vendor not in ERP approved list)
    {"filename": "INV-2026-008-UNKNOWN-VENDOR.pdf", "id": "INV-2026-008", "vendor": "Random Retailer X", "date": "01-09-2026", "taxable": 5000.00, "tax": 900.00, "total": 5900.00, "valid": True},

    # 5. Missing Field (No Invoice ID)
    {"filename": "INV-2026-009-MISSING-ID.pdf", "id": "", "vendor": "Nexus IT Solutions", "date": "31-08-2026", "taxable": 14000.00, "tax": 2520.00, "total": 16520.00, "valid": False}
]

def build_pdf(data):
    file_path = os.path.join(output_dir, data["filename"])
    c = canvas.Canvas(file_path, pagesize=letter)
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "TAX INVOICE")
    
    c.setFont("Helvetica", 10)
    c.drawString(50, 735, "Vendor: " + data["vendor"])
    
    # Metadata
    c.setFont("Helvetica-Bold", 10)
    if data["id"]:
        c.drawString(400, 750, f"Invoice No: {data['id']}")
    c.drawString(400, 735, f"Date: {data['date']}")
    
    # Divider
    c.line(50, 720, 550, 720)
    
    # Line items summary
    c.setFont("Helvetica", 11)
    c.drawString(50, 680, "Taxable Amount:")
    c.drawString(200, 680, f"INR {data['taxable']:.2f}")
    
    c.drawString(50, 655, "GST (18%):")
    c.drawString(200, 655, f"INR {data['tax']:.2f}")
    
    c.line(50, 640, 550, 640)
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 620, "Total Amount:")
    c.drawString(200, 620, f"INR {data['total']:.2f}")
    
    c.save()

for inv in invoices:
    build_pdf(inv)

print(f"Generated {len(invoices)} invoices inside Data/Input/")