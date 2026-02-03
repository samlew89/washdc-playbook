# DC Venue Lead List — 2,743 Venues

> Comprehensive lead list for all DC neighborhoods, sourced from Yelp Fusion API

---

## Data Overview

| Metric | Count |
|--------|-------|
| **Total Venues** | 2,743 |
| **Priority (Score 85+)** | 583 |
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

Venues are scored 70-95 based on Yelp data:

| Factor | Points |
|--------|--------|
| Base Score | 70 |
| Rating 4.5+ | +15 |
| Rating 4.0-4.4 | +10 |
| Rating 3.5-3.9 | +5 |
| 500+ Reviews | +10 |
| 200-499 Reviews | +7 |
| 100-199 Reviews | +5 |
| 50-99 Reviews | +3 |
| Price $$$ or $$$$ | +3 |

**Score Tiers:**
- **85-95: Priority** - High visibility, popular venues
- **70-84: High** - Good deployment candidates
- **50-69: Medium** - Consider for coverage
- **<50: Low** - Lower priority

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
```

Output files:
- `dc-venues-yelp.csv` / `dc-venues.csv`
- `dc-venues-yelp-raw.json`
