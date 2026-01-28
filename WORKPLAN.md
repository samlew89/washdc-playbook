# WORKPLAN.md — DC Playbook

## Project Goal
Create a highly readable, operator-friendly dashboard for driving hyper-dense Helium Mobile hotspot deployments in Washington DC, focused on:
- Dupont Circle (300 venues)
- 14th St NW + U St Corridor (300 venues)

The dashboard should prioritize:
- Venue lead generation + qualification
- Dense clustering within defined pods/zones
- Clear "what to do next" for outreach + installs
- Hardware planning tied to venue pipeline

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
- [x] Ambassador Program trimmed to Parts 1-2 only (Commission Structure + Job Description)
- [x] Ambassador job posting formatted to match official Helium Foundation template
- [x] Job posting adapted for Washington D.C. (experience requirement: 1+ years or equivalent hustle)

### Venue Data Cleanup (Jan 2026)
- [x] Used Yelp API to check all 600 venues for permanent closures
- [x] Removed 20 permanently closed venues
- [x] Removed 44 duplicate venues (same name+address in both files)
- [x] New totals: dupont-leads.csv (290), 14thu-leads.csv (246), Total: 536 venues
- [x] Scripts saved for future re-verification:
  - `check_closed_venues.py` - Check venues against Yelp API
  - `clean_venue_lists.py` - Remove closed venues by ID
  - `venue_check_results.json` - Full results from Yelp check
  - `venue_cleanup_log.json` - Record of removals

---

## Technical Notes

### Data Files
- `dupont-leads.csv` - 290 Dupont venues (after cleanup)
- `14thu-leads.csv` - 246 14th St/U St venues (after cleanup)
- Total: 536 venues (originally 600, removed 20 closed + 44 duplicates)
- Both CSVs have columns: ID, Name, Address, Category, Pod, Indoor, Outdoor, Score, Corner, Lat, Lng

### Key Thresholds
- Priority venue: Score >= 85
- Outdoor viable: Outdoor viability score >= 4
- Min score in data: 52 (slider starts at 50)

### Libraries Used
- Docsify 4.x - Documentation framework
- Leaflet 1.9.4 - Mapping
- Leaflet.markercluster 1.4.1 - Marker clustering
- Carto Positron tiles - Basemap (free, no API key)

### Mobile Breakpoints
- 768px - Tablet/mobile transition
- 480px - Small mobile adjustments

### Pod/Zone Codes
```
D1 = Dupont - Connecticut Ave
D2 = Dupont - 17th St Strip
D3 = Dupont - Dupont Ring
D4 = Dupont - P St / 20th
U1 = 14th/U - 14th St Main
U2 = 14th/U - U St Corridor
U3 = 14th/U - Shaw / 9th St
U4 = 14th/U - V/W / Columbia Heights
```

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
