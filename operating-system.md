# DC Hyper-Density Operating System

> **Note:** This operating system focuses on the priority deployment corridors (Dupont Circle + 14th/U St). The full venue dataset now covers 18 DC neighborhoods with 2,743 venues — see [venue-lead-generation-system.md](venue-lead-generation-system.md). Neighborhood dropdowns can be expanded as operations scale beyond the initial corridors.

---

## 1. Spreadsheet Tabs + Columns + Dropdown Values

### Tab 1: `LEADS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| lead_id | Auto | — | Yes |
| business_name | Text | — | Yes |
| street_address | Text | — | Yes |
| neighborhood | Dropdown | `Dupont Circle`, `14th St + U St` | Yes |
| micro_zone | Dropdown | `D1-Connecticut Ave`, `D2-17th St`, `D3-Dupont Ring`, `D4-P St`, `U1-14th St Main`, `U2-U St Corridor`, `U3-13th St`, `U4-V/W Streets` | Yes |
| category | Dropdown | `Coffee Shop`, `Restaurant/Bar`, `Fitness/Gym`, `Salon/Barber`, `Co-working`, `Retail`, `Laundromat`, `Auto/Repair`, `Other` | Yes |
| category_tier | Dropdown | `Tier 1`, `Tier 2`, `Tier 3` | Yes |
| source | Dropdown | `Desk Research`, `Field Blitz`, `Email`, `IG DM`, `Phone`, `QR Pamphlet`, `Referral` | Yes |
| source_date | Date | — | Yes |
| dm_name | Text | — | No |
| dm_title | Dropdown | `Owner`, `Manager`, `Employee`, `Unknown` | No |
| dm_phone | Phone | — | No |
| dm_email | Email | — | No |
| contact_pref | Dropdown | `Phone`, `Text`, `Email`, `In-person` | No |
| indoor_candidate | Dropdown | `Yes`, `No`, `Maybe` | Yes |
| indoor_sqft | Dropdown | `<1000`, `1000-2500`, `2500-5000`, `5000+`, `Unknown` | No |
| indoor_units | Dropdown | `0`, `1`, `2`, `3`, `4+` | No |
| outdoor_candidate | Dropdown | `Yes`, `No`, `Maybe` | Yes |
| outdoor_mount | Dropdown | `Rooftop`, `Awning`, `Wall`, `Pole`, `None`, `TBD` | No |
| corner_lot | Dropdown | `Yes`, `No` | Yes |
| permission_complexity | Dropdown | `Simple`, `Moderate`, `Complex`, `Very Complex`, `Unknown` | No |
| landlord_needed | Dropdown | `Yes`, `No`, `Unknown` | No |
| indoor_score | Number | — | Formula |
| outdoor_score | Number | — | Formula |
| total_score | Number | — | Formula |
| priority_rank | Dropdown | `A`, `B`, `C`, `D` | Formula |
| pipeline_stage | Dropdown | `Raw Lead`, `Contacted`, `Qualified`, `Permissioned`, `Scheduled`, `Installed`, `Verified`, `Declined`, `Dead` | Yes |
| assigned_to | Dropdown | `Unassigned`, `SDR-1`, `SDR-2`, `Installer-1`, `Installer-2`, `Installer-3` | No |
| notes | Text | — | No |

---

### Tab 2: `OUTREACH_LOG`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| log_id | Auto | — | Yes |
| lead_id | Lookup | — | Yes |
| business_name | Lookup | — | Auto |
| date | Date | — | Yes |
| channel | Dropdown | `Phone`, `Text`, `Email`, `IG DM`, `In-person`, `QR Follow-up` | Yes |
| direction | Dropdown | `Outbound`, `Inbound` | Yes |
| outcome | Dropdown | `Reached DM`, `Left VM`, `No Answer`, `Replied - Interested`, `Replied - Not Interested`, `Replied - Callback`, `Bounced`, `Blocked` | Yes |
| next_action | Dropdown | `Call Again`, `Send Email`, `Send Text`, `Schedule Visit`, `Close as Dead`, `None` | Yes |
| next_action_date | Date | — | No |
| notes | Text | — | No |

---

### Tab 3: `SITE_VISITS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| visit_id | Auto | — | Yes |
| lead_id | Lookup | — | Yes |
| business_name | Lookup | — | Auto |
| visit_date | Date | — | Yes |
| visit_time | Time | — | Yes |
| assigned_installer | Dropdown | `Installer-1`, `Installer-2`, `Installer-3` | Yes |
| visit_status | Dropdown | `Scheduled`, `Confirmed`, `Completed`, `No-show`, `Rescheduled`, `Cancelled` | Yes |
| indoor_viable | Dropdown | `Yes`, `No` | No |
| outdoor_viable | Dropdown | `Yes`, `No` | No |
| install_same_day | Dropdown | `Yes`, `No`, `N/A` | No |
| install_scheduled_date | Date | — | No |
| notes | Text | — | No |

---

### Tab 4: `INSTALLS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| install_id | Auto | — | Yes |
| lead_id | Lookup | — | Yes |
| business_name | Lookup | — | Auto |
| micro_zone | Lookup | — | Auto |
| install_date | Date | — | Yes |
| installer | Dropdown | `Installer-1`, `Installer-2`, `Installer-3` | Yes |
| indoor_units | Number | — | Yes |
| outdoor_units | Number | — | Yes |
| device_ids | Text | — | Yes |
| photos_submitted | Dropdown | `Yes`, `No` | Yes |
| gps_verified | Dropdown | `Yes`, `No`, `Pending` | Yes |
| host_agreement_signed | Dropdown | `Yes`, `No` | Yes |
| install_status | Dropdown | `Completed`, `Partial`, `Failed`, `Pending QA` | Yes |
| verification_status | Dropdown | `Pending 72hr`, `Online`, `Offline`, `Verified`, `Failed` | Yes |
| host_callback_status | Dropdown | `Not Started`, `Attempted`, `Confirmed`, `Denied`, `No Answer` | Yes |
| commission_status | Dropdown | `Pending`, `Approved`, `Paid`, `Clawback` | Yes |
| ambassador_id | Text | — | No |
| notes | Text | — | No |

---

### Tab 5: `AMBASSADORS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| ambassador_id | Auto | — | Yes |
| name | Text | — | Yes |
| phone | Phone | — | Yes |
| email | Email | — | Yes |
| zones_assigned | Multi-select | `D1`, `D2`, `D3`, `D4`, `U1`, `U2`, `U3`, `U4` | Yes |
| status | Dropdown | `Active`, `Suspended`, `Banned`, `Inactive` | Yes |
| onboarding_complete | Dropdown | `Yes`, `No` | Yes |
| strikes | Dropdown | `0`, `1`, `2`, `3` | Yes |
| lifetime_installs | Number | — | Auto |
| lifetime_earnings | Currency | — | Auto |
| badge | Dropdown | `None`, `Bronze`, `Silver`, `Gold`, `Platinum`, `Diamond` | Auto |

---

### Tab 6: `COMMISSIONS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| commission_id | Auto | — | Yes |
| install_id | Lookup | — | Yes |
| ambassador_id | Lookup | — | Yes |
| business_name | Lookup | — | Auto |
| micro_zone | Lookup | — | Auto |
| install_type | Dropdown | `Indoor`, `Outdoor` | Yes |
| install_route | Dropdown | `Self-Install`, `Deployer Network` | Yes |
| base_commission | Currency | — | Yes |
| welcome_pack_cut | Currency | — | No |
| total_commission | Currency | — | Formula |
| status | Dropdown | `Pending Verification`, `Approved`, `Paid`, `Clawback` | Yes |
| payout_date | Date | — | No |

---

### Tab 7: `DAILY_METRICS`

| Column | Type | Dropdown Values | Required |
|--------|------|-----------------|----------|
| date | Date | — | Yes |
| raw_leads_added | Number | — | Yes |
| raw_leads_cumulative | Number | — | Formula |
| qualified_added | Number | — | Yes |
| qualified_cumulative | Number | — | Formula |
| permissioned_added | Number | — | Yes |
| permissioned_cumulative | Number | — | Formula |
| scheduled_added | Number | — | Yes |
| scheduled_cumulative | Number | — | Formula |
| installed_added | Number | — | Yes |
| installed_cumulative | Number | — | Formula |
| calls_made | Number | — | Yes |
| emails_sent | Number | — | Yes |
| dms_sent | Number | — | Yes |
| field_visits | Number | — | Yes |
| pamphlets_placed | Number | — | Yes |
| qr_scans | Number | — | Yes |

---

## 2. QR Intake Form Fields

### Copy/Paste for Typeform or Tally

| # | Field Label | Field Type | Required | Validation | Dropdown Options |
|---|-------------|------------|----------|------------|------------------|
| 1 | Business Name | Short Text | Yes | Min 2 chars | — |
| 2 | Business Address | Address | Yes | DC only | — |
| 3 | What type of business? | Dropdown | Yes | — | `Coffee Shop / Cafe`, `Restaurant / Bar`, `Fitness / Gym`, `Salon / Barbershop`, `Retail Store`, `Co-working / Office`, `Laundromat`, `Auto / Repair`, `Other` |
| 4 | Your Name | Short Text | Yes | Min 2 chars | — |
| 5 | Your Role | Dropdown | Yes | — | `Owner`, `Manager`, `Employee`, `Other` |
| 6 | Are you the decision-maker for equipment? | Yes/No | Yes | — | `Yes`, `No` |
| 7 | For exterior work, would you need landlord approval? | Dropdown | Yes | — | `No - I control the building`, `Yes - landlord needed`, `Not sure` |
| 8 | When could we schedule installation? | Dropdown | Yes | — | `This week`, `Next 2 weeks`, `This month`, `Not sure yet` |
| 9 | How big is your space? | Dropdown | Yes | — | `Small (<1,000 sq ft)`, `Medium (1,000-3,000 sq ft)`, `Large (3,000+ sq ft)` |
| 10 | Interested in outdoor unit too? | Dropdown | Yes | — | `Yes`, `No`, `Maybe` |
| 11 | Is your business on a corner? | Yes/No | Yes | — | `Yes`, `No` |
| 12 | Phone Number | Phone | Yes | US format | — |
| 13 | Email | Email | Yes | Valid email | — |
| 14 | Preferred contact method | Dropdown | Yes | — | `Call`, `Text`, `Email` |
| 15 | Best time to reach you | Dropdown | Yes | — | `Morning (9am-12pm)`, `Afternoon (12-5pm)`, `Evening (5-8pm)`, `Anytime` |
| 16 | Does your business have WiFi? | Dropdown | No | — | `Yes`, `No`, `Not sure` |
| 17 | Business hours | Short Text | No | — | — |
| 18 | How did you hear about this? | Dropdown | No | — | `Pamphlet`, `Someone visited`, `Instagram`, `Friend/referral`, `Other` |
| 19 | Anything else we should know? | Long Text | No | — | — |

### Hidden Fields (Auto-Populated)

| Field | Value |
|-------|-------|
| zone | From QR URL param (`?zone=dupont` or `?zone=14th-u`) |
| source_id | From QR URL param (`?src=QR-D1-001`) |
| submission_timestamp | Auto |

---

## 3. Ambassador Commission Tracking Table

### Weekly Commission Report Template

| Ambassador | Zone | Venue | Install Type | Route | Commission | Welcome Pack Cut | **Total** | Status |
|------------|------|-------|--------------|-------|------------|------------------|-----------|--------|
| @marcus_dc | D1 | Compass Coffee | Indoor | Self-Install | $75 | +$X | **$75+** | Pending |
| @marcus_dc | D1 | Kramerbooks | Indoor | Deployer | $75 | — | **$75** | Pending |
| @marcus_dc | D1 | Teaism | Outdoor | Self-Install | $50 | +$X | **$50+** | Pending |
| @sarah_14th | U1 | Busboys & Poets | Indoor | Deployer | $75 | — | **$75** | Approved |
| @sarah_14th | U2 | Nellie's | Outdoor | Deployer | $50 | — | **$50** | Approved |
| @jenna_dupont | D2 | JR's Bar | Indoor | Self-Install | $75 | +$X | **$75+** | Paid |

### Commission Calculation Quick Reference

| Install Type | Commission |
|--------------|------------|
| Indoor hotspot installed + verified | $75 |
| Outdoor hotspot installed + verified | $50 |

| Route | Additional Earnings |
|-------|---------------------|
| Self-Install (welcome pack) | 25% cut of welcome pack value |
| Route to Deployer Network | Standard commission only |

**Monthly base salary:** $3,000 (minimum 5 verified installs/month to qualify)

### Weekly Leaderboard Template

| Rank | Ambassador | Installs | Commission | Top Category |
|------|------------|----------|------------|--------------|
| 1 | @marcus_dc | 12 | $900 | Most Installs |
| 2 | @sarah_14th | 9 | $675 | Outdoor Champ |
| 3 | @jenna_dupont | 8 | $600 | Most Self-Installs |
| 4 | @tyrell_nw | 6 | $450 | Best Anchors |

---

## 4. Pod Map Spec for Google My Maps

### Map Setup

**Map Name:** `DC Hyper-Density Deployment — [Date]`

**Base Map Style:** `Silver` (muted colors, venues pop)

---

### Layer 1: `Zone Boundaries`

| Zone | Boundary Color | Fill Opacity | Boundary Coordinates |
|------|---------------|--------------|----------------------|
| D1-Connecticut Ave | Blue | 15% | N St NW & Connecticut → R St NW & Connecticut → R St & 18th → N St & 18th → close |
| D2-17th St | Green | 15% | P St & 17th → R St & 17th → R St & 18th → P St & 18th → close |
| D3-Dupont Ring | Purple | 15% | 200ft radius from Dupont Circle center (38.9096, -77.0434) |
| D4-P St | Orange | 15% | P St & 18th → P St & 21st → Q St & 21st → Q St & 18th → close |
| U1-14th St Main | Red | 15% | T St & 14th → W St & 14th → W St & 15th → T St & 15th → close |
| U2-U St Corridor | Yellow | 15% | U St & 13th → U St & 16th → V St & 16th → V St & 13th → close |
| U3-13th St | Cyan | 15% | T St & 13th → V St & 13th → V St & 14th → T St & 14th → close |
| U4-V/W Streets | Pink | 15% | V St & 13th → W St & 15th → W St & 13th → close |

---

### Layer 2: `Venues — By Pipeline Stage`

| Stage | Pin Color | Icon |
|-------|-----------|------|
| Raw Lead | Gray | Circle |
| Contacted | Light Blue | Circle |
| Qualified | Blue | Star |
| Permissioned | Green | Star |
| Scheduled | Yellow | Flag |
| Installed | Dark Green | Checkmark |
| Verified | Gold | Trophy |
| Declined | Red | X |

**Pin Data Fields:**
- Name: `{business_name}`
- Description: `Zone: {micro_zone} | Stage: {pipeline_stage} | Score: {total_score}`

---

### Layer 3: `Venues — By Priority`

| Priority | Pin Color | Icon |
|----------|-----------|------|
| A (80-100) | Green | Large dot |
| B (60-79) | Yellow | Medium dot |
| C (40-59) | Orange | Small dot |
| D (0-39) | Gray | Tiny dot |

---

### Layer 4: `Outdoor Coverage Nodes`

| Node Type | Pin Color | Icon |
|-----------|-----------|------|
| Anchor Node (planned) | Blue | Antenna |
| Anchor Node (installed) | Green | Antenna |
| Fill Node (planned) | Light Blue | Small antenna |
| Fill Node (installed) | Light Green | Small antenna |

**Pin Data Fields:**
- Name: `Outdoor @ {business_name}`
- Description: `Height: {outdoor_height} | Sightline: {outdoor_sightline} | Status: {install_status}`

---

### Layer 5: `Daily Routes`

| Route | Line Color | Style |
|-------|-----------|-------|
| Dupont AM Route | Blue | Dashed |
| Dupont PM Route | Blue | Solid |
| 14th/U AM Route | Red | Dashed |
| 14th/U PM Route | Red | Solid |

---

### Pin Import Format (CSV)

```csv
name,address,lat,lng,zone,stage,priority,score,category,outdoor_candidate
Compass Coffee,1535 Connecticut Ave NW,38.9106,-77.0434,D1,Qualified,A,91,Coffee Shop,Yes
Kramerbooks,1517 Connecticut Ave NW,38.9102,-77.0432,D1,Permissioned,A,85,Retail,Yes
JR's Bar,1519 17th St NW,38.9115,-77.0385,D2,Scheduled,B,72,Bar,Yes
```

---

## 5. Day 1 Checklist with Numeric Targets

### Day 1: Desk Research Blitz

**Date:** _______________
**Team:** 2 researchers + 1 QA

---

#### Pre-Work (Before 8am)

| Task | Owner | Done |
|------|-------|------|
| Create master Google Sheet with all tabs | TM1 | ☐ |
| Set up Outscraper account ($40 budget) | TM1 | ☐ |
| Create Google My Maps with zone boundaries | TM2 | ☐ |
| Test QR form submission flow | TM3 | ☐ |
| Confirm team Slack channel | TM1 | ☐ |

---

#### Morning Block (8am - 12pm)

| Time | Task | Target | Actual | Owner |
|------|------|--------|--------|-------|
| 8:00-9:00 | Setup + test Outscraper | Ready | ☐ | TM1 |
| 9:00-10:00 | Pull Tier 1 categories - Dupont | 40 leads | ___ | TM1 |
| 9:00-10:00 | Pull Tier 1 categories - 14th/U | 50 leads | ___ | TM2 |
| 10:00-11:00 | Pull Tier 2 categories - Dupont | 30 leads | ___ | TM1 |
| 10:00-11:00 | Pull Tier 2 categories - 14th/U | 40 leads | ___ | TM2 |
| 11:00-12:00 | Dedupe + address cleanup | Clean data | ☐ | TM3 |

**Morning Target: 160 raw leads**

---

#### Lunch (12pm - 1pm)

| Task | Owner | Done |
|------|-------|------|
| Data backup to cloud | TM3 | ☐ |
| Quick team sync (15 min) | All | ☐ |
| Review morning blockers | All | ☐ |

---

#### Afternoon Block (1pm - 5pm)

| Time | Task | Target | Actual | Owner |
|------|------|--------|--------|-------|
| 1:00-2:00 | Google Maps gap fill - Dupont | 20 leads | ___ | TM1 |
| 1:00-2:00 | Google Maps gap fill - 14th/U | 20 leads | ___ | TM2 |
| 2:00-3:00 | Tier 3 categories - both zones | 30 leads | ___ | TM1+TM2 |
| 3:00-4:00 | Instagram handle lookup (50/hr) | 50 handles | ___ | TM1 |
| 3:00-4:00 | Instagram handle lookup (50/hr) | 50 handles | ___ | TM2 |
| 4:00-5:00 | Apply category + zone scoring | All scored | ☐ | TM3 |

**Afternoon Target: 70 leads + 100 IG handles**

---

#### End of Day (5pm - 6:30pm)

| Time | Task | Target | Actual | Owner |
|------|------|--------|--------|-------|
| 5:00-5:30 | Final data cleanup | 0 errors | ☐ | TM3 |
| 5:30-6:00 | Assign priority ranks (A/B/C/D) | All ranked | ☐ | TM3 |
| 6:00-6:30 | Day 1 standup + Day 2 planning | Complete | ☐ | All |

---

#### Day 1 Scorecard

| Metric | Target | Actual | Hit? |
|--------|--------|--------|------|
| Raw leads captured | 200 | ___ | ☐ |
| Dupont Circle leads | 90 | ___ | ☐ |
| 14th/U St leads | 110 | ___ | ☐ |
| Tier 1 venues | 60 | ___ | ☐ |
| Tier 2 venues | 80 | ___ | ☐ |
| Tier 3 venues | 60 | ___ | ☐ |
| IG handles found | 100 | ___ | ☐ |
| All leads scored | Yes | ___ | ☐ |
| Data errors | 0 | ___ | ☐ |

---

#### Day 1 Zone Breakdown

| Zone | Target | Actual |
|------|--------|--------|
| D1-Connecticut Ave | 40 | ___ |
| D2-17th St | 25 | ___ |
| D3-Dupont Ring | 15 | ___ |
| D4-P St | 10 | ___ |
| U1-14th St Main | 50 | ___ |
| U2-U St Corridor | 35 | ___ |
| U3-13th St | 15 | ___ |
| U4-V/W Streets | 10 | ___ |
| **TOTAL** | **200** | ___ |

---

#### Day 1 Blockers Log

| Blocker | Impact | Resolution |
|---------|--------|------------|
| | | |
| | | |
| | | |

---

#### Day 2 Prep (Before Leaving)

| Task | Owner | Done |
|------|-------|------|
| Export top 50 leads for email outreach | TM1 | ☐ |
| Export top 50 IG handles for DM outreach | TM2 | ☐ |
| Draft email sequence loaded in Lemlist | TM1 | ☐ |
| IG DM templates ready | TM2 | ☐ |
| Day 2 call list prioritized | TM3 | ☐ |
