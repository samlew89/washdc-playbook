#!/usr/bin/env python3
"""
Scrape DC bars and restaurants using Google Places API.
Comprehensive coverage by neighborhood with proper deduplication.
"""

import csv
import requests
import time
import json
import os
from datetime import datetime

# Get API key from environment or set directly
GOOGLE_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY", "YOUR_API_KEY_HERE")

PLACES_NEARBY_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACES_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# DC Neighborhoods with center coordinates and search radius (meters)
NEIGHBORHOODS = {
    "dupont_circle": {
        "name": "Dupont Circle",
        "lat": 38.9096,
        "lng": -77.0434,
        "radius": 800,
        "pod_prefix": "DUP"
    },
    "logan_circle": {
        "name": "Logan Circle",
        "lat": 38.9096,
        "lng": -77.0295,
        "radius": 600,
        "pod_prefix": "LOG"
    },
    "14th_street": {
        "name": "14th Street Corridor",
        "lat": 38.9170,
        "lng": -77.0320,
        "radius": 800,
        "pod_prefix": "14TH"
    },
    "u_street": {
        "name": "U Street",
        "lat": 38.9170,
        "lng": -77.0280,
        "radius": 700,
        "pod_prefix": "UST"
    },
    "shaw": {
        "name": "Shaw",
        "lat": 38.9120,
        "lng": -77.0220,
        "radius": 800,
        "pod_prefix": "SHAW"
    },
    "adams_morgan": {
        "name": "Adams Morgan",
        "lat": 38.9215,
        "lng": -77.0425,
        "radius": 700,
        "pod_prefix": "ADAM"
    },
    "columbia_heights": {
        "name": "Columbia Heights",
        "lat": 38.9285,
        "lng": -77.0325,
        "radius": 800,
        "pod_prefix": "COLH"
    },
    "petworth": {
        "name": "Petworth",
        "lat": 38.9420,
        "lng": -77.0250,
        "radius": 800,
        "pod_prefix": "PETW"
    },
    "h_street": {
        "name": "H Street NE",
        "lat": 38.9000,
        "lng": -76.9900,
        "radius": 800,
        "pod_prefix": "HST"
    },
    "capitol_hill": {
        "name": "Capitol Hill / Barracks Row",
        "lat": 38.8850,
        "lng": -76.9950,
        "radius": 900,
        "pod_prefix": "CAPH"
    },
    "navy_yard": {
        "name": "Navy Yard / The Wharf",
        "lat": 38.8760,
        "lng": -77.0030,
        "radius": 1000,
        "pod_prefix": "NAVY"
    },
    "penn_quarter": {
        "name": "Penn Quarter / Chinatown",
        "lat": 38.8975,
        "lng": -77.0220,
        "radius": 700,
        "pod_prefix": "PENN"
    },
    "georgetown": {
        "name": "Georgetown",
        "lat": 38.9055,
        "lng": -77.0636,
        "radius": 900,
        "pod_prefix": "GTWN"
    },
    "glover_park": {
        "name": "Glover Park / Cathedral",
        "lat": 38.9290,
        "lng": -77.0700,
        "radius": 800,
        "pod_prefix": "GLOV"
    },
    "woodley_park": {
        "name": "Woodley Park / Cleveland Park",
        "lat": 38.9350,
        "lng": -77.0580,
        "radius": 800,
        "pod_prefix": "WOOD"
    },
    "brookland": {
        "name": "Brookland",
        "lat": 38.9330,
        "lng": -76.9940,
        "radius": 800,
        "pod_prefix": "BROOK"
    },
    "noma": {
        "name": "NoMa / Union Market",
        "lat": 38.9070,
        "lng": -77.0030,
        "radius": 700,
        "pod_prefix": "NOMA"
    },
    "mt_pleasant": {
        "name": "Mount Pleasant",
        "lat": 38.9290,
        "lng": -77.0380,
        "radius": 500,
        "pod_prefix": "MTP"
    }
}

# Place types to search (Google Places API types)
PLACE_TYPES = [
    "restaurant",
    "bar",
    "cafe",
    "bakery",
    "night_club",
    "meal_takeaway",
    "brewery",  # May not be recognized, but try
]

# Category mapping from Google types
CATEGORY_MAP = {
    "restaurant": "Restaurant",
    "bar": "Bar",
    "cafe": "Cafe",
    "bakery": "Bakery",
    "night_club": "Nightclub",
    "meal_takeaway": "Restaurant",
    "meal_delivery": "Restaurant",
    "food": "Restaurant",
    "liquor_store": "Retail",
    "convenience_store": "Convenience",
    "grocery_or_supermarket": "Grocery",
}


def search_nearby(lat, lng, radius, place_type):
    """Search for places near a location."""
    all_results = []

    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "type": place_type,
        "key": GOOGLE_API_KEY
    }

    while True:
        response = requests.get(PLACES_NEARBY_URL, params=params, timeout=15)
        data = response.json()

        if data.get("status") not in ["OK", "ZERO_RESULTS"]:
            print(f"  API Error: {data.get('status')} - {data.get('error_message', '')}")
            break

        results = data.get("results", [])
        all_results.extend(results)

        # Check for more pages
        next_page_token = data.get("next_page_token")
        if next_page_token:
            # Google requires a short delay before using next_page_token
            time.sleep(2)
            params = {"pagetoken": next_page_token, "key": GOOGLE_API_KEY}
        else:
            break

    return all_results


def get_place_details(place_id):
    """Get detailed info for a place."""
    params = {
        "place_id": place_id,
        "fields": "name,formatted_address,geometry,types,price_level,rating,user_ratings_total,website,formatted_phone_number,opening_hours",
        "key": GOOGLE_API_KEY
    }

    response = requests.get(PLACES_DETAILS_URL, params=params, timeout=15)
    data = response.json()

    if data.get("status") == "OK":
        return data.get("result", {})
    return None


def categorize_venue(types):
    """Determine venue category from Google place types."""
    for t in types:
        if t in CATEGORY_MAP:
            return CATEGORY_MAP[t]
    # Default based on common patterns
    if "food" in types or "point_of_interest" in types:
        return "Restaurant"
    return "Venue"


def score_venue(venue_data):
    """Generate a priority score based on venue attributes."""
    score = 70  # Base score

    rating = venue_data.get("rating", 0)
    reviews = venue_data.get("user_ratings_total", 0)

    # Rating boost (up to +15)
    if rating >= 4.5:
        score += 15
    elif rating >= 4.0:
        score += 10
    elif rating >= 3.5:
        score += 5

    # Review count boost (indicates popularity, up to +10)
    if reviews >= 500:
        score += 10
    elif reviews >= 200:
        score += 7
    elif reviews >= 100:
        score += 5
    elif reviews >= 50:
        score += 3

    # Price level can indicate establishment type
    price = venue_data.get("price_level", 2)
    if price >= 3:  # Higher end
        score += 3

    return min(score, 95)  # Cap at 95


def scrape_neighborhood(neighborhood_key, neighborhood_config):
    """Scrape all venues in a neighborhood."""
    print(f"\nScraping {neighborhood_config['name']}...")

    all_venues = {}  # Use place_id as key to dedupe

    for place_type in PLACE_TYPES:
        print(f"  Searching for: {place_type}")
        results = search_nearby(
            neighborhood_config["lat"],
            neighborhood_config["lng"],
            neighborhood_config["radius"],
            place_type
        )
        print(f"    Found {len(results)} results")

        for place in results:
            place_id = place.get("place_id")
            if place_id and place_id not in all_venues:
                all_venues[place_id] = {
                    "place_id": place_id,
                    "name": place.get("name"),
                    "address": place.get("vicinity", ""),
                    "lat": place.get("geometry", {}).get("location", {}).get("lat"),
                    "lng": place.get("geometry", {}).get("location", {}).get("lng"),
                    "types": place.get("types", []),
                    "rating": place.get("rating"),
                    "user_ratings_total": place.get("user_ratings_total", 0),
                    "price_level": place.get("price_level"),
                    "neighborhood": neighborhood_key,
                    "pod_prefix": neighborhood_config["pod_prefix"]
                }

        # Small delay between searches
        time.sleep(0.5)

    print(f"  Total unique venues: {len(all_venues)}")
    return list(all_venues.values())


def main():
    print("=" * 60)
    print("DC VENUE SCRAPER - Google Places API")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if GOOGLE_API_KEY == "YOUR_API_KEY_HERE":
        print("\nERROR: Please set your Google Places API key!")
        print("Either:")
        print("  1. Set GOOGLE_PLACES_API_KEY environment variable")
        print("  2. Edit this script and replace YOUR_API_KEY_HERE")
        print("\nTo get an API key:")
        print("  1. Go to https://console.cloud.google.com/")
        print("  2. Create a project and enable 'Places API'")
        print("  3. Create credentials (API Key)")
        return

    all_venues = []
    seen_place_ids = set()

    for neighborhood_key, config in NEIGHBORHOODS.items():
        venues = scrape_neighborhood(neighborhood_key, config)

        # Deduplicate across neighborhoods
        for v in venues:
            if v["place_id"] not in seen_place_ids:
                seen_place_ids.add(v["place_id"])
                all_venues.append(v)

    print(f"\n{'=' * 60}")
    print(f"TOTAL UNIQUE VENUES: {len(all_venues)}")
    print("=" * 60)

    # Generate IDs and format for CSV
    venues_by_neighborhood = {}
    for v in all_venues:
        nb = v["neighborhood"]
        if nb not in venues_by_neighborhood:
            venues_by_neighborhood[nb] = []
        venues_by_neighborhood[nb].append(v)

    # Create CSV output
    output_rows = []
    for nb_key, venues in venues_by_neighborhood.items():
        config = NEIGHBORHOODS[nb_key]
        prefix = config["pod_prefix"]

        for i, v in enumerate(venues, 1):
            venue_id = f"{prefix}-{i:03d}"
            category = categorize_venue(v.get("types", []))
            score = score_venue(v)

            output_rows.append({
                "ID": venue_id,
                "Name": v["name"],
                "Address": v["address"],
                "Category": category,
                "Neighborhood": config["name"],
                "Rating": v.get("rating", ""),
                "Reviews": v.get("user_ratings_total", ""),
                "Score": score,
                "Lat": v["lat"],
                "Lng": v["lng"],
                "PlaceID": v["place_id"]
            })

    # Sort by neighborhood then score
    output_rows.sort(key=lambda x: (x["Neighborhood"], -x["Score"]))

    # Write CSV
    output_file = "dc-venues-google.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ID", "Name", "Address", "Category", "Neighborhood", "Rating", "Reviews", "Score", "Lat", "Lng", "PlaceID"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\nOutput saved to: {output_file}")

    # Also save raw JSON for reference
    with open("dc-venues-raw.json", "w", encoding="utf-8") as f:
        json.dump(all_venues, f, indent=2)
    print(f"Raw data saved to: dc-venues-raw.json")

    # Print summary by neighborhood
    print(f"\n{'=' * 60}")
    print("VENUES BY NEIGHBORHOOD")
    print("=" * 60)
    for nb_key in NEIGHBORHOODS:
        count = len(venues_by_neighborhood.get(nb_key, []))
        name = NEIGHBORHOODS[nb_key]["name"]
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
