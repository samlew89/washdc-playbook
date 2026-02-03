# DC Venue Lead List — 2,743 Venues

> Comprehensive lead list for all DC neighborhoods, sourced from Yelp Fusion API

---

## Data Overview

| Metric | Count |
|--------|-------|
| **Total Venues** | 2,743 |
| **Priority (85+)** | ~125 |
| **High (60-84)** | ~1,685 |
| **Medium (45-59)** | ~867 |
| **Low (<45)** | ~66 |
| **Neighborhoods** | 18 |
| **Categories** | 8 |

### By Category

| Category | Count |
|----------|-------|
| Restaurant | 1,410 |
| Bar | 605 |
| Coffee | 386 |
| Cafe | 96 |
| Bakery | 94 |
| Nightclub | 71 |
| Wine Bar | 66 |
| Brewery | 15 |

### By Neighborhood

| Neighborhood | Venues |
|--------------|--------|
| Dupont Circle | 504 |
| H Street NE | 275 |
| Penn Quarter / Chinatown | 262 |
| Capitol Hill / Barracks Row | 239 |
| Georgetown | 238 |
| Logan Circle | 221 |
| Adams Morgan | 129 |
| Columbia Heights | 118 |
| Petworth | 111 |
| 14th Street Corridor | 108 |
| Brookland | 106 |
| Navy Yard / The Wharf | 87 |
| NoMa / Union Market | 85 |
| Glover Park / Cathedral | 78 |
| Shaw | 76 |
| U Street | 69 |
| Woodley Park / Cleveland Park | 29 |
| Mount Pleasant | 8 |

---

## Access the Data

### Interactive Tools

- **[Venue Pipeline](venue-list.html)** - Searchable list with filters
- **[Venue Map](density-map.html)** - Interactive map with clustering

### Raw Data Files

- `dc-venues.csv` - Full venue list (CSV format)
- `dc-venues.geojson` - Geographic data for mapping
- `dc-venues-yelp-raw.json` - Raw Yelp API response data

---

## Scoring Methodology

Venues are scored 0-100 using five weighted categories. See [Venue Scoring Rubric](venue-scoring-rubric.md) for full details.

| Category | Weight | Confidence | Data Source |
|----------|--------|------------|-------------|
| Outdoor Mounting Viability | 35% | High | Category inference (rooftop bars, patios) |
| Location & Line-of-Sight | 25% | Low | Neutral baseline (can't detect corners from API) |
| Foot Traffic & Dwell Time | 15% | Medium | Review count + category (coffee = high dwell) |
| Permissioning Speed | 15% | Low | Chain detection + category (independent = better) |
| Operational Reliability | 10% | Medium | Category proxy (coffee shops = long hours) |

**Score Tiers:**
- **85+: Priority** - Immediate outreach, best candidates (~125 venues)
- **60-84: High** - Good candidates, standard pipeline
- **45-59: Medium** - Lower priority, pursue if capacity allows
- **<45: Low** - Deprioritize unless situation changes

*Note: Scoring uses continuous factors (log review count, category type) to create smooth distribution. Yelp ratings and price are NOT used in scoring.*

---

## Data Source

**Yelp Fusion API** (February 2026)

Categories searched:
- restaurants
- bars
- coffee
- bakeries
- breweries
- wine_bars
- cocktailbars
- nightlife
- cafes

---

## Scraper Scripts

To refresh the data:

```bash
# Using Yelp API (current method)
python3 scrape_dc_venues_yelp.py

# Using Google Places API (alternative)
# Set GOOGLE_PLACES_API_KEY environment variable first
python3 scrape_dc_venues.py

# Re-score existing venues without re-scraping
python3 rescore_venues.py
```

Output files:
- `dc-venues-yelp.csv` / `dc-venues.csv`
- `dc-venues-yelp-raw.json`
