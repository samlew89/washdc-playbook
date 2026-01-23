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

### Overview Page
- [x] Added Summary & Goals section with executive summary
- [x] Added Network BU Plan (4 pillars)
- [x] Added KPIs section
- [x] Removed Quick Links (redundant with sidebar)

### Lead List & Pipeline Page
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

---

## Technical Notes

### Data Files
- `dupont-leads.csv` - 300 Dupont venues
- `14thu-leads.csv` - 300 14th St/U St venues
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
- [ ] Mobile-responsive venue list improvements
- [ ] Integration with deployment tracking system

---

## Running Locally
```bash
cd /Users/samuellewis/Projects/WashDC
python3 -m http.server 8000
# Open http://localhost:8000
```
