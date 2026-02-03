# DC Venue Lead List — Spreadsheet Schema

## Schema Overview

**Total columns:** 42
**Sections:**
1. Venue Identity (8 cols)
2. Location & Zone (6 cols)
3. Indoor Placement (7 cols)
4. Outdoor Placement (7 cols)
5. Decision-Maker & Permissioning (8 cols)
6. Scoring (4 cols)
7. Pipeline & Routing (2 cols)

---

## Section 1: Venue Identity

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 1 | `lead_id` | Auto-generated (DC-DUP-0001, DC-14U-0001) | Unique ID. Prefix = neighborhood (DUP = Dupont, 14U = 14th/U St) | DC-DUP-0147 |
| 2 | `business_name` | Free text | Legal or DBA name as shown on signage | Compass Coffee |
| 3 | `category_tier` | Tier 1, Tier 2, Tier 3 | Priority tier per venue category ranking | Tier 1 |
| 4 | `category` | Coffee Shop, Co-working, Brewery/Taproom, Fitness Studio, Barber/Salon, Fast-Casual, Boutique Retail, Wine/Cocktail Bar, Laundromat, Tech/Phone Repair, Dry Cleaner, Bodega/Convenience, Nail Salon, Auto Shop, Church/Community, Restaurant (Full Service), Other | Primary business type | Coffee Shop |
| 5 | `source` | Desk Research, On-Foot Blitz, IG Outreach, Email Outreach, Phone Outreach, Referral, QR Pamphlet, Inbound | How lead was captured | On-Foot Blitz |
| 6 | `source_date` | Date (YYYY-MM-DD) | Date lead was first captured | 2025-02-03 |
| 7 | `website` | URL or blank | Business website if known | compasscoffee.com |
| 8 | `instagram` | @handle or blank | Instagram handle | @compasscoffee |

---

## Section 2: Location & Zone

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 9 | `neighborhood` | Dupont Circle, 14th St + U St | Target neighborhood | Dupont Circle |
| 10 | `micro_zone` | D1-Connecticut Ave, D2-17th St, D3-P St, D4-Dupont Ring, U1-14th St Main, U2-U St Corridor, U3-13th St, U4-V/W Side Streets | Specific zone within neighborhood | D1-Connecticut Ave |
| 11 | `street_address` | Free text | Full street address | 1535 Connecticut Ave NW |
| 12 | `cross_street` | Free text | Nearest cross street for routing | Q St NW |
| 13 | `lat` | Decimal (-90 to 90) | Latitude for mapping | 38.9106 |
| 14 | `lng` | Decimal (-180 to 180) | Longitude for mapping | -77.0434 |

---

## Section 3: Indoor Placement

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 15 | `indoor_candidate` | Yes, No, Maybe | Is this venue viable for indoor hotspot? | Yes |
| 16 | `indoor_sqft` | <1000, 1000-2500, 2500-5000, 5000+, Unknown | Estimated interior square footage | 1000-2500 |
| 17 | `indoor_units_needed` | 0, 1, 2, 3, 4+ | Number of indoor units required for coverage | 1 |
| 18 | `indoor_power_access` | Easy (outlet near window), Moderate (outlet within 15ft), Difficult (no visible outlet), Unknown | Power availability for indoor unit | Easy (outlet near window) |
| 19 | `indoor_mount_location` | Window sill, Counter/shelf, Wall mount, Ceiling, Other, TBD | Where indoor unit would be placed | Window sill |
| 20 | `indoor_wifi_available` | Yes - venue WiFi, Yes - owner hotspot, No - needs cellular backhaul, Unknown | Internet connectivity for indoor unit | Yes - venue WiFi |
| 21 | `indoor_notes` | Free text | Any special notes about indoor placement | Front window has ledge, outlet 3ft away |

---

## Section 4: Outdoor Placement

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 22 | `outdoor_candidate` | Yes, No, Maybe | Is this venue viable for outdoor hotspot? | Yes |
| 23 | `outdoor_mount_type` | Rooftop, Awning/Overhang, Exterior Wall, Pole/Post, Balcony, None Viable, TBD | Best outdoor mounting option | Awning/Overhang |
| 24 | `outdoor_height_ft` | Ground (<10ft), Low (10-20ft), Medium (20-40ft), High (40ft+), Unknown | Estimated mount height | Low (10-20ft) |
| 25 | `outdoor_sightline` | Excellent (clear 360°), Good (clear 180°+), Partial (obstructed), Poor (blocked), Unknown | Line-of-sight quality from mount point | Good (clear 180°+) |
| 26 | `outdoor_power_access` | Easy (exterior outlet), Moderate (run from interior), Difficult (no access), Unknown | Power availability for outdoor unit | Moderate (run from interior) |
| 27 | `outdoor_corner_lot` | Yes, No | Is venue on a corner? (Higher coverage value) | Yes |
| 28 | `outdoor_notes` | Free text | Any special notes about outdoor placement | Awning over sidewalk seating, landlord may need approval |

---

## Section 5: Decision-Maker & Permissioning

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 29 | `dm_name` | Free text | Decision-maker name (owner, manager, etc.) | Sarah Chen |
| 30 | `dm_title` | Owner, Co-owner, General Manager, Manager, Franchisee, Employee (no authority), Unknown | Decision-maker's role | Owner |
| 31 | `dm_phone` | Phone number | Best phone number for DM | 202-555-1234 |
| 32 | `dm_email` | Email | Best email for DM | sarah@compasscoffee.com |
| 33 | `dm_contact_pref` | Phone, Email, Text, Instagram DM, In-person only, Unknown | Preferred contact method | Text |
| 34 | `permission_complexity` | Simple (owner decides), Moderate (manager + owner), Complex (landlord involved), Very Complex (corporate/franchise), Unknown | How many approvals needed to install | Simple (owner decides) |
| 35 | `landlord_approval_needed` | Yes, No, Unknown | Does landlord need to approve exterior work? | No |
| 36 | `permission_notes` | Free text | Any notes on permissioning challenges | Owner is on-site M-F mornings, makes all decisions |

---

## Section 6: Scoring

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 37 | `indoor_score` | 0-50 (integer) | Indoor viability score (see rubric below) | 42 |
| 38 | `outdoor_score` | 0-50 (integer) | Outdoor viability score (see rubric below) | 38 |
| 39 | `total_score` | 0-100 (formula: indoor_score + outdoor_score) | Combined score for prioritization | 80 |
| 40 | `priority_rank` | A (80-100), B (60-79), C (40-59), D (0-39) | Auto-calculated priority tier | A |

---

## Section 7: Pipeline & Routing

| # | Column Name | Allowed Values | Definition | Example |
|---|-------------|----------------|------------|---------|
| 41 | `pipeline_stage` | Raw Lead, Contacted, Qualified, Permissioned, Scheduled, Installed, Verified, Declined, Dead | Current stage in pipeline | Qualified |
| 42 | `assigned_installer` | Unassigned, [Installer Name 1], [Installer Name 2], etc. | Which installer/ambassador is assigned | Unassigned |

---

## Scoring Rubrics

> **Note:** This schema uses a **post-contact qualification scoring** system (Indoor + Outdoor = 0-100) that differs from the **lead generation scoring** in [venue-scoring-rubric.md](venue-scoring-rubric.md).
> - **Lead generation score** (venue-scoring-rubric.md): Used by scrapers to prioritize initial outreach based on API-observable data
> - **Qualification score** (this schema): Used after contact to score venues based on verified placement viability

### Indoor Score (0-50 points)

| Factor | Points | Scoring Logic |
|--------|--------|---------------|
| **Category Tier** | 0-10 | Tier 1 = 10, Tier 2 = 6, Tier 3 = 3 |
| **Square Footage** | 0-10 | <1000 = 10, 1000-2500 = 8, 2500-5000 = 5, 5000+ = 3 |
| **Power Access** | 0-10 | Easy = 10, Moderate = 6, Difficult = 2, Unknown = 4 |
| **WiFi Available** | 0-10 | Yes (venue) = 10, Yes (hotspot) = 7, No = 3, Unknown = 5 |
| **Permission Complexity** | 0-10 | Simple = 10, Moderate = 7, Complex = 4, Very Complex = 2 |

**Formula:** `indoor_score = category_tier_pts + sqft_pts + power_pts + wifi_pts + permission_pts`

---

### Outdoor Score (0-50 points)

| Factor | Points | Scoring Logic |
|--------|--------|---------------|
| **Mount Type Viability** | 0-10 | Rooftop = 10, Awning = 8, Wall = 7, Pole = 6, Balcony = 5, None = 0 |
| **Sightline Quality** | 0-15 | Excellent = 15, Good = 11, Partial = 6, Poor = 2, Unknown = 5 |
| **Corner Lot** | 0-10 | Yes = 10, No = 3 |
| **Power Access** | 0-10 | Easy = 10, Moderate = 6, Difficult = 2, Unknown = 4 |
| **Landlord Approval** | 0-5 | No = 5, Unknown = 3, Yes = 1 |

**Formula:** `outdoor_score = mount_pts + sightline_pts + corner_pts + power_pts + landlord_pts`

---

### Priority Rank Calculation

| Total Score | Rank | Action |
|-------------|------|--------|
| 80-100 | A | Priority install — route to installer immediately |
| 60-79 | B | Strong candidate — schedule within 1 week |
| 40-59 | C | Viable — schedule within 2 weeks |
| 0-39 | D | Low priority — revisit only if capacity allows |

---

## Example Row (Full)

| Column | Value |
|--------|-------|
| lead_id | DC-DUP-0147 |
| business_name | Compass Coffee |
| category_tier | Tier 1 |
| category | Coffee Shop |
| source | On-Foot Blitz |
| source_date | 2025-02-03 |
| website | compasscoffee.com |
| instagram | @compasscoffee |
| neighborhood | Dupont Circle |
| micro_zone | D1-Connecticut Ave |
| street_address | 1535 Connecticut Ave NW |
| cross_street | Q St NW |
| lat | 38.9106 |
| lng | -77.0434 |
| indoor_candidate | Yes |
| indoor_sqft | 1000-2500 |
| indoor_units_needed | 1 |
| indoor_power_access | Easy (outlet near window) |
| indoor_mount_location | Window sill |
| indoor_wifi_available | Yes - venue WiFi |
| indoor_notes | Front window has ledge, outlet 3ft away |
| outdoor_candidate | Yes |
| outdoor_mount_type | Awning/Overhang |
| outdoor_height_ft | Low (10-20ft) |
| outdoor_sightline | Good (clear 180°+) |
| outdoor_power_access | Moderate (run from interior) |
| outdoor_corner_lot | Yes |
| outdoor_notes | Awning over sidewalk seating, landlord may need approval |
| dm_name | Sarah Chen |
| dm_title | Owner |
| dm_phone | 202-555-1234 |
| dm_email | sarah@compasscoffee.com |
| dm_contact_pref | Text |
| permission_complexity | Simple (owner decides) |
| landlord_approval_needed | No |
| permission_notes | Owner is on-site M-F mornings, makes all decisions |
| indoor_score | 42 |
| outdoor_score | 38 |
| total_score | 80 |
| priority_rank | A |
| pipeline_stage | Qualified |
| assigned_installer | Unassigned |

---

## Google Sheets Implementation Notes

### Dropdowns
Create data validation dropdowns for all columns with predefined allowed values (columns 3, 4, 5, 9, 10, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 30, 33, 34, 35, 40, 41, 42).

### Formulas

**Column 39 (total_score):**
```
=IF(AND(ISNUMBER(indoor_score), ISNUMBER(outdoor_score)), indoor_score + outdoor_score, "")
```

**Column 40 (priority_rank):**
```
=IF(total_score>=80,"A",IF(total_score>=60,"B",IF(total_score>=40,"C","D")))
```

**Column 1 (lead_id) — auto-generate:**
```
=IF(neighborhood="Dupont Circle","DC-DUP-"&TEXT(ROW()-1,"0000"),"DC-14U-"&TEXT(ROW()-1,"0000"))
```

### Conditional Formatting
- **Green (rows):** priority_rank = A
- **Yellow (rows):** priority_rank = B
- **Orange (rows):** priority_rank = C
- **Red (rows):** priority_rank = D
- **Bold:** pipeline_stage = "Scheduled" or "Installed"

### Filters to Create
1. By neighborhood
2. By micro_zone
3. By pipeline_stage
4. By priority_rank
5. By assigned_installer
6. By outdoor_candidate = "Yes" (for outdoor routing)
7. By permission_complexity (to identify easy wins)

---

## Quick Copy: Column Headers

```
lead_id,business_name,category_tier,category,source,source_date,website,instagram,neighborhood,micro_zone,street_address,cross_street,lat,lng,indoor_candidate,indoor_sqft,indoor_units_needed,indoor_power_access,indoor_mount_location,indoor_wifi_available,indoor_notes,outdoor_candidate,outdoor_mount_type,outdoor_height_ft,outdoor_sightline,outdoor_power_access,outdoor_corner_lot,outdoor_notes,dm_name,dm_title,dm_phone,dm_email,dm_contact_pref,permission_complexity,landlord_approval_needed,permission_notes,indoor_score,outdoor_score,total_score,priority_rank,pipeline_stage,assigned_installer
```
