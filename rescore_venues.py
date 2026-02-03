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
    Generate priority score using updated rubric weights with SMOOTH distribution.
    Uses continuous scoring to create ~100 priority venues (75+) and even spread.

    Categories:
    - Outdoor Mounting Viability: 35% (inferred from category)
    - Location & Line-of-Sight: 25% (rating as proxy for desirable location)
    - Foot Traffic & Dwell Time: 15% (review count + category)
    - Permissioning Speed: 15% (chain detection + category)
    - Operational Reliability: 10% (category proxy)
    """
    import math

    categories = [c.get("alias", "") for c in biz.get("categories", [])]
    name = biz.get("name", "").lower()
    reviews = biz.get("review_count", 0)
    rating = biz.get("rating", 0) or 3.5  # Default if missing

    score = 0.0

    # --- OUTDOOR MOUNTING VIABILITY (0-35) ---
    # Base by category + rating boost for quality venues
    if any(c in categories for c in ["rooftopbars", "beergardens"]):
        outdoor_base = 28
    elif any(c in categories for c in ["breweries", "brewpubs"]):
        outdoor_base = 26
    elif any(c in categories for c in ["coffee", "coffeeroasteries"]):
        outdoor_base = 24
    elif any(c in categories for c in ["wine_bars", "cocktailbars", "cafes"]):
        outdoor_base = 22
    elif any(c in categories for c in ["bars"]):
        outdoor_base = 20
    elif any(c in categories for c in ["nightlife", "danceclubs"]):
        outdoor_base = 14
    else:
        outdoor_base = 18  # Restaurants and others

    # Rating boost (0-7): higher rated = likely better maintained building
    outdoor_rating_boost = ((rating - 3.0) / 2.0) * 7  # 3.0 rating = 0, 5.0 rating = 7
    outdoor_rating_boost = max(0, min(7, outdoor_rating_boost))

    score += outdoor_base + outdoor_rating_boost

    # --- LOCATION & LINE-OF-SIGHT (0-25) ---
    # Use log(reviews) as proxy for prime location (more reviews = busier area)
    # Plus rating as quality indicator
    if reviews > 0:
        review_location_score = min(15, math.log10(reviews + 1) * 5)  # 0-15 based on reviews
    else:
        review_location_score = 5

    rating_location_boost = ((rating - 3.0) / 2.0) * 10  # 0-10 based on rating
    rating_location_boost = max(0, min(10, rating_location_boost))

    score += review_location_score + rating_location_boost

    # --- FOOT TRAFFIC & DWELL TIME (0-15) ---
    # Continuous review count scoring (log scale)
    if reviews > 0:
        review_traffic = min(8, math.log10(reviews + 1) * 2.5)
    else:
        review_traffic = 1

    # Dwell time by category (0-7)
    if any(c in categories for c in ["coffee", "coffeeroasteries", "cafes"]):
        dwell_score = 7
    elif any(c in categories for c in ["breweries", "brewpubs", "wine_bars", "cocktailbars"]):
        dwell_score = 6
    elif any(c in categories for c in ["bars"]):
        dwell_score = 5
    elif any(c in categories for c in ["restaurants", "newamerican", "italian", "japanese", "mexican"]):
        dwell_score = 4
    else:
        dwell_score = 3

    score += min(15, review_traffic + dwell_score)

    # --- PERMISSIONING SPEED (0-15) ---
    chain_keywords = ["starbucks", "dunkin", "mcdonald", "subway", "chipotle",
                      "sweetgreen", "cava", "shake shack", "five guys", "panera",
                      "wawa", "7-eleven", "cvs", "walgreens", "peet's", "philz"]
    is_chain = any(kw in name for kw in chain_keywords)

    if is_chain:
        perm_base = 2
    elif any(c in categories for c in ["coffee", "coffeeroasteries", "cafes"]):
        perm_base = 13
    elif any(c in categories for c in ["breweries", "brewpubs"]):
        perm_base = 12
    elif any(c in categories for c in ["wine_bars"]):
        perm_base = 11
    elif any(c in categories for c in ["cocktailbars", "bars"]):
        perm_base = 10
    else:
        perm_base = 8

    # Small boost for highly rated (owner cares about business)
    if rating >= 4.5:
        perm_base = min(15, perm_base + 2)
    elif rating >= 4.0:
        perm_base = min(15, perm_base + 1)

    score += perm_base

    # --- OPERATIONAL RELIABILITY (0-10) ---
    if any(c in categories for c in ["coffee", "coffeeroasteries", "cafes"]):
        reliability_base = 8
    elif any(c in categories for c in ["breweries", "brewpubs"]):
        reliability_base = 7
    elif any(c in categories for c in ["bars", "cocktailbars", "wine_bars"]):
        reliability_base = 6
    else:
        reliability_base = 5

    # Rating boost for reliability
    if rating >= 4.5:
        reliability_base = min(10, reliability_base + 2)
    elif rating >= 4.0:
        reliability_base = min(10, reliability_base + 1)

    score += reliability_base

    return round(min(100, max(0, score)))


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
    priority = len([r for r in output_rows if r["Score"] >= 80])
    high = len([r for r in output_rows if 60 <= r["Score"] < 80])
    medium = len([r for r in output_rows if 45 <= r["Score"] < 60])
    low = len([r for r in output_rows if r["Score"] < 45])
    print(f"  Priority (80+): {priority}")
    print(f"  High (60-79): {high}")
    print(f"  Medium (45-59): {medium}")
    print(f"  Low (<45): {low}")

    print(f"\nTop 10 venues by score:")
    for row in output_rows[:10]:
        print(f"  {row['Score']}: {row['Name']} ({row['Category']}) - {row['Neighborhood']}")


if __name__ == "__main__":
    main()
