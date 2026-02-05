#!/usr/bin/env python3
"""
Migrate DC venues from CSV to Google Sheets format.

This script reads dc-venues.csv and outputs a new CSV file that can be
imported into Google Sheets with the Stage and LastUpdated columns added.

Usage:
    python3 migrate-to-sheets.py

Output:
    dc-venues-for-sheets.csv - Import this file into Google Sheets

After importing:
1. Go to File > Import > Upload the CSV
2. Select "Replace spreadsheet" or "Insert new sheet"
3. The data will include Stage (default: "Not Started") and LastUpdated columns
"""

import csv
from datetime import datetime

INPUT_FILE = 'dc-venues.csv'
OUTPUT_FILE = 'dc-venues-for-sheets.csv'

# New columns to add
NEW_COLUMNS = ['Stage', 'LastUpdated']
DEFAULT_STAGE = 'Not Started'

def migrate():
    venues = []

    # Read existing CSV
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        original_headers = reader.fieldnames

        for row in reader:
            # Add new columns with defaults
            row['Stage'] = DEFAULT_STAGE
            row['LastUpdated'] = ''
            venues.append(row)

    # Write new CSV with added columns
    new_headers = original_headers + NEW_COLUMNS

    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_headers)
        writer.writeheader()
        writer.writerows(venues)

    print(f"Migration complete!")
    print(f"  Input:  {INPUT_FILE} ({len(venues)} venues)")
    print(f"  Output: {OUTPUT_FILE}")
    print(f"")
    print(f"New columns added:")
    print(f"  - Stage (default: '{DEFAULT_STAGE}')")
    print(f"  - LastUpdated (empty)")
    print(f"")
    print(f"Next steps:")
    print(f"  1. Create a new Google Sheet named 'DC Venue Pipeline'")
    print(f"  2. Go to File > Import > Upload")
    print(f"  3. Select '{OUTPUT_FILE}'")
    print(f"  4. Choose 'Replace spreadsheet' or 'Replace current sheet'")
    print(f"  5. Open Extensions > Apps Script")
    print(f"  6. Paste the contents of google-apps-script.js")
    print(f"  7. Deploy as web app (see script comments for details)")

if __name__ == '__main__':
    migrate()
