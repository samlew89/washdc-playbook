# WORKPLAN.md — DC Playbook

## Project Goal
Create a highly readable, operator-friendly dashboard for driving hyper-dense Helium Mobile hotspot deployments in Washington DC, covering 18 neighborhoods with comprehensive venue data.

The dashboard should prioritize:
- Venue lead generation + qualification
- Dense clustering across DC neighborhoods
- Clear "what to do next" for outreach + installs
- Hardware planning tied to venue pipeline

---

## Completed Work (Feb 2026)

### Comprehensive Venue Data Expansion
- [x] Replaced manually curated 536-venue list with Yelp Fusion API data
- [x] Expanded from 2 neighborhoods to 18 neighborhoods across DC
- [x] New venue count: **2,743 venues** (was 536)
- [x] Created `scrape_dc_venues_yelp.py` for reproducible data pulls
- [x] Created `scrape_dc_venues.py` for Google Places API alternative
- [x] Updated scoring algorithm based on venue rubric weights

### Updated HTML Pages
- [x] `density-map.html` - Category filter chips, 18 neighborhoods, rating filter
- [x] `venue-list.html` - Complete rebuild for new data format with category filters
- [x] Both pages now load from single `dc-venues.csv` file

### Neighborhoods Now Covered
Dupont Circle, Logan Circle, 14th Street Corridor, U Street, Shaw, Adams Morgan, Columbia Heights, Petworth, H Street NE, Capitol Hill/Barracks Row, Navy Yard/The Wharf, Penn Quarter/Chinatown, Georgetown, Glover Park, Woodley Park/Cleveland Park, Brookland, NoMa/Union Market, Mount Pleasant

### Data Files
- `dc-venues.csv` - 2,743 venues with Yelp data
- `dc-venues.geojson` - Updated geographic data
- `dc-venues-yelp-raw.json` - Raw API response backup

### Codebase Cleanup
- [x] Removed old data files (`*-old.csv`, duplicate CSVs)
- [x] Removed obsolete scripts (`check_closed_venues.py`, `clean_venue_lists.py`)
- [x] Removed intermediate JSON files
- [x] Added missing docs to sidebar (`venue-lead-generation-system.md`, `7-day-sprint-plan.md`)

---

## Completed Work (Jan 2026)

### Deployment & Hosting
- [x] Pushed to GitHub: https://github.com/samlew89/washdc-playbook
- [x] Deployed to Vercel (auto-deploys on push)
- [x] Added robots.txt to block crawlers
- [x] Added noindex/nofollow meta tags to all HTML pages
- [x] Set default homepage to Summary & Goals (Docsify `homepage` config)

### Mobile Responsive Design
- [x] **index.html**: Hamburger menu + slide-in sidebar drawer
- [x] **index.html**: Overlay backdrop, closes on tap outside or link tap
- [x] **index.html**: Scaled typography for mobile (h1, h2, h3)
- [x] **index.html**: Tables auto-wrapped for horizontal scroll
- [x] **venue-list.html**: Stats display as even 5-across row
- [x] **venue-list.html**: Filters stack vertically, full-width inputs
- [x] **venue-list.html**: Venue cards stack naturally (score inline)
- [x] **density-map.html**: Controls bar horizontally scrollable
- [x] **density-map.html**: Compact legend, hidden tooltips on touch
- [x] **density-map.html**: Popups constrained to viewport

### Overview Page
- [x] Added Summary & Goals section with executive summary
- [x] Added Network BU Plan (4 pillars)
- [x] Added KPIs section
- [x] Removed Quick Links (redundant with sidebar)
- [x] Simplified BU Plan item 1 (single bullet)

### Lead List & Pipeline Page
- [x] Renamed from README.md to lead-list.md
- [x] Venue Pipeline with 4 collapsible sections (all closed by default)
  - Priority Venues (97 venues, score 85+) - marked as "subset"
  - Dupont Circle (300 venues)
  - 14th St + U St Corridor (300 venues)
  - Data Sources
- [x] Venue names are clickable (Google search in new tab)
- [x] Removed expanded venue details (cleaner UX)
- [x] Sticky filter bar when scrolling
- [x] Hardware Requirements updated to "Max Build-Out" model:
  - All Venues: 600 indoor + 252 outdoor = 852 total
  - Priority Only: 97 indoor + 78 outdoor = 175 total

### Venue Map (density-map.html)
- [x] Modern redesign with Carto Positron basemap
- [x] Loads all 600 venues from CSV (no hardcoded limit)
- [x] Marker clustering (leaflet.markercluster) for performance
- [x] Score-based color coding: Purple (85+), Blue (70-84), Orange (50-69), Red (<50)
- [x] Hover tooltips: "Venue Name · Score"
- [x] Click popups with: Name (search link), Address, Neighborhood, Category, Outdoor viable badge
- [x] Live "Showing X / 600 venues" counter
- [x] Filters: Neighborhood, Zone, Min Score (50-100), Outdoor Viable Only
- [x] Show Zones toggle (dashed boundary polygons)

### Sidebar & Navigation
- [x] Custom branded header: Helium logo + "DC Playbook"
- [x] Removed search bar
- [x] Disabled auto-generated sub-sections (subMaxLevel: 0)
- [x] Clean section structure: Overview, Dashboard, Programs, Reference

### Programs
- [x] Added Deployer Bootcamp page (from PDF content)
- [x] Ambassador Program trimmed to Parts 1-2 only (Compensation Plan + Job Description)
- [x] Ambassador job posting formatted to match official Helium Foundation template
- [x] Job posting adapted for Washington D.C. (experience requirement: 1+ years or equivalent hustle)

### Venue Data Cleanup (Jan 2026)
*Note: This work was superseded by the Feb 2026 Yelp API integration which replaced all manual venue data.*

- [x] Used Yelp API to check venues for permanent closures
- [x] Removed closed and duplicate venues
- [x] Original totals: 536 venues across 2 neighborhoods

---

## Technical Notes

### Data Files
- `dc-venues.csv` - 2,743 venues across 18 neighborhoods (from Yelp API)
- `dc-venues.geojson` - Geographic data for mapping
- `dc-venues-yelp-raw.json` - Raw API response backup
- `venues.db` - SQLite database for external tools (Superset, etc.)
- CSV columns: ID, Name, Address, Category, Neighborhood, Rating, Reviews, Price, Score, Lat, Lng, Phone, YelpID

### External Integrations (Superset, BI Tools)

The venue data can be shared with external platforms via SQLite database:

**Database:** `venues.db`
**Table:** `venues`

| Column | Type | Description |
|--------|------|-------------|
| id | TEXT | Venue ID (e.g., DUP-001) |
| name | TEXT | Venue name |
| address | TEXT | Full address |
| category | TEXT | Coffee, Bar, Brewery, etc. |
| neighborhood | TEXT | One of 18 DC neighborhoods |
| score | INTEGER | Priority score (0-100) |
| priority_tier | TEXT | Priority, High, Medium, Low |
| rating | REAL | Yelp rating |
| reviews | INTEGER | Review count |
| lat, lng | REAL | Coordinates |
| phone, yelp_id | TEXT | Contact info |

**To regenerate the database after updating venue data:**
```bash
python3 create_venue_db.py
```

**To connect from Superset:**
Add database connection: `sqlite:////path/to/venues.db`

### Key Thresholds
- Priority: Score >= 85 (~125 venues)
- High: Score 60-84 (~1,685 venues)
- Medium: Score 45-59 (~867 venues)
- Low: Score < 45 (~66 venues)

*Note: Scoring uses continuous factors (log review count, category type) for smooth distribution. Yelp ratings and price are NOT used in scoring.*

### Scoring Algorithm (Yelp-based)
- Outdoor Mounting Viability: 35% (inferred from category)
- Location & Line-of-Sight: 25% (neutral baseline)
- Foot Traffic & Dwell Time: 15% (reviews + category)
- Permissioning Speed: 15% (chain detection + category)
- Operational Reliability: 10% (category proxy)

### Libraries Used
- Docsify 4.x - Documentation framework
- Leaflet 1.9.4 - Mapping
- Leaflet.markercluster 1.4.1 - Marker clustering
- Carto Positron tiles - Basemap (free, no API key)

### Mobile Breakpoints
- 768px - Tablet/mobile transition
- 480px - Small mobile adjustments

### Neighborhoods
18 total: Dupont Circle, Logan Circle, 14th Street, U Street, Shaw, Adams Morgan, Columbia Heights, Petworth, H Street NE, Capitol Hill, Navy Yard/Wharf, Penn Quarter, Georgetown, Glover Park, Woodley Park, Brookland, NoMa, Mount Pleasant

---

## Future Improvements (Ideas)

- [ ] Add venue status tracking (Not Started → Contacted → Closed → Installed)
- [ ] Export filtered venue lists to CSV
- [ ] Add "Copy to clipboard" for venue addresses
- [ ] Dark mode support
- [ ] Integration with deployment tracking system

---

## Deployment

**Live Site:** Auto-deploys via Vercel on every push to main.

**To deploy changes:**
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Vercel will automatically build and deploy within ~1 minute. No manual steps needed.

**To trigger a redeploy without changes:**
```bash
git commit --allow-empty -m "Trigger redeploy"
git push origin main
```

---

## Running Locally
```bash
cd /Users/samuellewis/Projects/WashDC
python3 -m http.server 8000
# Open http://localhost:8000
```
