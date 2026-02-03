#!/usr/bin/env python3
"""
Scrape DC bars and restaurants using Yelp Fusion API.
Uses existing Yelp API key - comprehensive coverage by neighborhood.
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

# Yelp categories to search
YELP_CATEGORIES = [
    "bars",
    "restaurants",
    "coffee",
    "bakeries",
    "breweries",
    "wine_bars",
    "cocktailbars",
    "nightlife",
    "cafes",
]


def search_yelp(lat, lng, radius, categories):
    """Search Yelp for businesses."""
    all_results = []
    offset = 0
    limit = 50  # Yelp max per request

    while True:
        params = {
            "latitude": lat,
            "longitude": lng,
            "radius": radius,
            "categories": categories,
            "limit": limit,
            "offset": offset,
            "sort_by": "best_match"
        }

        try:
            response = requests.get(YELP_SEARCH_URL, headers=HEADERS, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"    API Error: {e}")
            break

        businesses = data.get("businesses", [])
        all_results.extend(businesses)

        total = data.get("total", 0)
        offset += limit

        # Yelp limits to 1000 results total, and we paginate through
        if offset >= total or offset >= 1000 or len(businesses) == 0:
            break

        time.sleep(0.3)  # Rate limiting

    return all_results


def categorize_from_yelp(categories):
    """Map Yelp categories to our categories."""
    category_aliases = [c.get("alias", "") for c in categories]

    if any(c in category_aliases for c in ["bars", "cocktailbars", "divebars", "sportsbars", "whiskeybars", "beerbar"]):
        return "Bar"
    if any(c in category_aliases for c in ["breweries", "brewpubs"]):
        return "Brewery"
    if any(c in category_aliases for c in ["wine_bars", "wineries"]):
        return "Wine Bar"
    if any(c in category_aliases for c in ["coffee", "coffeeroasteries"]):
        return "Coffee"
    if any(c in category_aliases for c in ["bakeries"]):
        return "Bakery"
    if any(c in category_aliases for c in ["cafes", "cafeteria"]):
        return "Cafe"
    if any(c in category_aliases for c in ["nightlife", "danceclubs", "musicvenues"]):
        return "Nightclub"
    return "Restaurant"


def score_venue(biz):
    """
    Generate priority score from Yelp data using updated rubric weights:
    - Outdoor Mounting Viability: 35% (inferred from category)
    - Location & Line-of-Sight: 25% (neutral - can't determine from API)
    - Foot Traffic & Dwell Time: 15% (review count + category)
    - Permissioning Speed: 15% (chain detection + category)
    - Operational Reliability: 10% (category proxy)
    """
    score = 0
    categories = [c.get("alias", "") for c in biz.get("categories", [])]
    name = biz.get("name", "").lower()
    reviews = biz.get("review_count", 0)
    rating = biz.get("rating", 0)

    # --- OUTDOOR MOUNTING VIABILITY (0-35) ---
    # Inferred from category - rooftops, patios, outdoor indicators
    outdoor_score = 18  # Neutral baseline
    if any(c in categories for c in ["rooftopbars", "beer_and_wine", "beergardens"]):
        outdoor_score = 30  # Likely has outdoor/rooftop
    elif any(c in categories for c in ["coffee", "cafes", "breweries", "wine_bars", "cocktailbars"]):
        outdoor_score = 24  # Often have patios
    elif any(c in categories for c in ["nightlife", "danceclubs"]):
        outdoor_score = 12  # Usually indoor-only
    score += outdoor_score

    # --- LOCATION & LINE-OF-SIGHT (0-25) ---
    # Can't determine corner lots from API - use neutral score
    location_score = 15  # Neutral - needs manual verification
    score += location_score

    # --- FOOT TRAFFIC & DWELL TIME (0-15) ---
    traffic_score = 0
    # Review count as traffic proxy (0-6)
    if reviews >= 500:
        traffic_score += 6
    elif reviews >= 200:
        traffic_score += 5
    elif reviews >= 100:
        traffic_score += 4
    elif reviews >= 50:
        traffic_score += 3
    else:
        traffic_score += 1

    # Dwell time from category (0-5)
    if any(c in categories for c in ["coffee", "cafes", "breweries", "wine_bars", "cocktailbars"]):
        traffic_score += 5  # High dwell
    elif any(c in categories for c in ["restaurants", "newamerican", "italian", "japanese"]):
        traffic_score += 3  # Medium dwell
    else:
        traffic_score += 2  # Low-medium dwell

    # Outdoor seating indicator (0-4)
    if any(c in categories for c in ["beergardens", "rooftopbars"]):
        traffic_score += 4
    elif any(c in categories for c in ["coffee", "cafes", "breweries"]):
        traffic_score += 2  # Often have outdoor
    score += min(traffic_score, 15)

    # --- PERMISSIONING SPEED (0-15) ---
    # Chain detection + category-based owner-operated inference
    perm_score = 8  # Neutral baseline

    # Chain detection (lowers score)
    chain_keywords = ["starbucks", "dunkin", "mcdonald", "subway", "chipotle",
                      "sweetgreen", "cava", "shake shack", "five guys", "panera",
                      "wawa", "7-eleven", "cvs", "walgreens"]
    is_chain = any(kw in name for kw in chain_keywords)

    if is_chain:
        perm_score = 2  # National chain
    elif any(c in categories for c in ["coffee", "cafes"]):
        perm_score = 12  # Likely owner-operated
    elif any(c in categories for c in ["breweries", "wine_bars"]):
        perm_score = 11  # Usually independent
    elif any(c in categories for c in ["bars", "cocktailbars"]):
        perm_score = 10  # Often independent
    score += perm_score

    # --- OPERATIONAL RELIABILITY (0-10) ---
    # Category-based proxy
    reliability_score = 6  # Neutral
    if any(c in categories for c in ["coffee", "cafes"]):
        reliability_score = 9  # Long hours, tech-forward
    elif any(c in categories for c in ["bars", "nightlife"]):
        reliability_score = 7  # Evening hours but consistent
    elif rating >= 4.0:
        reliability_score = 8  # Higher rated = more reliable operation
    score += reliability_score

    return min(score, 95)


def scrape_neighborhood(neighborhood_key, config):
    """Scrape all venues in a neighborhood."""
    print(f"\nScraping {config['name']}...")

    all_venues = {}  # Dedupe by Yelp ID

    for category in YELP_CATEGORIES:
        print(f"  Searching: {category}")
        results = search_yelp(
            config["lat"],
            config["lng"],
            config["radius"],
            category
        )
        print(f"    Found {len(results)} results")

        for biz in results:
            yelp_id = biz.get("id")
            if yelp_id and yelp_id not in all_venues:
                # Skip closed businesses
                if biz.get("is_closed"):
                    continue

                location = biz.get("location", {})
                coords = biz.get("coordinates", {})

                all_venues[yelp_id] = {
                    "yelp_id": yelp_id,
                    "name": biz.get("name"),
                    "address": ", ".join(filter(None, [
                        location.get("address1"),
                        location.get("city"),
                        location.get("state"),
                        location.get("zip_code")
                    ])),
                    "lat": coords.get("latitude"),
                    "lng": coords.get("longitude"),
                    "categories": biz.get("categories", []),
                    "rating": biz.get("rating"),
                    "review_count": biz.get("review_count", 0),
                    "price": biz.get("price"),
                    "phone": biz.get("phone"),
                    "neighborhood": neighborhood_key,
                    "pod_prefix": config["pod_prefix"]
                }

        time.sleep(0.3)

    print(f"  Total unique venues: {len(all_venues)}")
    return list(all_venues.values())


def main():
    print("=" * 60)
    print("DC VENUE SCRAPER - Yelp Fusion API")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    all_venues = []
    seen_ids = set()

    for neighborhood_key, config in NEIGHBORHOODS.items():
        venues = scrape_neighborhood(neighborhood_key, config)

        # Dedupe across neighborhoods
        for v in venues:
            if v["yelp_id"] not in seen_ids:
                seen_ids.add(v["yelp_id"])
                all_venues.append(v)

    print(f"\n{'=' * 60}")
    print(f"TOTAL UNIQUE VENUES: {len(all_venues)}")
    print("=" * 60)

    # Group by neighborhood
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

        # Sort by score within neighborhood
        venues_sorted = sorted(venues, key=lambda x: -score_venue(x))

        for i, v in enumerate(venues_sorted, 1):
            venue_id = f"{prefix}-{i:03d}"
            category = categorize_from_yelp(v.get("categories", []))
            score = score_venue(v)

            output_rows.append({
                "ID": venue_id,
                "Name": v["name"],
                "Address": v["address"],
                "Category": category,
                "Neighborhood": config["name"],
                "Rating": v.get("rating", ""),
                "Reviews": v.get("review_count", ""),
                "Price": v.get("price", ""),
                "Score": score,
                "Lat": v["lat"],
                "Lng": v["lng"],
                "Phone": v.get("phone", ""),
                "YelpID": v["yelp_id"]
            })

    # Sort by neighborhood then score
    output_rows.sort(key=lambda x: (x["Neighborhood"], -x["Score"]))

    # Write CSV
    output_file = "dc-venues-yelp.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ID", "Name", "Address", "Category", "Neighborhood", "Rating", "Reviews", "Price", "Score", "Lat", "Lng", "Phone", "YelpID"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"\nOutput saved to: {output_file}")

    # Save raw JSON
    with open("dc-venues-yelp-raw.json", "w", encoding="utf-8") as f:
        json.dump(all_venues, f, indent=2)
    print(f"Raw data saved to: dc-venues-yelp-raw.json")

    # Summary
    print(f"\n{'=' * 60}")
    print("VENUES BY NEIGHBORHOOD")
    print("=" * 60)
    for nb_key in NEIGHBORHOODS:
        count = len(venues_by_neighborhood.get(nb_key, []))
        name = NEIGHBORHOODS[nb_key]["name"]
        print(f"  {name}: {count}")

    # Category breakdown
    print(f"\n{'=' * 60}")
    print("VENUES BY CATEGORY")
    print("=" * 60)
    categories = {}
    for row in output_rows:
        cat = row["Category"]
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
