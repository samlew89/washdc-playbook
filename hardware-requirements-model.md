# Hardware Requirements Model — DC Hyper-Density Deployment

## Coverage Assumptions

### Indoor Hotspots
- **Effective coverage:** ~1,500 sq ft per unit
- **Typical venue needs:**
  - Small venue (<1,500 sq ft): 1 unit
  - Medium venue (1,500-3,000 sq ft): 2 units
  - Large venue (3,000-5,000 sq ft): 3 units
  - Very large (5,000+ sq ft): 4+ units

### Outdoor Hotspots
- **Theoretical max range:** 800 ft line-of-sight
- **DC urban reality:** Buildings, trees, parked cars, signage, and pedestrians create significant obstruction
- **Effective coverage radius in DC corridors:**
  - Corner mount (20ft+ height): ~300-400 ft effective radius
  - Mid-block wall mount (15ft height): ~200-250 ft effective radius
  - Awning mount (10-12ft height): ~150-200 ft effective radius
  - Ground-level (<10ft): ~100 ft effective radius (not recommended)

### Urban Corridor Spacing Logic

**The goal is overlapping coverage with no dead zones.**

```
Street View — Outdoor Hotspot Spacing (14th St Example)

                    ← 300ft →     ← 300ft →     ← 300ft →
    ┌─────────────────┬─────────────────┬─────────────────┐
    │                 │                 │                 │
    │    [OUTDOOR]    │    [OUTDOOR]    │    [OUTDOOR]    │
    │     Unit A      │     Unit B      │     Unit C      │
    │   @ Corner      │   @ Mid-block   │   @ Corner      │
    │   (20ft high)   │   (15ft high)   │   (20ft high)   │
    │                 │                 │                 │
    │   ←──400ft──→   │   ←──250ft──→   │   ←──400ft──→   │
    │    coverage     │    coverage     │    coverage     │
    │                 │                 │                 │
====│=================│=================│=================│====
    │     14TH ST     │     14TH ST     │     14TH ST     │
====│=================│=================│=================│====
    │                 │                 │                 │
    │     ←─ overlap zone ─→           │                 │
    │        (~100ft)                   │                 │
    └─────────────────┴─────────────────┴─────────────────┘

Coverage overlap ensures no dead zones as users walk the corridor.
```

**Spacing Rules:**
1. **Corner-to-corner:** 500-600 ft max (corners have best coverage)
2. **Corner-to-midblock:** 300-400 ft max
3. **Midblock-to-midblock:** 250-350 ft max (midblock has weaker coverage)
4. **Always prioritize corners** — they cover 2 street directions
5. **Height matters** — every 5ft of elevation adds ~50ft effective radius

---

# Dupont Circle — Micro-Pod Definitions

## Pod D1: Connecticut Ave Core

**Boundaries:**
- North: R St NW
- South: N St NW
- Primary corridor: Connecticut Ave NW (both sides)
- Depth: 1/2 block east and west of Connecticut

**Street geometry:**
- Connecticut Ave runs NW-SE through the area
- ~8 blocks of commercial frontage
- Major cross streets: N, O, P, Q, R
- Distance N St to R St: ~1,600 ft

**Venue density estimate:**
- ~80-100 total venues in zone
- ~25-35 Tier 1/2 venues (install targets)
- Avg venue size: 1,500-2,500 sq ft

**Coverage target:** Continuous outdoor coverage along Connecticut Ave from N St to R St

---

## Pod D2: 17th St Strip

**Boundaries:**
- North: R St NW
- South: P St NW
- Primary corridor: 17th St NW (both sides)
- Depth: 1/2 block east and west

**Street geometry:**
- 17th St runs N-S
- ~4 blocks of dense bar/restaurant row
- Cross streets: P, Q, R
- Distance P St to R St: ~800 ft

**Venue density estimate:**
- ~40-50 total venues in zone
- ~15-20 Tier 1/2 venues
- Avg venue size: 2,000-3,500 sq ft (larger restaurants/bars)

**Coverage target:** Continuous outdoor coverage along 17th St from P to R

---

## Pod D3: Dupont Circle Ring

**Boundaries:**
- The traffic circle itself
- Immediate storefronts facing the circle
- ~200 ft radius from circle center

**Street geometry:**
- Circular intersection of Connecticut, Massachusetts, P St, 19th St, New Hampshire
- High pedestrian density in park/circle
- Premium visibility locations

**Venue density estimate:**
- ~15-20 venues facing the circle
- ~8-12 Tier 1/2 venues
- Mixed sizes

**Coverage target:** Blanket the circle and immediate surroundings

---

## Pod D4: P St Connector (Optional)

**Boundaries:**
- P St from Dupont Circle to 21st St
- ~6 blocks westward

**Street geometry:**
- P St runs E-W
- Connects Dupont Circle to residential/retail west
- Distance: ~1,000 ft

**Venue density estimate:**
- ~30-40 venues
- ~10-15 Tier 1/2 venues
- Smaller retail/service businesses

**Coverage target:** Connect Pod D3 (Circle) to western coverage

---

# Dupont Circle — Hardware Plans

## Pod D1: Connecticut Ave Core

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 12 | 1.5 | 18 |
| Tier 2 | 15 | 1.3 | 20 |
| Tier 3 | 8 | 1.0 | 8 |
| **Total** | **35** | | **46** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: Connecticut & R | 350 ft | — | 1 |
| Corner: Connecticut & Q | 350 ft | 400 ft from R | 1 |
| Mid-block: between Q & P | 200 ft | 300 ft from Q | 1 |
| Corner: Connecticut & P | 350 ft | 300 ft from mid | 1 |
| Corner: Connecticut & O | 350 ft | 400 ft from P | 1 |
| Mid-block: between O & N | 200 ft | 300 ft from O | 1 |
| Corner: Connecticut & N | 350 ft | 300 ft from mid | 1 |
| **Total** | | | **7** |

**Pod D1 Total:** 46 indoor + 7 outdoor = **53 units**

---

## Pod D2: 17th St Strip

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 8 | 2.0 | 16 |
| Tier 2 | 10 | 1.5 | 15 |
| Tier 3 | 4 | 1.0 | 4 |
| **Total** | **22** | | **35** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: 17th & R | 350 ft | — | 1 |
| Mid-block: between R & Q | 200 ft | 300 ft from R | 1 |
| Corner: 17th & Q | 350 ft | 250 ft from mid | 1 |
| Corner: 17th & P | 350 ft | 400 ft from Q | 1 |
| **Total** | | | **4** |

**Pod D2 Total:** 35 indoor + 4 outdoor = **39 units**

---

## Pod D3: Dupont Circle Ring

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 5 | 1.5 | 8 |
| Tier 2 | 5 | 1.3 | 7 |
| Tier 3 | 3 | 1.0 | 3 |
| **Total** | **13** | | **18** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| North side of circle (high elevation) | 400 ft | — | 1 |
| South side of circle | 400 ft | 300 ft from N | 1 |
| East spoke (Connecticut incoming) | 300 ft | 250 ft from S | 1 |
| **Total** | | | **3** |

**Pod D3 Total:** 18 indoor + 3 outdoor = **21 units**

---

## Pod D4: P St Connector (Optional)

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 4 | 1.3 | 5 |
| Tier 2 | 6 | 1.2 | 7 |
| Tier 3 | 5 | 1.0 | 5 |
| **Total** | **15** | | **17** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: P & 20th | 350 ft | — | 1 |
| Mid-block: P between 20th & 21st | 200 ft | 350 ft from 20th | 1 |
| Corner: P & 21st | 350 ft | 250 ft from mid | 1 |
| **Total** | | | **3** |

**Pod D4 Total:** 17 indoor + 3 outdoor = **20 units**

---

## Dupont Circle — Scenario Summary

| Scenario | Pods Included | Indoor | Outdoor | **Total** |
|----------|---------------|--------|---------|-----------|
| **LOW: Minimum Viable** | D1 only | 46 | 7 | **53** |
| **MEDIUM: Strong Density** | D1 + D2 + D3 | 99 | 14 | **113** |
| **HIGH: Dominate Corridor** | D1 + D2 + D3 + D4 | 116 | 17 | **133** |

---

# 14th St + U St — Micro-Pod Definitions

## Pod U1: 14th St Main Drag

**Boundaries:**
- North: W St NW
- South: T St NW
- Primary corridor: 14th St NW (both sides)
- Depth: 1/2 block east and west

**Street geometry:**
- 14th St runs N-S
- ~6 blocks of prime commercial
- Cross streets: T, U, V, W
- Distance T St to W St: ~1,200 ft

**Venue density estimate:**
- ~100-120 total venues
- ~35-45 Tier 1/2 venues
- Avg venue size: 1,500-2,500 sq ft

**Coverage target:** Continuous outdoor coverage along 14th St spine

---

## Pod U2: U St Corridor

**Boundaries:**
- U St from 13th St to 16th St
- Both sides of street
- Depth: 1/2 block north and south

**Street geometry:**
- U St runs E-W
- ~6 blocks of nightlife/entertainment
- Cross streets: 13th, 14th, 15th, 16th
- Distance 13th to 16th: ~1,200 ft

**Venue density estimate:**
- ~60-80 total venues
- ~25-30 Tier 1/2 venues
- Larger venues (bars, clubs, restaurants)

**Coverage target:** Continuous coverage along U St bar corridor

---

## Pod U3: 14th & U Intersection Anchor

**Boundaries:**
- 200 ft radius from 14th & U intersection
- All four corners + immediate adjacent

**Street geometry:**
- Major intersection, high visibility
- Metro station nearby
- Peak pedestrian density

**Venue density estimate:**
- ~15-20 venues at/near intersection
- ~10-12 Tier 1/2 venues
- Mixed sizes, high value

**Coverage target:** Blanket the intersection as anchor node

---

## Pod U4: V St Backfill (Optional)

**Boundaries:**
- V St from 13th to 15th St
- Secondary street parallel to U St

**Street geometry:**
- V St runs E-W
- ~4 blocks
- Emerging restaurant/bar scene
- Distance: ~800 ft

**Venue density estimate:**
- ~25-35 venues
- ~10-15 Tier 1/2 venues
- Smaller, newer businesses

**Coverage target:** Fill gap between 14th St and U St pods

---

# 14th St + U St — Hardware Plans

## Pod U1: 14th St Main Drag

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 15 | 1.5 | 23 |
| Tier 2 | 20 | 1.3 | 26 |
| Tier 3 | 10 | 1.0 | 10 |
| **Total** | **45** | | **59** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: 14th & W | 350 ft | — | 1 |
| Mid-block: between W & V | 200 ft | 300 ft from W | 1 |
| Corner: 14th & V | 350 ft | 250 ft from mid | 1 |
| Corner: 14th & U | 400 ft | 400 ft from V | 1 (shared w/ U3) |
| Mid-block: between U & T | 200 ft | 300 ft from U | 1 |
| Corner: 14th & T | 350 ft | 300 ft from mid | 1 |
| **Total** | | | **6** |

**Pod U1 Total:** 59 indoor + 6 outdoor = **65 units**

---

## Pod U2: U St Corridor

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 10 | 2.0 | 20 |
| Tier 2 | 12 | 1.5 | 18 |
| Tier 3 | 8 | 1.0 | 8 |
| **Total** | **30** | | **46** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: U & 13th | 350 ft | — | 1 |
| Corner: U & 14th | 400 ft | 400 ft from 13th | 1 (shared w/ U1) |
| Mid-block: between 14th & 15th | 200 ft | 300 ft from 14th | 1 |
| Corner: U & 15th | 350 ft | 250 ft from mid | 1 |
| Corner: U & 16th | 350 ft | 400 ft from 15th | 1 |
| **Total** | | | **5** |

Note: 14th & U corner counted in U1, so net new = **4**

**Pod U2 Total:** 46 indoor + 4 outdoor = **50 units**

---

## Pod U3: 14th & U Intersection Anchor

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 5 | 1.5 | 8 |
| Tier 2 | 5 | 1.3 | 7 |
| Tier 3 | 3 | 1.0 | 3 |
| **Total** | **13** | | **18** |

### Outdoor Hardware

The 14th & U corner unit serves as anchor for this pod (already counted in U1).

**Additional high-elevation unit** on tallest building at intersection for 360° coverage:

| Mount Location | Coverage Radius | Units Needed |
|----------------|-----------------|--------------|
| Rooftop at 14th & U (if available) | 500 ft | 1 |

**Pod U3 Total:** 18 indoor + 1 outdoor = **19 units**

---

## Pod U4: V St Backfill (Optional)

### Indoor Hardware

| Venue Tier | Est. Venues | Avg Units/Venue | Indoor Units |
|------------|-------------|-----------------|--------------|
| Tier 1 | 5 | 1.3 | 7 |
| Tier 2 | 7 | 1.2 | 8 |
| Tier 3 | 5 | 1.0 | 5 |
| **Total** | **17** | | **20** |

### Outdoor Hardware

| Mount Location | Coverage Radius | Spacing | Units Needed |
|----------------|-----------------|---------|--------------|
| Corner: V & 14th | 350 ft | — | 1 |
| Corner: V & 13th | 350 ft | 400 ft from 14th | 1 |
| **Total** | | | **2** |

**Pod U4 Total:** 20 indoor + 2 outdoor = **22 units**

---

## 14th St + U St — Scenario Summary

| Scenario | Pods Included | Indoor | Outdoor | **Total** |
|----------|---------------|--------|---------|-----------|
| **LOW: Minimum Viable** | U1 only | 59 | 6 | **65** |
| **MEDIUM: Strong Density** | U1 + U2 + U3 | 123 | 11 | **134** |
| **HIGH: Dominate Corridor** | U1 + U2 + U3 + U4 | 143 | 13 | **156** |

---

# Combined Hardware Summary — Both Neighborhoods

## Scenario Comparison

| Scenario | Dupont Indoor | Dupont Outdoor | 14th/U Indoor | 14th/U Outdoor | **TOTAL** |
|----------|---------------|----------------|---------------|----------------|-----------|
| **LOW** | 46 | 7 | 59 | 6 | **118** |
| **MEDIUM** | 99 | 14 | 123 | 11 | **247** |
| **HIGH** | 116 | 17 | 143 | 13 | **289** |

## Recommended: MEDIUM Scenario

**Why MEDIUM:**
- Covers all high-value pods without overextending
- Creates true contiguous coverage along main corridors
- Indoor/outdoor ratio (~8:1) balances venue penetration with street coverage
- Achievable with 60-80 venue closes (realistic for 4-week push)

**MEDIUM scenario hardware order:**

| Item | Quantity | Buffer (10%) | **Order Total** |
|------|----------|--------------|-----------------|
| Indoor hotspots | 222 | +22 | **244** |
| Outdoor hotspots | 25 | +3 | **28** |
| **TOTAL UNITS** | 247 | +25 | **272** |

---

# Outdoor Spacing — Detailed Explanation

## Why Urban Coverage is Reduced

**Theoretical vs. Reality:**

| Factor | Impact on Range |
|--------|-----------------|
| Building walls (brick, concrete) | -50% to -80% signal penetration |
| Parked cars and trucks | -20% at street level |
| Street trees (especially with leaves) | -30% to -50% |
| Pedestrian density | -10% to -20% (bodies absorb signal) |
| Competing RF signals | -10% to -15% interference |
| Humidity/rain | -5% to -15% |

**Result:** 800 ft theoretical → 200-400 ft effective in DC corridors

## Optimal Outdoor Placement Hierarchy

**Priority 1: Corner mounts at 20ft+ elevation**
- Cover 2 street directions
- Clear sightlines down both streets
- 350-400 ft effective radius
- Space these 500-600 ft apart

**Priority 2: Mid-block mounts at 15ft+ elevation**
- Fill gaps between corners
- 200-250 ft effective radius
- Space 300-400 ft from nearest corner

**Priority 3: Low mounts (10-15ft) — only if no other option**
- Awnings, first-floor wall mounts
- 150-200 ft effective radius
- Space 250-300 ft apart

## Overlap Zones Are Intentional

```
Coverage Diagram — Plan View (Looking Down)

                Corner A                    Corner B
                   ●                           ●
                  /│\                         /│\
                 / │ \                       / │ \
                /  │  \                     /  │  \
               /   │   \                   /   │   \
         350ft│    │    │350ft       350ft│    │    │350ft
              │    │    │                 │    │    │
               \   │   /                   \   │   /
                \  │  /                     \  │  /
                 \ │ /                       \ │ /
                  \│/                         \│/
                   ▼                           ▼
                   └─────── ~100ft overlap ─────┘
                         (no dead zone)

Users walking from A to B never lose coverage.
Handoff happens in overlap zone.
```

**Target overlap:** 50-100 ft between adjacent unit coverage areas

## Street Width Considerations

| Street Type | Width | Impact |
|-------------|-------|--------|
| Connecticut Ave | ~80 ft | Opposite side = ~40% signal strength |
| 14th St | ~70 ft | Opposite side = ~50% signal strength |
| Side streets | ~50 ft | Opposite side = ~60% signal strength |

**Implication:** For wide avenues, mount on BOTH sides of the street for full coverage. For narrow side streets, one side may suffice.

---

# Hardware Staging Plan

## Phase 1: Anchor Nodes (Week 1)
Deploy at highest-value intersections first:
- Dupont: Connecticut & Q, 17th & R, Dupont Circle north
- 14th/U: 14th & U, U & 13th, 14th & W

**Phase 1 hardware:** 8 outdoor + 30 indoor = **38 units**

## Phase 2: Corridor Fill (Week 2-3)
Fill gaps along main corridors:
- Dupont: Remaining Connecticut Ave, 17th St strip
- 14th/U: Remaining 14th St, U St corridor

**Phase 2 hardware:** 12 outdoor + 100 indoor = **112 units**

## Phase 3: Density Completion (Week 4)
Complete secondary pods and backfill:
- Dupont: P St connector, remaining circle venues
- 14th/U: V St backfill, remaining venues

**Phase 3 hardware:** 5 outdoor + 92 indoor = **97 units**

---

# Quick Reference: Outdoor Spacing Rules

| Situation | Spacing Rule |
|-----------|--------------|
| Corner to corner (same street) | 500-600 ft max |
| Corner to mid-block | 300-400 ft max |
| Mid-block to mid-block | 250-350 ft max |
| Across intersection (diagonal) | 400-500 ft max |
| Wide avenue (need both sides) | Mount on both sides, stagger 200 ft |

| Mount Height | Effective Radius | Priority |
|--------------|------------------|----------|
| Rooftop (40ft+) | 400-500 ft | Anchor nodes only |
| High wall (20-40ft) | 300-400 ft | Primary |
| Low wall (10-20ft) | 200-250 ft | Fill gaps |
| Awning (<10ft) | 150-200 ft | Last resort |
