#!/usr/bin/env python3
"""
Clean venue lists by removing closed venues and duplicates.
"""

import csv
import json
from collections import defaultdict

# Closed venue IDs from Yelp check
CLOSED_IDS = {
    "D1-066", "D1-079", "D2-016", "D2-037", "D2-040", "D2-047", "D2-063",
    "D3-066", "D4-025", "D4-026", "U1-015", "U1-070", "U1-081", "U1-092",
    "U2-017", "U2-059", "U3-023", "U3-027", "U3-035", "U4-034"
}

def load_csv(path):
    """Load CSV and return list of dicts."""
    venues = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            venues.append(row)
    return venues

def save_csv(venues, path, fieldnames):
    """Save list of dicts to CSV."""
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(venues)

def normalize_key(name, address):
    """Create a normalized key for duplicate detection."""
    return (name.lower().strip(), address.lower().strip())

def main():
    print("=" * 60)
    print("VENUE LIST CLEANUP")
    print("=" * 60)

    # Load both CSV files
    dupont = load_csv("dupont-leads.csv")
    thu14 = load_csv("14thu-leads.csv")

    print(f"\nLoaded:")
    print(f"  dupont-leads.csv: {len(dupont)} venues")
    print(f"  14thu-leads.csv:  {len(thu14)} venues")
    print(f"  Total: {len(dupont) + len(thu14)} venues")

    # Get fieldnames from original
    fieldnames = list(dupont[0].keys())

    # Step 1: Remove closed venues
    print("\n" + "-" * 60)
    print("STEP 1: Removing closed venues")
    print("-" * 60)

    dupont_closed = [v for v in dupont if v["ID"] in CLOSED_IDS]
    thu14_closed = [v for v in thu14 if v["ID"] in CLOSED_IDS]

    dupont_filtered = [v for v in dupont if v["ID"] not in CLOSED_IDS]
    thu14_filtered = [v for v in thu14 if v["ID"] not in CLOSED_IDS]

    print(f"\nRemoved from dupont-leads.csv ({len(dupont_closed)}):")
    for v in dupont_closed:
        print(f"  - {v['ID']}: {v['Name']}")

    print(f"\nRemoved from 14thu-leads.csv ({len(thu14_closed)}):")
    for v in thu14_closed:
        print(f"  - {v['ID']}: {v['Name']}")

    # Step 2: Find duplicates between files
    print("\n" + "-" * 60)
    print("STEP 2: Finding duplicates between files")
    print("-" * 60)

    # Build lookup of venues by name+address
    dupont_keys = {}
    for v in dupont_filtered:
        key = normalize_key(v["Name"], v["Address"])
        dupont_keys[key] = v

    # Find duplicates in 14th St list that exist in Dupont
    duplicates = []
    thu14_deduped = []

    for v in thu14_filtered:
        key = normalize_key(v["Name"], v["Address"])
        if key in dupont_keys:
            duplicates.append({
                "name": v["Name"],
                "address": v["Address"],
                "dupont_id": dupont_keys[key]["ID"],
                "thu14_id": v["ID"]
            })
        else:
            thu14_deduped.append(v)

    if duplicates:
        print(f"\nFound {len(duplicates)} duplicate(s) (same name + address in both files):")
        for d in duplicates:
            print(f"  - {d['name']} @ {d['address']}")
            print(f"    Dupont ID: {d['dupont_id']}, 14th St ID: {d['thu14_id']} (removing 14th St entry)")
    else:
        print("\nNo duplicates found between files.")

    # Step 3: Save cleaned files
    print("\n" + "-" * 60)
    print("STEP 3: Saving cleaned files")
    print("-" * 60)

    save_csv(dupont_filtered, "dupont-leads.csv", fieldnames)
    save_csv(thu14_deduped, "14thu-leads.csv", fieldnames)

    print(f"\nSaved:")
    print(f"  dupont-leads.csv: {len(dupont_filtered)} venues (was {len(dupont)})")
    print(f"  14thu-leads.csv:  {len(thu14_deduped)} venues (was {len(thu14)})")

    # Summary
    total_removed = (len(dupont) - len(dupont_filtered)) + (len(thu14) - len(thu14_deduped))

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nOriginal total: {len(dupont) + len(thu14)} venues")
    print(f"Closed removed: {len(dupont_closed) + len(thu14_closed)}")
    print(f"Duplicates removed: {len(duplicates)}")
    print(f"New total: {len(dupont_filtered) + len(thu14_deduped)} venues")
    print(f"\nTotal removed: {total_removed} venues")

    # Save removal log
    removal_log = {
        "closed_venues_removed": [
            {"id": v["ID"], "name": v["Name"], "file": "dupont-leads.csv"}
            for v in dupont_closed
        ] + [
            {"id": v["ID"], "name": v["Name"], "file": "14thu-leads.csv"}
            for v in thu14_closed
        ],
        "duplicates_removed": duplicates,
        "summary": {
            "original_dupont": len(dupont),
            "original_14thu": len(thu14),
            "original_total": len(dupont) + len(thu14),
            "new_dupont": len(dupont_filtered),
            "new_14thu": len(thu14_deduped),
            "new_total": len(dupont_filtered) + len(thu14_deduped),
            "closed_removed": len(dupont_closed) + len(thu14_closed),
            "duplicates_removed": len(duplicates)
        }
    }

    with open("venue_cleanup_log.json", "w") as f:
        json.dump(removal_log, f, indent=2)

    print(f"\nCleanup log saved to: venue_cleanup_log.json")

if __name__ == "__main__":
    main()
