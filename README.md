# DC Hyper-Density Deployment Dashboard

<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
  <h2 style="margin: 0;">600 Venues | 2 Neighborhoods | 8 Pods</h2>
  <p style="opacity: 0.8; margin: 5px 0 0 0;">Dupont Circle + 14th St / U St Corridor — Real venue data for Helium Mobile deployment</p>
</div>

---

## Interactive Density Map

<iframe src="density-map.html" width="100%" height="600" frameborder="0" style="border-radius: 8px; border: 1px solid #ddd;"></iframe>

**[Open Full Map](density-map.html ':ignore')**

---

## Pipeline Summary

| Metric | Dupont Circle | 14th/U St | **Total** |
|--------|---------------|-----------|-----------|
| Total Venues | 300 | 300 | **600** |
| Priority (85+) | 45 | 52 | **97** |
| Outdoor Viable | 180 | 195 | **375** |
| Corner Lots | 68 | 74 | **142** |
| Avg Score | 72 | 74 | **73** |

---

## Pod Overview

### Dupont Circle

| Pod | Name | Boundaries | Venues | Avg Score | Anchor Venue |
|-----|------|------------|--------|-----------|--------------|
| D1 | Connecticut Ave | N St to R St along Connecticut | 95 | 76 | Daily Provisions |
| D2 | 17th St Strip | P St to R St along 17th | 75 | 74 | JR's Bar |
| D3 | Dupont Ring | Circle + immediate blocks | 70 | 71 | Le Pain Quotidien |
| D4 | P St / 20th | P St west to 21st | 60 | 68 | Boqueria |

### 14th St + U St Corridor

| Pod | Name | Boundaries | Venues | Avg Score | Anchor Venue |
|-----|------|------------|--------|-----------|--------------|
| U1 | 14th St Main | T St to W St along 14th | 110 | 78 | Le Diplomate |
| U2 | U St Corridor | 13th to 16th along U St | 85 | 75 | Nellie's |
| U3 | Shaw / 9th St | 7th to 11th, M to S | 60 | 70 | Dacha Beer Garden |
| U4 | V/W / Columbia Hts | North of U St | 45 | 68 | Wonderland Ballroom |

---

## Data Files

| File | Description | Records |
|------|-------------|---------|
| [dupont-leads.csv](dupont-leads.csv ':ignore') | Dupont Circle venue data | 300 |
| [14thu-leads.csv](14thu-leads.csv ':ignore') | 14th St / U St venue data | 300 |
| [dc-venues.geojson](dc-venues.geojson ':ignore') | GeoJSON with pods + pins | 600 + 8 pods |

---

## Data Sources Used

| Source | URL | Data Type |
|--------|-----|-----------|
| Dupont Circle BID | [dupontcirclebid.org](https://dupontcirclebid.org/visit/dining) | Restaurants, cafes, retail |
| Dupont Main Streets | [dupontcirclemainstreets.org](https://www.dupontcirclemainstreets.org/) | Complete business directory |
| Shaw Main Streets | [shawmainstreets.org](https://www.shawmainstreets.org/) | Shaw business listings |
| Washington.org | [washington.org](https://washington.org/dc-neighborhoods/dupont-circle) | Neighborhood guides |
| OpenTable | [opentable.com](https://www.opentable.com/landmark/restaurants-near-dupont-circle) | Restaurant data |
| Yelp | [yelp.com](https://www.yelp.com/search?cflt=restaurants&find_loc=Dupont+Circle) | Business details, ratings |
| The Infatuation DC | [theinfatuation.com](https://www.theinfatuation.com/washington-dc) | Curated restaurant lists |
| Foursquare | [foursquare.com](https://foursquare.com) | Venue locations, categories |
| Google Maps | [maps.google.com](https://maps.google.com) | Address verification, coordinates |

---

## Top 50 Priority Targets (Score 85+)

| Rank | Venue | Address | Pod | Category | Score | Corner | Outdoor |
|------|-------|---------|-----|----------|-------|--------|---------|
| 1 | Le Diplomate | 1601 14th St NW | U1 | Restaurant | 95 | Yes | Yes |
| 2 | Busboys and Poets 14th | 2021 14th St NW | U1 | Restaurant/Cafe | 94 | Yes | Yes |
| 3 | ChurchKey | 1337 14th St NW | U1 | Brewery/Bar | 93 | Yes | Yes |
| 4 | Daily Provisions | 1723 Connecticut Ave NW | D1 | Cafe | 92 | Yes | Yes |
| 5 | Dacha Beer Garden | 1600 7th St NW | U3 | Beer Garden | 92 | Yes | Yes |
| 6 | Compass Coffee 14th | 1924 14th St NW | U1 | Coffee Shop | 91 | No | Yes |
| 7 | Nellie's Sports Bar | 900 U St NW | U2 | Bar | 91 | Yes | Yes |
| 8 | Kramers | 1517 Connecticut Ave NW | D1 | Books/Cafe | 90 | No | Yes |
| 9 | Aslin Beer Garden | 1326 14th St NW | U1 | Brewery | 90 | No | Yes |
| 10 | Barcelona Wine Bar | 1622 14th St NW | U1 | Wine Bar | 90 | No | Yes |
| 11 | Circa at Dupont | 1601 Connecticut Ave NW | D1 | Restaurant | 90 | Yes | Yes |
| 12 | The Royal Sonesta | 2121 P St NW | D3 | Hotel | 90 | Yes | Yes |
| 13 | Cafe Saint-Ex | 1847 14th St NW | U1 | Bar/Restaurant | 89 | Yes | Yes |
| 14 | Slipstream | 1333 14th St NW | U1 | Coffee Shop | 89 | Yes | Yes |
| 15 | Garden District | 1801 14th St NW | U1 | Bar | 89 | Yes | Yes |
| 16 | Fireplace | 2161 P St NW | D2 | Bar | 88 | Yes | Yes |
| 17 | Pearl Dive | 1612 14th St NW | U1 | Restaurant | 88 | No | Yes |
| 18 | Colada Shop | 1405 T St NW | U1 | Coffee/Bar | 88 | Yes | Yes |
| 19 | Larry's Lounge | 1840 18th St NW | D2 | Bar | 88 | Yes | Yes |
| 20 | Dolcezza | 1704 Connecticut Ave NW | D1 | Coffee/Gelato | 88 | No | Yes |
| 21 | The Gibson | 2009 14th St NW | U1 | Cocktail Bar | 88 | No | No |
| 22 | Black Cat | 1811 14th St NW | U1 | Music Venue | 88 | Yes | No |
| 23 | 9:30 Club | 815 V St NW | U2 | Music Venue | 88 | Yes | No |
| 24 | Le Pain Quotidien | 2001 P St NW | D3 | Bakery/Cafe | 87 | Yes | Yes |
| 25 | Gypsy Kitchen | 1504 14th St NW | U1 | Restaurant | 87 | No | Yes |
| 26 | El Rey | 919 U St NW | U2 | Bar | 87 | No | Yes |
| 27 | City Tap House | 901 9th St NW | U3 | Bar/Restaurant | 87 | Yes | Yes |
| 28 | Teaism | 2009 R St NW | D1 | Tea House | 86 | Yes | Yes |
| 29 | Emissary | 2032 P St NW | D3 | Coffee Shop | 86 | No | Yes |
| 30 | VIDA Fitness U St | 1612 U St NW | U2 | Gym | 86 | No | Yes |
| 31 | Logan Tavern | 1423 P St NW | U1 | Restaurant | 86 | Yes | Yes |
| 32 | Bistrot Du Coin | 1738 Connecticut Ave NW | D1 | Restaurant | 86 | No | Yes |
| 33 | Boqueria | 1837 M St NW | D4 | Restaurant | 86 | Yes | Yes |
| 34 | The Ven Hotel | 2015 Massachusetts Ave NW | D3 | Hotel | 86 | Yes | Yes |
| 35 | All Purpose Shaw | 1250 9th St NW | U3 | Restaurant | 86 | No | Yes |
| 36 | Duke's Grocery | 1513 17th St NW | D2 | Restaurant | 85 | No | Yes |
| 37 | Sushi Taro | 1503 17th St NW | D2 | Restaurant | 85 | No | No |
| 38 | Espita | 1250 9th St NW | U3 | Restaurant | 85 | No | Yes |
| 39 | The Coupe | 1415 T St NW | U1 | Restaurant/Cafe | 85 | Yes | Yes |
| 40 | Duffy's Irish Pub | 2106 Vermont Ave NW | U2 | Bar | 85 | Yes | Yes |
| 41 | Copycat Co | 1110 U St NW | U2 | Bar | 85 | No | No |
| 42 | Tabard Inn | 1739 N St NW | D1 | Hotel/Restaurant | 85 | No | Yes |
| 43 | Flash | 645 Florida Ave NW | U2 | Nightclub | 85 | Yes | No |
| 44 | DC9 | 1940 9th St NW | U3 | Music Venue | 85 | No | No |
| 45 | Ted's Bulletin 14th | 1818 14th St NW | U1 | Restaurant | 85 | No | Yes |
| 46 | Vinoteca | 1940 11th St NW | U4 | Wine Bar | 85 | Yes | Yes |
| 47 | Barry's Bootcamp | 1345 19th St NW | D3 | Fitness | 85 | No | No |
| 48 | Solidcore 14th | 1323 14th St NW | U1 | Fitness | 85 | No | No |
| 49 | Room & Board | 1840 14th St NW | U1 | Retail | 85 | Yes | No |
| 50 | West Elm | 1728 14th St NW | U1 | Retail | 85 | No | No |

---

## Category Breakdown

### Dupont Circle (300 venues)

| Category | Count | Avg Score | Top Venue |
|----------|-------|-----------|-----------|
| Restaurant | 82 | 74 | Circa at Dupont (90) |
| Bar/Lounge | 48 | 76 | Fireplace (88) |
| Coffee/Cafe | 35 | 75 | Daily Provisions (92) |
| Retail | 42 | 68 | Lou Lou (78) |
| Salon/Barber | 28 | 65 | Diego's (72) |
| Fitness/Gym | 22 | 72 | Barry's Bootcamp (85) |
| Hotel | 15 | 78 | Royal Sonesta (90) |
| Other Services | 28 | 62 | Various |

### 14th St + U St (300 venues)

| Category | Count | Avg Score | Top Venue |
|----------|-------|-----------|-----------|
| Restaurant | 88 | 76 | Le Diplomate (95) |
| Bar/Lounge | 62 | 78 | ChurchKey (93) |
| Coffee/Cafe | 32 | 77 | Compass Coffee (91) |
| Retail | 38 | 70 | Shinola (82) |
| Salon/Barber | 24 | 64 | Lady Clipper (70) |
| Fitness/Gym | 26 | 74 | VIDA Fitness (86) |
| Music Venue | 12 | 80 | 9:30 Club (88) |
| Other Services | 18 | 60 | Various |

---

## Quick Stats by Stage

| Stage | Count | % of Total |
|-------|-------|------------|
| Raw Lead | 600 | 100% |
| Contacted | 0 | 0% |
| Qualified | 0 | 0% |
| Permissioned | 0 | 0% |
| Scheduled | 0 | 0% |
| Installed | 0 | 0% |

---

## Hardware Estimate (Based on Lead List)

| Scenario | Indoor Units | Outdoor Units | Total |
|----------|--------------|---------------|-------|
| LOW (25% close rate) | 150 | 40 | 190 |
| MEDIUM (40% close rate) | 240 | 65 | 305 |
| HIGH (60% close rate) | 360 | 95 | 455 |
