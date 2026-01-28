#!/usr/bin/env python3
"""
Check venues against Yelp API to find permanently closed businesses.
"""

import csv
import requests
import time
import json
from datetime import datetime

YELP_API_KEY = "uajJ0KaAnz1sq3EyDbsFiWYZAKJxuWHxukfR3GCD2EYL0csDcSh_gdbAw588RMchwn9oZUFyzun3Wq5XWDtoUSUn5-EjSb80W7n8V_x74pdwRKRkmJVO44iqQSx6aXYx"
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"

HEADERS = {
    "Authorization": f"Bearer {YELP_API_KEY}",
    "Accept": "application/json"
}

def load_venues(csv_path):
    """Load venues from a CSV file."""
    venues = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            venues.append(row)
    return venues

def check_venue_yelp(venue):
    """
    Check a venue against Yelp API.
    Returns: dict with yelp status info
    """
    params = {
        "term": venue["Name"],
        "latitude": float(venue["Lat"]),
        "longitude": float(venue["Lng"]),
        "radius": 200,  # 200 meters
        "limit": 3
    }

    try:
        response = requests.get(YELP_SEARCH_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("businesses"):
            # Find best match (first result usually best due to proximity + name match)
            for biz in data["businesses"]:
                biz_name = biz.get("name", "").lower()
                venue_name = venue["Name"].lower()

                # Check for reasonable name match
                if (venue_name in biz_name or
                    biz_name in venue_name or
                    any(word in biz_name for word in venue_name.split() if len(word) > 3)):

                    return {
                        "found": True,
                        "yelp_name": biz.get("name"),
                        "yelp_id": biz.get("id"),
                        "is_closed": biz.get("is_closed", False),
                        "rating": biz.get("rating"),
                        "review_count": biz.get("review_count", 0)
                    }

            # No good name match, return first result anyway for review
            biz = data["businesses"][0]
            return {
                "found": True,
                "yelp_name": biz.get("name"),
                "yelp_id": biz.get("id"),
                "is_closed": biz.get("is_closed", False),
                "rating": biz.get("rating"),
                "review_count": biz.get("review_count", 0),
                "name_mismatch": True
            }
        else:
            return {"found": False, "is_closed": None}

    except requests.exceptions.RequestException as e:
        return {"found": False, "error": str(e), "is_closed": None}

def main():
    print("=" * 60)
    print("VENUE CLOSURE CHECK - Yelp API")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Load venues from both CSVs
    dupont_venues = load_venues("dupont-leads.csv")
    thu14_venues = load_venues("14thu-leads.csv")

    all_venues = []
    for v in dupont_venues:
        v["source_file"] = "dupont-leads.csv"
        all_venues.append(v)
    for v in thu14_venues:
        v["source_file"] = "14thu-leads.csv"
        all_venues.append(v)

    print(f"\nLoaded {len(all_venues)} venues total")
    print(f"  - Dupont Circle: {len(dupont_venues)}")
    print(f"  - 14th St/U St: {len(thu14_venues)}")
    print("\nChecking venues against Yelp API...")
    print("(This will take a few minutes to avoid rate limits)\n")

    closed_venues = []
    not_found_venues = []
    open_venues = []
    errors = []

    for i, venue in enumerate(all_venues):
        # Progress indicator
        if (i + 1) % 25 == 0 or i == 0:
            print(f"Progress: {i + 1}/{len(all_venues)} venues checked...")

        result = check_venue_yelp(venue)
        venue["yelp_result"] = result

        if result.get("error"):
            errors.append(venue)
        elif not result.get("found"):
            not_found_venues.append(venue)
        elif result.get("is_closed"):
            closed_venues.append(venue)
            print(f"  [CLOSED] {venue['ID']}: {venue['Name']} - {venue['Address']}")
        else:
            open_venues.append(venue)

        # Rate limiting: ~5 requests per second to stay under Yelp limits
        time.sleep(0.2)

    # Generate report
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print(f"\nTotal venues checked: {len(all_venues)}")
    print(f"  Open/Active:        {len(open_venues)}")
    print(f"  PERMANENTLY CLOSED: {len(closed_venues)}")
    print(f"  Not found on Yelp:  {len(not_found_venues)}")
    print(f"  API errors:         {len(errors)}")

    if closed_venues:
        print("\n" + "-" * 60)
        print("CLOSED VENUES (recommend removing from list):")
        print("-" * 60)
        for v in closed_venues:
            yelp = v["yelp_result"]
            print(f"\n  {v['ID']}: {v['Name']}")
            print(f"    Address: {v['Address']}")
            print(f"    File: {v['source_file']}")
            print(f"    Yelp match: {yelp.get('yelp_name', 'N/A')}")

    if not_found_venues:
        print("\n" + "-" * 60)
        print(f"NOT FOUND ON YELP ({len(not_found_venues)} venues):")
        print("(May need manual verification)")
        print("-" * 60)
        for v in not_found_venues[:20]:  # Show first 20
            print(f"  {v['ID']}: {v['Name']} - {v['Address']}")
        if len(not_found_venues) > 20:
            print(f"  ... and {len(not_found_venues) - 20} more")

    # Save detailed results to JSON
    results = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "total": len(all_venues),
            "open": len(open_venues),
            "closed": len(closed_venues),
            "not_found": len(not_found_venues),
            "errors": len(errors)
        },
        "closed_venues": [
            {
                "id": v["ID"],
                "name": v["Name"],
                "address": v["Address"],
                "source_file": v["source_file"],
                "yelp_name": v["yelp_result"].get("yelp_name")
            }
            for v in closed_venues
        ],
        "not_found_venues": [
            {"id": v["ID"], "name": v["Name"], "address": v["Address"]}
            for v in not_found_venues
        ]
    }

    with open("venue_check_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n\nDetailed results saved to: venue_check_results.json")

    # Offer to create filtered CSVs
    if closed_venues:
        print("\n" + "=" * 60)
        print("NEXT STEPS")
        print("=" * 60)
        print(f"\nFound {len(closed_venues)} closed venue(s) to remove.")
        print("Review the list above and the JSON file.")
        print("Run with --remove flag to generate filtered CSV files.")

if __name__ == "__main__":
    main()
