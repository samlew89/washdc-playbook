#!/usr/bin/env python3
"""
Re-score existing venue data using updated rubric weights.
Reads from dc-venues-yelp-raw.json, outputs updated CSV.
"""

import csv
import json

NEIGHBORHOODS = {
    "dupont_circle": {"name": "Dupont Circle", "pod_prefix": "DUP"},
    "logan_circle": {"name": "Logan Circle", "pod_prefix": "LOG"},
    "14th_street": {"name": "14th Street Corridor", "pod_prefix": "14TH"},
    "u_street": {"name": "U Street", "pod_prefix": "UST"},
    "shaw": {"name": "Shaw", "pod_prefix": "SHAW"},
    "adams_morgan": {"name": "Adams Morgan", "pod_prefix": "ADAM"},
    "columbia_heights": {"name": "Columbia Heights", "pod_prefix": "COLH"},
    "petworth": {"name": "Petworth", "pod_prefix": "PETW"},
    "h_street": {"name": "H Street NE", "pod_prefix": "HST"},
    "capitol_hill": {"name": "Capitol Hill / Barracks Row", "pod_prefix": "CAPH"},
    "navy_yard": {"name": "Navy Yard / The Wharf", "pod_prefix": "NAVY"},
    "penn_quarter": {"name": "Penn Quarter / Chinatown", "pod_prefix": "PENN"},
    "georgetown": {"name": "Georgetown", "pod_prefix": "GTWN"},
    "glover_park": {"name": "Glover Park / Cathedral", "pod_prefix": "GLOV"},
    "woodley_park": {"name": "Woodley Park / Cleveland Park", "pod_prefix": "WOOD"},
    "brookland": {"name": "Brookland", "pod_prefix": "BROOK"},
    "noma": {"name": "NoMa / Union Market", "pod_prefix": "NOMA"},
    "mt_pleasant": {"name": "Mount Pleasant", "pod_prefix": "MTP"},
}


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
    Generate priority score using updated rubric weights:
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
    outdoor_score = 18  # Neutral baseline
    if any(c in categories for c in ["rooftopbars", "beer_and_wine", "beergardens"]):
        outdoor_score = 30
    elif any(c in categories for c in ["coffee", "cafes", "breweries", "wine_bars", "cocktailbars"]):
        outdoor_score = 24
    elif any(c in categories for c in ["nightlife", "danceclubs"]):
        outdoor_score = 12
    score += outdoor_score

    # --- LOCATION & LINE-OF-SIGHT (0-25) ---
    location_score = 15  # Neutral - needs manual verification
    score += location_score

    # --- FOOT TRAFFIC & DWELL TIME (0-15) ---
    traffic_score = 0
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

    if any(c in categories for c in ["coffee", "cafes", "breweries", "wine_bars", "cocktailbars"]):
        traffic_score += 5
    elif any(c in categories for c in ["restaurants", "newamerican", "italian", "japanese"]):
        traffic_score += 3
    else:
        traffic_score += 2

    if any(c in categories for c in ["beergardens", "rooftopbars"]):
        traffic_score += 4
    elif any(c in categories for c in ["coffee", "cafes", "breweries"]):
        traffic_score += 2
    score += min(traffic_score, 15)

    # --- PERMISSIONING SPEED (0-15) ---
    perm_score = 8
    chain_keywords = ["starbucks", "dunkin", "mcdonald", "subway", "chipotle",
                      "sweetgreen", "cava", "shake shack", "five guys", "panera",
                      "wawa", "7-eleven", "cvs", "walgreens"]
    is_chain = any(kw in name for kw in chain_keywords)

    if is_chain:
        perm_score = 2
    elif any(c in categories for c in ["coffee", "cafes"]):
        perm_score = 12
    elif any(c in categories for c in ["breweries", "wine_bars"]):
        perm_score = 11
    elif any(c in categories for c in ["bars", "cocktailbars"]):
        perm_score = 10
    score += perm_score

    # --- OPERATIONAL RELIABILITY (0-10) ---
    reliability_score = 6
    if any(c in categories for c in ["coffee", "cafes"]):
        reliability_score = 9
    elif any(c in categories for c in ["bars", "nightlife"]):
        reliability_score = 7
    elif rating >= 4.0:
        reliability_score = 8
    score += reliability_score

    return min(score, 95)


def main():
    print("Re-scoring venues with updated rubric...")

    # Load raw venue data
    with open("dc-venues-yelp-raw.json", "r") as f:
        all_venues = json.load(f)

    print(f"Loaded {len(all_venues)} venues")

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
        config = NEIGHBORHOODS.get(nb_key, {"name": nb_key, "pod_prefix": "UNK"})
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

    # Sort by score descending (highest priority first)
    output_rows.sort(key=lambda x: -x["Score"])

    # Write CSV
    output_file = "dc-venues-yelp.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ID", "Name", "Address", "Category", "Neighborhood", "Rating", "Reviews", "Price", "Score", "Lat", "Lng", "Phone", "YelpID"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Output saved to: {output_file}")

    # Also update dc-venues.csv if it exists (for the map)
    with open("dc-venues.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ID", "Name", "Address", "Category", "Neighborhood", "Rating", "Reviews", "Price", "Score", "Lat", "Lng", "Phone", "YelpID"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Also updated: dc-venues.csv")

    # Summary stats
    print(f"\n{'=' * 50}")
    print("SCORE DISTRIBUTION")
    print("=" * 50)
    high = len([r for r in output_rows if r["Score"] >= 75])
    medium = len([r for r in output_rows if 55 <= r["Score"] < 75])
    low = len([r for r in output_rows if r["Score"] < 55])
    print(f"  HOT (75+): {high}")
    print(f"  WARM (55-74): {medium}")
    print(f"  COOL (<55): {low}")

    print(f"\nTop 10 venues by score:")
    for row in output_rows[:10]:
        print(f"  {row['Score']}: {row['Name']} ({row['Category']}) - {row['Neighborhood']}")


if __name__ == "__main__":
    main()
