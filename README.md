# Automated Invoice Processing & Verification

An RPA bot developed in UiPath Studio to batch-process multi-vendor PDF invoices, extract critical financial entities using RegEx, validate calculations and approved vendors, and route exceptions autonomously.

## Overview
Manual processing of vendor invoices often leads to data entry errors, delayed reconciliation, and improper payments. This automation ingests raw PDF invoices from an input directory, reconciles financial figures, checks vendor legitimacy against master records, and isolates faulty files for review.

## Key Features
- **Batch Processing:** Iterates through multi-vendor invoice PDFs in local directories.
- **RegEx Data Extraction:** Accurately parses Invoice Number, Vendor Name, Date, Taxable Amount, GST, and Total Amount.
- **Two-Tier Validation:**
  - *Math Verification:* Reconciles `Taxable Amount + GST = Total Amount` down to 2 decimal places.
  - *Master Vendor Lookup:* Validates extracted vendor names against an approved CSV vendor directory.
- **Automated Routing:** Moves verified documents to `Data/Processed/` and redirects math/vendor discrepancies to `Data/Exceptions/`.
- **Audit Logging:** Appends clean, reconciled records into a final summary CSV report.

## Tech Stack
- **RPA Platform:** UiPath Studio (.NET)
- **Data Extraction:** Regular Expressions (RegEx)
- **Data Handling:** CSV, DataTables, LINQ
- **Documents:** PDF Invoices

## Project Architecture
```text
Invoice_Processing_Automation/
├── Main.xaml
├── Workflows/
│   └── ExtractInvoiceData.xaml
├── Data/
│   ├── Input/                 # Raw PDF invoices
│   ├── Processed/             # Verified invoices
│   ├── Exceptions/            # Discrepancy & math error invoices
│   ├── Output/
│   │   └── reconciliation_report.csv
│   └── approved_vendors.csv   # Master vendor directory
├── Scripts/
│   └── generate_invoices.py   # Synthetic test data generation
└── project.json
