# Hyper-Density Venue Scoring Rubric (0-100)

## Design Principles

This rubric is optimized for **outdoor coverage density**, not just indoor installs. We prioritize venues that:
1. Allow outdoor mounts on the same building
2. Can be closed and installed FAST (simple permissioning)
3. Sit at high-value locations (corners, intersections, sight lines)
4. Have reliable power/backhaul and accessible hours

---

## Scoring Categories Overview

| Category | Max Points | Weight | Confidence | Why |
|----------|------------|--------|------------|-----|
| **Outdoor Mounting Viability** | 35 | 35% | High | Core to density strategy; observable via Street View |
| **Permissioning Speed** | 15 | 15% | Low | Fast closes matter, but mostly inferred from business type |
| **Location & Line-of-Sight** | 25 | 25% | High | Coverage reach per unit; observable via maps |
| **Foot Traffic & Dwell Time** | 15 | 15% | Medium | Network utilization; inferred from reviews/category |
| **Operational Reliability** | 10 | 10% | Medium | Long-term uptime; partially observable |
| **TOTAL** | **100** | 100% | | |

---

## Category 1: Outdoor Mounting Viability (35 points)

*Can we mount an outdoor unit on or immediately adjacent to this building?*

**Data source:** Google Street View, Yelp/Google photos, satellite imagery. **Confidence: High.**

| Factor | Points | Scoring |
|--------|--------|---------|
| **Outdoor mount possible on same building** | 0-14 | |
| | 14 | Yes - rooftop, awning, or exterior wall clearly viable |
| | 9 | Probably - needs site visit to confirm |
| | 4 | Maybe - significant obstacles but possible |
| | 0 | No - no viable mount point visible |
| **Adjacent building mount option** | 0-7 | |
| | 7 | Adjacent building also in our pipeline (combo install) |
| | 4 | Adjacent building looks viable but not yet contacted |
| | 0 | No adjacent option / not applicable |
| **Mount height advantage** | 0-7 | |
| | 7 | 20ft+ elevation possible (rooftop, 2nd floor wall) |
| | 5 | 10-20ft elevation (awning, high wall mount) |
| | 2 | Ground level only (<10ft) |
| | 0 | Below grade or obstructed |
| **Owner controls exterior** | 0-7 | |
| | 7 | Owner owns building or has full exterior rights (signage matches business) |
| | 4 | Likely standard lease (street-level retail, typical setup) |
| | 1 | Multi-tenant building or landlord approval likely required |
| | 0 | Large commercial building, historic district, or complex ownership |

**Category 1 Total: /35**

---

## Category 2: Permissioning Speed (15 points)

*How fast can we go from "yes" to hardware on the wall?*

**Note:** These factors are **inferred from observable signals** (business type, ownership structure). This category has lower weight because confidence is low until actual contact. **Confidence: Low.**

| Factor | Points | Scoring |
|--------|--------|---------|
| **Decision-maker accessibility (inferred)** | 0-6 | |
| | 6 | Independent + owner-operated category (coffee, barber, brewery) + single location |
| | 5 | Independent + reviews/social mention owner by name or "family-run" |
| | 4 | Independent + typical owner-operated category |
| | 3 | Independent + larger venue (restaurant/bar likely has manager layer) |
| | 2 | Local chain (2-5 locations) OR unknown/can't determine |
| | 1 | Franchise (single owner-operator, e.g., subway franchisee) |
| | 0 | National chain (corporate-managed location) |
| **Approval layers (inferred)** | 0-5 | |
| | 5 | Owner-operated + likely owns building (signage matches business) |
| | 4 | Owner-operated + likely standard lease (street-level retail) |
| | 2 | Independent but multi-tenant building (landlord approval likely) |
| | 1 | Chain or franchise (corporate + landlord layers) |
| | 0 | Large commercial building, BID area, or historic district |
| **Prior tech/telecom installs (observable)** | 0-4 | |
| | 4 | Visible antennas, exterior cameras, digital signage on building |
| | 2 | Modern POS visible, digital menus, tech-forward appearance |
| | 1 | Standard setup, no visible tech resistance |
| | 0 | Explicitly "no tech" aesthetic or anti-corporate messaging |

**Inference sources:** Business name, Yelp/Google category, single vs multi-location, review text mentioning owner, Street View for building ownership indicators.

**Category 2 Total: /15**

---

## Category 3: Location & Line-of-Sight (25 points)

*How much coverage can we achieve from this location?*

**Data source:** Google Maps, satellite imagery, Street View. **Confidence: High.**

| Factor | Points | Scoring |
|--------|--------|---------|
| **Corner lot / intersection position** | 0-10 | |
| | 10 | Corner lot at major intersection |
| | 7 | Corner lot at minor intersection |
| | 4 | Mid-block but near intersection (<100ft) |
| | 0 | Mid-block, far from intersections |
| **Street-facing sightline** | 0-8 | |
| | 8 | Unobstructed view down 2+ street directions |
| | 5 | Clear view down 1 street direction |
| | 2 | Partial view (trees, awnings, but workable) |
| | 0 | Blocked (tall buildings, heavy tree cover) |
| **Cluster potential** | 0-7 | |
| | 7 | 3+ other viable venues within 200ft (anchor node) |
| | 5 | 2 other viable venues within 200ft |
| | 2 | 1 other venue nearby or residential density |
| | 0 | Isolated location, sparse surroundings |

**Category 3 Total: /25**

---

## Category 4: Foot Traffic & Dwell Time (15 points)

*How many users will connect to this coverage?*

**Data source:** Yelp/Google category, review count as popularity proxy, photos showing outdoor seating. **Confidence: Medium.**

| Factor | Points | Scoring |
|--------|--------|---------|
| **Peak foot traffic (inferred from category + reviews)** | 0-6 | |
| | 6 | High traffic category (coffee, fast-casual) + 200+ reviews |
| | 4 | Moderate traffic category or strong review count |
| | 2 | Low-moderate traffic (boutique, salon, side street location) |
| | 0 | Very low traffic (appointment-only, back alley, few reviews) |
| **Dwell time (inferred from category)** | 0-5 | |
| | 5 | High dwell category: co-working, coffee, gym, bar |
| | 3 | Medium dwell category: restaurant, salon, laundromat |
| | 1 | Low dwell category: dry cleaner, convenience, retail |
| **Outdoor seating / gathering area (observable)** | 0-4 | |
| | 4 | Patio, sidewalk seating visible in photos/Street View |
| | 2 | Standing area or occasional outdoor use |
| | 0 | No outdoor customer presence visible |

**Category 4 Total: /15**

---

## Category 5: Operational Reliability (10 points)

*Will this install stay online and accessible?*

**Data source:** Google/Yelp hours, Street View for visible infrastructure, business category norms. **Confidence: Medium.**

| Factor | Points | Scoring |
|--------|--------|---------|
| **Power access (inferred)** | 0-4 | |
| | 4 | Standard retail/restaurant (assume power available) |
| | 2 | Older building or unusual setup |
| | 0 | Outdoor-only venue or kiosk |
| **Internet backhaul (inferred from category)** | 0-3 | |
| | 3 | Tech-forward category (co-working, coffee shop) — assume WiFi |
| | 2 | Standard retail/restaurant — likely has WiFi |
| | 1 | Basic service business — cellular backup likely needed |
| | 0 | Outdoor venue or no clear backhaul |
| **Access hours (observable)** | 0-3 | |
| | 3 | Open 12+ hrs/day, 7 days/week (per Google/Yelp) |
| | 2 | Open 8+ hrs/day, 5+ days/week |
| | 1 | Limited hours or seasonal |
| | 0 | Irregular hours or frequently closed |

**Category 5 Total: /10**

---

## Score Interpretation

| Score Range | Priority | Action |
|-------------|----------|--------|
| **85-100** | CRITICAL | Anchor node — install within 48 hrs if possible |
| **70-84** | HIGH | Priority install — schedule within 1 week |
| **55-69** | MEDIUM | Standard pipeline — schedule within 2 weeks |
| **40-54** | LOW | Backfill candidate — install if capacity allows |
| **0-39** | DEPRIORITIZE | Do not pursue unless situation changes |

---

## Auto-Reject Rules

**Immediately disqualify a venue if ANY of the following are true:**

*Note: These are hard blockers discovered during research or outreach — not applied at initial lead generation.*

| Rule # | Auto-Reject Condition | Why |
|--------|----------------------|-----|
| AR-1 | No decision-maker identifiable after 2 contact attempts | Will never close |
| AR-2 | Landlord explicitly declined exterior modifications | Dead end |
| AR-3 | No power within 50ft of viable mount point | Install cost prohibitive |
| AR-4 | Basement-only or below-grade location | Zero coverage value |
| AR-5 | Venue closing/relocating within 6 months | Wasted hardware |
| AR-6 | Owner hostile or explicitly anti-tech | Will not close |
| AR-7 | Located in zone already at density target (3+ outdoor units within 400ft) | Diminishing returns |

*Note: National chains are NOT auto-rejected — they receive lower permissioning scores but may still be worth pursuing if location/mounting scores are exceptional.*

**If auto-reject triggered:** Mark lead as "Rejected - [Rule #]" and do not pursue further.

---

## High-Priority Archetypes

These venue profiles consistently score 75+ and should be prioritized in prospecting:

### Tier S: Anchor Nodes (Target: 85-100 points)

| Archetype | Why | Expected Score |
|-----------|-----|----------------|
| **Coffee shop on a corner with patio** | Corner = high location score, patio = outdoor mount, independent = good permissioning, high dwell | 85-95 |
| **Brewery/taproom with rooftop or patio** | Rooftop = high mount score, independent, high dwell category | 82-92 |
| **Co-working space in multi-story building** | Rooftop access likely, tech-forward category, all-day traffic | 80-90 |
| **Gym/fitness studio on corner lot** | Corner location, often has exterior signage = mount viable, independent | 78-88 |

### Tier A: High-Value Targets (Target: 70-84 points)

| Archetype | Why | Expected Score |
|-----------|-----|----------------|
| **Fast-casual restaurant with sidewalk seating** | Awning mount, patio = outdoor score, moderate traffic | 70-82 |
| **Wine bar / cocktail bar with outdoor area** | Patio visibility, independent, evening density | 68-80 |
| **Barber shop / salon on main drag** | Independent owner-operated category, but often mid-block | 65-75 |
| **Boutique retail on corner** | Corner location advantage, independent | 62-72 |

### Tier B: Solid Pipeline (Target: 55-69 points)

| Archetype | Why | Expected Score |
|-----------|-----|----------------|
| **Laundromat** | High dwell, but often mid-block, limited outdoor mount options | 55-65 |
| **Phone repair / tech shop** | Tech-forward, but small footprint, often mid-block | 52-62 |
| **Nail salon on main corridor** | Medium dwell, but often no outdoor option | 48-58 |

### Lower Priority (but not rejected)

| Archetype | Why | Expected Score |
|-----------|-----|----------------|
| **National chain fast food** | Low permissioning score (corporate), but may have good locations | 40-55 |
| **Bank branch** | Corporate = low permissioning, but often corner lots | 35-50 |
| **Large restaurant (full-service, chain)** | Manager layer, corporate approval | 35-50 |
| **Medical office / clinic** | Limited hours, compliance concerns | 30-45 |

*Note: Chains with exceptional locations (corner, clear mount options) may still be worth pursuing — just expect longer timelines.*

---

## 90-Second Scout Checklist

*Print this on a card. Complete at each venue during on-foot blitz.*

```
┌─────────────────────────────────────────────────────────────────┐
│  VENUE SCOUT CHECKLIST (90 sec)                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  VENUE NAME: _______________________  ZONE: ____               │
│  ADDRESS: __________________________  TIME: ____               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  1. OUTDOOR MOUNT? (look up)                     /35           │
│     □ Rooftop visible?        □ Yes □ No □ Maybe               │
│     □ Awning/overhang?        □ Yes □ No                       │
│     □ Exterior wall viable?   □ Yes □ No                       │
│     □ Owner controls exterior? □ Yes □ No □ Ask                │
│     □ Corner lot?             □ Yes □ No                       │
│     Quick score: ____/35                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  2. LOCATION VALUE (observe)                    /25            │
│     □ Corner/intersection?    □ Yes □ No                       │
│     □ Clear sightline?        □ 2+ streets □ 1 street □ None  │
│     □ Other good venues within 200ft? □ 3+ □ 2 □ 1 □ 0        │
│     Quick score: ____/25                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  3. TRAFFIC & DWELL (observe)                   /15            │
│     □ Busy right now?         □ High □ Med □ Low               │
│     □ Avg time customers stay? □ 60+ □ 15-60 □ <15 min        │
│     □ Outdoor seating/patio?  □ Yes □ No                       │
│     Quick score: ____/15                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  4. PERMISSIONING (observe)                     /15            │
│     □ Independent or chain?   □ Indep □ Local □ National       │
│     □ Visible tech installs?  □ Yes □ No                       │
│     Quick score: ____/15                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  5. RELIABILITY (observe or ask)                /10            │
│     □ Hours: Open ____am - ____pm, ____ days/wk                │
│     Quick score: ____/10                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  TOTAL SCORE: ____/100                                         │
│                                                                 │
│  □ AUTO-REJECT? (check if any apply)                           │
│    □ Can't find decision-maker (after 2 attempts)              │
│    □ Landlord already said no                                  │
│    □ No power anywhere                                         │
│    □ Below grade / basement                                    │
│    □ Closing soon                                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  VERDICT:  □ HOT (75+)  □ WARM (55-74)  □ COOL (40-54)  □ SKIP │
│                                                                 │
│  NEXT STEP:                                                    │
│    □ Spoke to DM — schedule install                            │
│    □ Left pamphlet — follow up in 48 hrs                       │
│    □ Return when owner is here: _____________ (day/time)       │
│    □ Add to outreach list (IG/email/phone)                     │
│    □ Skip — reason: _____________________                      │
│                                                                 │
│  PHOTO TAKEN? □ Yes                                            │
│  DM CONTACT: _________________________ (phone/email)           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Score Calculator (Quick Math)

For field use, use this simplified scoring (reflects reweighted categories):

| Category | Quick Question | Fast Score |
|----------|----------------|------------|
| Outdoor Mount (35%) | Can I see where we'd mount outside? | Yes = 30, Maybe = 18, No = 5 |
| Location (25%) | Corner lot with clear sightline? | Corner = 22, Near corner = 14, Mid-block = 6 |
| Traffic (15%) | Busy with people staying a while? | High+dwell = 13, Medium = 8, Low = 4 |
| Permissioning (15%) | Independent or chain? | Independent = 12, Local chain = 7, National = 3 |
| Reliability (10%) | Good hours visible? | 12+ hrs/day = 10, 8+ hrs = 6, Limited = 3 |

**Quick total = Outdoor + Location + Traffic + Permissioning + Reliability**

| Quick Total | Verdict |
|-------------|---------|
| 75+ | HOT — pitch now |
| 55-74 | WARM — leave pamphlet, follow up |
| 40-54 | COOL — add to list, low priority |
| <40 | SKIP |

---

## Appendix: Score Examples

### Example 1: Compass Coffee (Dupont Circle, corner of Connecticut & Q)

| Category | Factor | Score |
|----------|--------|-------|
| Outdoor Mount | Rooftop likely, signage matches business (owner controls), corner | 30/35 |
| Permissioning | Independent coffee shop, single location, owner-operated category | 13/15 |
| Location | Corner lot at major intersection, clear 2-street sightline, 4 venues nearby | 23/25 |
| Traffic | High-traffic category, 200+ reviews, high dwell, patio visible | 15/15 |
| Reliability | Standard retail (power assumed), tech-forward (WiFi assumed), long hours | 10/10 |
| **TOTAL** | | **91/100** |

**Verdict:** CRITICAL — Anchor node. Prioritize outreach.

---

### Example 2: Mid-Block Nail Salon (14th St, between U and V)

| Category | Factor | Score |
|----------|--------|-------|
| Outdoor Mount | No rooftop visible, small awning only, multi-tenant building | 12/35 |
| Permissioning | Independent, owner-operated category, but multi-tenant building | 8/15 |
| Location | Mid-block, partial sightline, 2 venues nearby | 11/25 |
| Traffic | Medium dwell category, moderate reviews | 8/15 |
| Reliability | Standard retail, likely WiFi, 10am-7pm 6 days | 8/10 |
| **TOTAL** | | **47/100** |

**Verdict:** LOW — Indoor-only candidate, backfill if capacity allows.

---

### Example 3: National Chain Pharmacy (Dupont Circle)

| Category | Factor | Score |
|----------|--------|-------|
| Outdoor Mount | Wall space visible, but corporate branding suggests limited control | 15/35 |
| Permissioning | National chain = 0 DM accessibility, corporate layers | 2/15 |
| Location | Corner lot, good sightline, cluster potential | 20/25 |
| Traffic | High traffic (reviews), but low dwell category | 5/15 |
| Reliability | Long hours, assume power/WiFi | 10/10 |
| **TOTAL** | | **52/100** |

**Verdict:** LOW — Exceptional location but permissioning drag. May be worth pursuing if no better options in area, but expect slow close.
