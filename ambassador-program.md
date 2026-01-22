# DC Ambassador Program — Commission-Based Install Sourcing

## Program Overview

**Mission:** Recruit local ambassadors to source qualified venue installations in Dupont Circle and 14th St/U St corridors, paying commission only for verified, high-quality deployments.

**Key Principles:**
1. Pay for RESULTS, not leads
2. Reward DENSITY, not sprawl
3. Verify EVERYTHING before payment
4. Clawback for fraud or failure

---

# Part 1: Commission Structure Options

## Option A: Simple Flat Rate

**Best for:** Pilot program, simple tracking, predictable costs

| Install Type | Commission |
|--------------|------------|
| Indoor hotspot installed + verified | $50 |
| Outdoor hotspot installed + verified | $75 |
| Combo (indoor + outdoor same venue) | $100 |

**Pros:** Easy to understand, easy to track
**Cons:** No incentive for density or high-value venues

---

## Option B: Tiered Performance

**Best for:** Motivating high performers, scaling effort

| Monthly Installs | Indoor Rate | Outdoor Rate | Combo Rate |
|------------------|-------------|--------------|------------|
| 1-5 installs | $40 | $60 | $80 |
| 6-15 installs | $50 | $75 | $100 |
| 16-30 installs | $60 | $90 | $120 |
| 31+ installs | $75 | $100 | $150 |

**Tier resets monthly.** Ambassadors climb tiers as they close more installs.

**Pros:** Rewards consistent performers, encourages volume
**Cons:** May incentivize quantity over quality

---

## Option C: Density Bonus (RECOMMENDED)

**Best for:** Achieving hyper-density goals in target zones

### Base Commission

| Install Type | Base Commission |
|--------------|-----------------|
| Indoor hotspot | $40 |
| Outdoor hotspot | $60 |
| Combo (same venue) | $80 |

### Density Multipliers

| Condition | Multiplier | Example Payout |
|-----------|------------|----------------|
| **Priority Zone** (D1, D2, U1, U2) | 1.5x | Indoor: $60 |
| **Anchor Node** (corner + outdoor + 75+ score) | 2.0x | Combo: $160 |
| **Cluster Bonus** (3+ installs within 300ft) | +$25 per install | Extra $75 for 3-unit cluster |
| **Speed Bonus** (install within 48hrs of lead) | +$15 | |
| **Tier 1 Venue** (coffee, cowork, brewery, gym) | 1.25x | Indoor: $50 |

### Density Bonus Examples

**Example 1: Standard indoor install in secondary zone**
- Base: $40
- No multipliers
- **Total: $40**

**Example 2: Outdoor install at corner coffee shop in D1 zone**
- Base outdoor: $60
- Priority Zone (D1): 1.5x = $90
- Tier 1 venue: 1.25x = $112.50
- **Total: $112.50**

**Example 3: Combo install at anchor node (corner brewery, 85 score)**
- Base combo: $80
- Anchor Node: 2.0x = $160
- Priority Zone (U1): already included in Anchor
- Speed Bonus (installed in 36hrs): +$15
- **Total: $175**

**Example 4: Cluster of 3 indoor installs on same block**
- 3x Indoor base: $40 × 3 = $120
- Priority Zone (D2): 1.5x = $180
- Cluster Bonus: +$25 × 3 = $75
- **Total: $255**

---

## Commission Comparison Table

| Scenario | Option A | Option B (Tier 2) | Option C |
|----------|----------|-------------------|----------|
| 1 indoor, secondary zone | $50 | $50 | $40 |
| 1 indoor, priority zone | $50 | $50 | $60 |
| 1 outdoor, corner, priority zone | $75 | $75 | $90-112 |
| Combo at anchor node | $100 | $100 | $160-175 |
| 3-unit cluster, priority zone | $150 | $150 | $255 |

**Recommendation: Option C** — Directly incentivizes the density clustering we need.

---

# Part 2: Qualification Checklist

## What Counts as a "Qualified Install"

A lead becomes a qualified install ONLY when ALL of the following are true:

### Stage 1: Lead Qualification (Before Install)

| # | Requirement | How to Verify |
|---|-------------|---------------|
| Q1 | Venue is within target boundaries (Dupont or 14th/U micro-zones) | GPS coordinates match zone |
| Q2 | Venue category is Tier 1, 2, or 3 (not excluded type) | Category confirmed |
| Q3 | Decision-maker has given verbal or written consent | Consent form or recorded confirmation |
| Q4 | Venue is not already in pipeline from another source | CRM check (no duplicate address) |
| Q5 | Ambassador personally sourced the lead (not transferred) | Ambassador attestation |

### Stage 2: Install Qualification (During Install)

| # | Requirement | How to Verify |
|---|-------------|---------------|
| Q6 | Hardware physically installed at venue | Photo evidence |
| Q7 | Hardware powered on and connected | Device online in Helium dashboard |
| Q8 | Indoor unit placed per guidelines (near window, proper height) | Photo of placement |
| Q9 | Outdoor unit mounted securely (if applicable) | Photo of mount |
| Q10 | Host agreement signed | Digital or paper signature |

### Stage 3: Verification (Post-Install)

| # | Requirement | How to Verify |
|---|-------------|---------------|
| Q11 | Device online for 72+ consecutive hours | Helium dashboard uptime check |
| Q12 | Business confirms installation via callback | Phone/text confirmation |
| Q13 | No duplicate device at same address | Device ID + address cross-check |
| Q14 | Install location matches claimed zone | GPS vs. claimed zone |

**Commission triggers ONLY after Stage 3 verification passes (minimum 72 hours post-install).**

---

## Excluded Venue Types (Never Qualify)

| Exclusion | Reason |
|-----------|--------|
| Residential addresses | Not commercial deployment |
| Ambassador's own home/business | Conflict of interest |
| Family member's business | Conflict of interest |
| Venues outside target neighborhoods | Not part of density strategy |
| National chains requiring corporate approval | Install unlikely to complete |
| Venues with existing Helium hotspot | Duplicate coverage |
| Temporary/pop-up locations | No long-term value |
| Venues closing within 6 months | Wasted hardware |

---

# Part 3: Verification Process

## Verification Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    VERIFICATION PIPELINE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LEAD SUBMITTED                                                 │
│       │                                                         │
│       ▼                                                         │
│  ┌─────────────────┐                                           │
│  │ AUTO-CHECK #1   │ Duplicate address check                   │
│  │ (Instant)       │ Zone boundary check                       │
│  └────────┬────────┘ Excluded category check                   │
│           │                                                     │
│           ▼ PASS                                                │
│  ┌─────────────────┐                                           │
│  │ INSTALL         │ Ambassador or installer completes         │
│  │ SCHEDULED       │ install at venue                          │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │ PHOTO + GPS     │ 4 required photos                         │
│  │ SUBMISSION      │ GPS timestamp on each                     │
│  └────────┬────────┘ Device ID captured                        │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │ AUTO-CHECK #2   │ GPS matches claimed address?              │
│  │ (Instant)       │ Device online in dashboard?               │
│  └────────┬────────┘ Photos meet requirements?                 │
│           │                                                     │
│           ▼ PASS                                                │
│  ┌─────────────────┐                                           │
│  │ 72-HOUR HOLD    │ Device must stay online                   │
│  │                 │ No disconnection > 4 hours                │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │ HOST CALLBACK   │ "Is there a Helium device at your         │
│  │ (Within 5 days) │  business? Who installed it?"             │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼ CONFIRMED                                           │
│  ┌─────────────────┐                                           │
│  │ COMMISSION      │ Ambassador paid in next                   │
│  │ APPROVED        │ weekly payout cycle                       │
│  └─────────────────┘                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Required Photo Evidence

Every install must include **4 photos** with GPS metadata:

| Photo # | Requirement | What It Proves |
|---------|-------------|----------------|
| 1 | **Storefront exterior** with visible business name/signage | Correct venue |
| 2 | **Indoor unit in place** showing device, power connection, and surrounding context | Proper installation |
| 3 | **Device serial number / QR code** close-up | Device ID verification |
| 4 | **Outdoor unit** (if applicable) showing mount and orientation | Outdoor install quality |

**Photo requirements:**
- GPS metadata enabled (auto-embedded by phone)
- Taken within 1 hour of install completion
- No filters or edits
- Faces of non-consenting individuals blurred

---

## GPS Verification Rules

| Check | Tolerance | Action if Fail |
|-------|-----------|----------------|
| Photo GPS vs. claimed address | ±150 ft | Flag for manual review |
| Photo GPS vs. target zone boundary | Must be inside | Auto-reject |
| All 4 photos same GPS cluster | Within 300 ft of each other | Flag if spread wider |
| Photo timestamp vs. submission | Within 24 hours | Flag for review |

---

## Host Callback Script

**Performed 3-5 days post-install by verification team (not ambassador):**

```
"Hi, this is [Name] from Helium Mobile. I'm calling to confirm a recent
installation at [Business Name].

1. Do you have a small wireless device installed at your business recently?
   [If no → FLAG]

2. Do you recall who installed it?
   [Record answer — should match ambassador or installer name]

3. Is the device still plugged in and in place?
   [If no → FLAG]

4. Were you satisfied with the installation process?
   [Note any issues]

Thank you! The device is providing mobile coverage to your customers
and the surrounding area. Please keep it plugged in. If you have any
issues, call [support number]."
```

**Callback outcomes:**
- **Confirmed:** Commission approved
- **No Answer (3 attempts):** Hold commission, extend verification
- **Denies installation:** Immediate flag, investigate fraud
- **Device removed:** Clawback eligible

---

# Part 4: Dispute Resolution & Clawback Rules

## Dispute Categories

| Category | Description | Resolution Path |
|----------|-------------|-----------------|
| **Attribution dispute** | Two ambassadors claim same venue | First-in-CRM wins; timestamp is proof |
| **Zone dispute** | Ambassador claims venue is in priority zone | GPS coordinates are definitive |
| **Qualification dispute** | Ambassador disagrees with rejection | Submit appeal with evidence |
| **Commission calculation** | Ambassador disputes payout amount | Provide breakdown; recalculate if error |
| **Clawback dispute** | Ambassador disputes clawback | Evidence review within 7 days |

---

## Attribution Rules (Who Gets Credit)

| Scenario | Who Gets Credit |
|----------|-----------------|
| Ambassador A submits lead, Ambassador B closes | Ambassador A (sourced) |
| Ambassador submits, internal team closes | Ambassador (sourced) |
| Two ambassadors submit same address | First submission timestamp wins |
| Ambassador sources lead from QR pamphlet scan | QR pamphlet program (not ambassador) |
| Venue was already contacted by internal team | Internal team (no ambassador credit) |

**Key rule:** Timestamp in CRM is the only proof of attribution. Verbal claims without CRM entry = no credit.

---

## Clawback Rules

**Commission can be clawed back (deducted from future payouts) if:**

| Clawback Trigger | Timeframe | Clawback Amount |
|------------------|-----------|-----------------|
| Device goes offline within 14 days (not due to venue) | 14 days | 100% of commission |
| Device removed by host within 30 days | 30 days | 100% of commission |
| Fraudulent submission discovered | Any time | 100% + ban |
| Host denies ever consenting | Any time | 100% + investigation |
| Duplicate claim (ambassador claimed venue already paid to another) | Any time | 100% + warning |
| GPS/photo manipulation detected | Any time | 100% + permanent ban |
| Venue outside target zone (boundary fraud) | Any time | 100% + warning |

---

## Fraud Indicators (Auto-Flag)

| Indicator | Response |
|-----------|----------|
| 5+ submissions in 1 hour from same ambassador | Hold all, manual review |
| Photos without GPS metadata | Reject, require resubmission |
| GPS coordinates >500ft from claimed address | Reject |
| Same device ID submitted twice | Reject second, investigate |
| Host callback: "I don't know this person" | Freeze ambassador, investigate |
| Multiple venues with same phone number | Flag for review |
| Ambassador submits own address or family | Permanent ban |

---

## Fraud Prevention Layers

| Layer | What It Catches |
|-------|-----------------|
| **CRM duplicate check** | Same address submitted twice |
| **GPS verification** | Wrong location claims |
| **Device ID tracking** | Same device moved between venues |
| **Host callback** | Fabricated installs |
| **72-hour uptime hold** | "Install and immediately remove" scams |
| **Photo metadata analysis** | Stock photos, old photos, edited photos |
| **Commission velocity limits** | Unrealistic submission rates |

---

## Strike System

| Strikes | Consequence |
|---------|-------------|
| 1 strike | Warning + training reminder |
| 2 strikes | Commission held for 14 days pending review |
| 3 strikes | 30-day suspension from program |
| 4 strikes | Permanent ban, all pending commissions forfeited |

**Strike-worthy offenses:**
- Submitting unqualified venues (1 strike)
- Zone boundary violation (1 strike)
- Missing/invalid photos (1 strike)
- Host complaint (2 strikes)
- Any fraud attempt (immediate permanent ban)

---

# Part 5: Weekly Leaderboard & Incentives

## Leaderboard Categories

**Posted every Monday, covering prior week (Mon-Sun):**

| Category | Metric | Prize |
|----------|--------|-------|
| **Most Installs** | Total verified installs | $200 bonus |
| **Highest Density** | Most installs within 500ft radius | $150 bonus |
| **Best Anchor Hunter** | Most 80+ score venues | $150 bonus |
| **Fastest Closer** | Shortest avg lead-to-install time | $100 bonus |
| **Outdoor Champion** | Most outdoor installs | $100 bonus |

**Ties:** Split prize or use secondary metric (total score)

---

## Weekly Bonus Structure

### Individual Bonuses

| Achievement | Bonus |
|-------------|-------|
| First install of the week (any ambassador) | $25 |
| 5 installs in a week | $50 |
| 10 installs in a week | $150 |
| 15+ installs in a week | $300 |
| Perfect week (all submissions verified, zero rejections) | $75 |

### Team/Cohort Bonuses

| Achievement | Bonus (split among all ambassadors) |
|-------------|-------------------------------------|
| 50 total installs across all ambassadors in a week | $500 pool |
| 100 total installs in a week | $1,500 pool |
| Full coverage of a micro-zone achieved | $1,000 pool |

---

## Milestone Bonuses (Cumulative)

| Lifetime Installs | Bonus | Badge |
|-------------------|-------|-------|
| 10 verified installs | $100 | Bronze Deployer |
| 25 verified installs | $250 | Silver Deployer |
| 50 verified installs | $500 | Gold Deployer |
| 100 verified installs | $1,000 | Platinum Deployer |
| 200 verified installs | $2,500 | Diamond Deployer |

**Badges unlock:**
- Priority support channel access
- Early access to new zones/hardware
- Invitation to deployer events
- Referral bonus eligibility (recruit other ambassadors)

---

## Leaderboard Display Format

```
┌─────────────────────────────────────────────────────────────────┐
│           DC AMBASSADOR LEADERBOARD — Week of Jan 20           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MOST INSTALLS                          HIGHEST DENSITY         │
│  ────────────────                       ─────────────────       │
│  1. @marcus_dc      12 installs  $200   1. @jenna_dupont  8/500ft│
│  2. @sarah_14th      9 installs         2. @marcus_dc     6/500ft│
│  3. @jenna_dupont    8 installs         3. @tyrell_nw     5/500ft│
│                                                                 │
│  BEST ANCHOR HUNTER                     OUTDOOR CHAMPION        │
│  ───────────────────                    ────────────────        │
│  1. @tyrell_nw    5 anchors (85+ avg)   1. @sarah_14th  4 outdoor│
│  2. @sarah_14th   4 anchors             2. @marcus_dc   3 outdoor│
│  3. @marcus_dc    3 anchors             3. @tyrell_nw   2 outdoor│
│                                                                 │
│  FASTEST CLOSER                                                 │
│  ───────────────                                                │
│  1. @jenna_dupont   18 hrs avg                                  │
│  2. @marcus_dc      26 hrs avg                                  │
│  3. @sarah_14th     32 hrs avg                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  WEEKLY TOTALS                                                  │
│  Total installs: 47    Indoor: 38    Outdoor: 9                 │
│  Dupont: 22            14th/U: 25                               │
│  Team bonus unlocked: $500 pool (50+ installs!)                 │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  TOP EARNERS THIS WEEK                                          │
│  1. @marcus_dc      $847  (12 installs + bonuses)               │
│  2. @sarah_14th     $612  (9 installs + outdoor bonus)          │
│  3. @jenna_dupont   $589  (8 installs + density bonus)          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Momentum Mechanics

### Daily Challenges (Optional, +$10-25)

| Day | Challenge | Bonus |
|-----|-----------|-------|
| Monday | First install of the week | $25 |
| Tuesday | Install in a new micro-zone | $15 |
| Wednesday | Outdoor install | $20 |
| Thursday | Tier 1 venue | $15 |
| Friday | 80+ score venue | $20 |
| Weekend | Any 2 installs | $25 |

### Streak Bonuses

| Streak | Bonus |
|--------|-------|
| 3 consecutive days with install | $30 |
| 5 consecutive days with install | $75 |
| 7 consecutive days with install | $150 |
| 14 consecutive days with install | $400 |

---

## Payment Schedule

| Item | Timing |
|------|--------|
| Commission calculation | Every Sunday 11:59pm |
| Verification window | Monday-Wednesday |
| Payout processed | Thursday |
| Funds received | Friday (direct deposit or PayPal) |

**Minimum payout threshold:** $50 (balances below roll to next week)

---

## Ambassador Onboarding Checklist

Before an ambassador can earn:

| Step | Requirement |
|------|-------------|
| 1 | Complete 15-min training video |
| 2 | Pass 10-question qualification quiz (80%+) |
| 3 | Sign ambassador agreement (commission terms, fraud policy) |
| 4 | Submit W-9 (for US tax reporting) |
| 5 | Set up payment method (direct deposit or PayPal) |
| 6 | Complete 1 supervised "shadow" install with mentor |
| 7 | Receive ambassador kit (pamphlets, QR cards, talking points) |

**Time to activate:** Same day if all steps completed

---

## Quick Reference: Commission Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│              AMBASSADOR COMMISSION CHEAT SHEET                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BASE RATES                                                     │
│  ──────────                                                     │
│  Indoor:  $40    Outdoor:  $60    Combo:  $80                  │
│                                                                 │
│  MULTIPLIERS (stack)                                            │
│  ───────────────────                                            │
│  Priority Zone (D1, D2, U1, U2):     1.5x                      │
│  Anchor Node (corner + outdoor + 75+): 2.0x                    │
│  Tier 1 Venue:                        1.25x                    │
│                                                                 │
│  BONUSES (add)                                                  │
│  ─────────────                                                  │
│  Cluster (3+ within 300ft):     +$25 each                      │
│  Speed (<48hrs):                +$15                           │
│  Weekly 5 installs:             +$50                           │
│  Weekly 10 installs:            +$150                          │
│                                                                 │
│  EXAMPLE PAYOUTS                                                │
│  ───────────────                                                │
│  Basic indoor, secondary zone:       $40                       │
│  Indoor, priority zone:              $60                       │
│  Combo, anchor, speed bonus:         $175                      │
│  3-unit cluster, priority zone:      $255                      │
│                                                                 │
│  DISQUALIFIERS (no pay)                                        │
│  ──────────────────────                                         │
│  ✗ Outside target zones                                        │
│  ✗ Missing photos or GPS                                       │
│  ✗ Device offline < 72 hrs                                     │
│  ✗ Host denies consent                                         │
│  ✗ Duplicate address                                           │
│  ✗ Your own home/family business                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
