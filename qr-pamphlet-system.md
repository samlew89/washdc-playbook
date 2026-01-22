# QR Pamphlet Lead Capture System

## Design Principles

1. **No crypto language** — Zero mentions of blockchain, tokens, Helium, Web3, or mining
2. **Local business focus** — "Your neighborhood," "local businesses," "your customers"
3. **Value-first messaging** — Free hardware, better connectivity, no cost to you
4. **Low-friction form** — 2 minutes max, mobile-optimized
5. **Built-in qualification** — Form fields that filter and score leads automatically

---

# Part 1: Pamphlet Text

## Front Side (5.5" x 4.25" — Half-letter landscape)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│          FREE MOBILE                                            │
│          COVERAGE UPGRADE                                       │
│          FOR YOUR BUSINESS                                      │
│                                                                 │
│                                                                 │
│   We're building better mobile connectivity                     │
│   in [Dupont Circle / 14th & U Street].                        │
│                                                                 │
│   Local businesses like yours are getting                       │
│   FREE hardware that improves cell coverage                     │
│   for your customers and the whole block.                       │
│                                                                 │
│                                                                 │
│          ┌─────────────┐                                       │
│          │             │                                        │
│          │   [QR CODE] │    Scan to see if                     │
│          │             │    your business qualifies             │
│          └─────────────┘                                       │
│                                                                 │
│          Takes 2 minutes. No obligations.                       │
│                                                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Print versions:**
- Dupont Circle version (blue accent)
- 14th & U St version (orange accent)

---

## Back Side

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  WHAT YOU GET (FREE)                                           │
│  ───────────────────                                           │
│                                                                 │
│  ✓  Indoor wireless unit (worth $250+)                         │
│     Improves mobile signal inside your business                │
│                                                                 │
│  ✓  Outdoor unit option (worth $350+)                          │
│     Extends coverage to the sidewalk and street                │
│                                                                 │
│  ✓  Professional installation                                  │
│     15-20 minutes, scheduled when it works for you             │
│                                                                 │
│  ✓  No monthly fees. No contracts. It's yours.                 │
│                                                                 │
│                                                                 │
│  WHY WE'RE DOING THIS                                          │
│  ────────────────────                                          │
│                                                                 │
│  We're a mobile network expanding coverage in DC.              │
│  We partner with local businesses to host small                │
│  wireless devices that make connectivity better                │
│  for everyone in the neighborhood.                             │
│                                                                 │
│  You get free hardware. Your customers get better              │
│  signal. The neighborhood gets stronger coverage.              │
│                                                                 │
│                                                                 │
│  QUESTIONS?                                                    │
│  ──────────                                                    │
│  Text "INFO" to (202) XXX-XXXX                                 │
│  or email dc@[domain].com                                      │
│                                                                 │
│                                                                 │
│             [LOGO]        [Dupont Circle / 14th & U]           │
│                           Coverage Initiative                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Alternate Headlines (A/B Test)

| Version | Headline |
|---------|----------|
| A (default) | FREE MOBILE COVERAGE UPGRADE FOR YOUR BUSINESS |
| B | GET FREE HARDWARE THAT HELPS YOUR CUSTOMERS |
| C | YOUR BUSINESS. BETTER SIGNAL. NO COST. |
| D | FREE WIFI BOOST FOR [NEIGHBORHOOD] BUSINESSES |

---

## Pamphlet Placement Strategy

| Location Type | Placement Method |
|---------------|------------------|
| Coffee shops | Leave 5-10 on counter (with permission) |
| Bulletin boards | Pin single copy with tear-off QR tabs |
| Restaurant host stands | Leave stack with host |
| Co-working spaces | Community board or front desk |
| Barber shops / salons | Waiting area magazine rack |
| Direct handoff | Scout hands to owner/manager during blitz |

**Do NOT:**
- Leave on cars (littering, low conversion)
- Tape to windows without permission
- Leave in mailboxes (federal violation)

---

# Part 2: QR Form Fields

## Form URL Structure

```
https://[domain].com/dc-coverage?zone=dupont
https://[domain].com/dc-coverage?zone=14th-u
```

Zone pre-populated from QR code to track source.

---

## Form Fields (Typeform or Tally Recommended)

### Section 1: Business Info (Required)

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `business_name` | Text | Yes | Min 2 chars |
| `business_address` | Address autocomplete | Yes | Must be in DC |
| `business_category` | Dropdown | Yes | See options below |
| `your_name` | Text | Yes | Min 2 chars |
| `your_role` | Dropdown | Yes | Owner, Manager, Employee, Other |

**Category dropdown options:**
- Coffee shop / Cafe
- Restaurant / Bar
- Fitness studio / Gym
- Salon / Barbershop
- Retail store
- Co-working / Office
- Laundromat
- Auto / Repair shop
- Other service business

---

### Section 2: Qualification Questions (Required)

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `decision_maker` | Yes/No | Yes | "Are you the person who makes decisions about equipment and vendors for this business?" |
| `landlord_permission` | Dropdown | Yes | "For exterior work, would you need landlord approval?" Options: No - I own/control the building, Yes - landlord approval needed, Not sure |
| `timeline` | Dropdown | Yes | "If you qualify, when could we schedule installation?" Options: This week, Next 2 weeks, This month, Not sure yet |

---

### Section 3: Site Details (Required)

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `square_footage` | Dropdown | Yes | "Roughly how big is your space?" Options: Small (<1,000 sq ft), Medium (1,000-3,000 sq ft), Large (3,000+ sq ft) |
| `outdoor_interest` | Yes/No/Maybe | Yes | "Would you be interested in an outdoor unit as well? (mounted on your building exterior)" |
| `corner_location` | Yes/No | Yes | "Is your business on a corner or at an intersection?" |

---

### Section 4: Contact (Required)

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `phone` | Phone | Yes | Valid US format |
| `email` | Email | Yes | Valid email |
| `contact_preference` | Dropdown | Yes | Options: Call, Text, Email |
| `best_time` | Dropdown | Yes | Options: Morning (9am-12pm), Afternoon (12-5pm), Evening (5-8pm), Anytime |

---

### Section 5: Optional (Bonus Info)

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| `wifi_available` | Yes/No/Not sure | No | "Does your business have WiFi we could connect the device to?" |
| `hours_of_operation` | Text | No | "What are your business hours?" |
| `notes` | Text area | No | "Anything else we should know?" |
| `how_heard` | Dropdown | No | "How did you hear about this?" Options: Pamphlet, Someone stopped by, Instagram, Friend/referral, Other |

---

## Form Completion Screen

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                         ✓ YOU'RE IN!                           │
│                                                                 │
│   Thanks for your interest, [First Name]!                      │
│                                                                 │
│   We'll review your info and reach out within 48 hours         │
│   to schedule a quick site visit.                              │
│                                                                 │
│   What happens next:                                           │
│   1. We'll call/text to confirm details                        │
│   2. Schedule a 15-minute site visit                           │
│   3. If it's a fit, we install your free hardware              │
│                                                                 │
│   Questions? Text us at (202) XXX-XXXX                         │
│                                                                 │
│   [Return to website]                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

# Part 3: Lead Scoring Rules

## Auto-Scoring Logic (0-100)

Every form submission is automatically scored based on responses:

### Decision-Maker Score (25 points max)

| Response | Points |
|----------|--------|
| `your_role` = Owner | 25 |
| `your_role` = Manager + `decision_maker` = Yes | 20 |
| `your_role` = Manager + `decision_maker` = No | 10 |
| `your_role` = Employee | 5 |
| `decision_maker` = Yes (any role) | +5 bonus |

---

### Category Score (20 points max)

| Category | Points | Tier |
|----------|--------|------|
| Coffee shop / Cafe | 20 | Tier 1 |
| Co-working / Office | 20 | Tier 1 |
| Fitness studio / Gym | 18 | Tier 1 |
| Restaurant / Bar | 18 | Tier 1 |
| Salon / Barbershop | 16 | Tier 1 |
| Retail store | 12 | Tier 2 |
| Laundromat | 12 | Tier 2 |
| Auto / Repair shop | 10 | Tier 3 |
| Other service business | 8 | Tier 3 |

---

### Outdoor Potential Score (20 points max)

| Factor | Points |
|--------|--------|
| `outdoor_interest` = Yes | 10 |
| `outdoor_interest` = Maybe | 5 |
| `outdoor_interest` = No | 0 |
| `corner_location` = Yes | 10 |
| `corner_location` = No | 0 |

---

### Permissioning Speed Score (20 points max)

| Factor | Points |
|--------|--------|
| `landlord_permission` = No (owner controls) | 15 |
| `landlord_permission` = Not sure | 8 |
| `landlord_permission` = Yes (needed) | 3 |
| `timeline` = This week | 5 |
| `timeline` = Next 2 weeks | 4 |
| `timeline` = This month | 2 |
| `timeline` = Not sure | 0 |

---

### Size & Reliability Score (15 points max)

| Factor | Points |
|--------|--------|
| `square_footage` = Small | 15 (efficient coverage) |
| `square_footage` = Medium | 12 |
| `square_footage` = Large | 8 |
| `wifi_available` = Yes | +3 bonus |
| `wifi_available` = Not sure | +1 |

---

### Zone Bonus (Separate Multiplier)

| Zone | Multiplier |
|------|------------|
| Priority zone (D1, D2, U1, U2) | 1.2x |
| Secondary zone (D3, D4, U3, U4) | 1.0x |
| Outside target zones | 0.5x (deprioritize) |

**Final Score Formula:**
```
raw_score = decision_maker_pts + category_pts + outdoor_pts + permissioning_pts + size_pts
final_score = raw_score × zone_multiplier
```

---

## Lead Tiers Based on Score

| Score | Tier | Action |
|-------|------|--------|
| 80-100 | HOT | Call within 4 hours |
| 60-79 | WARM | Call within 24 hours |
| 40-59 | COOL | Call within 48 hours |
| 20-39 | COLD | Email only, low priority |
| 0-19 | DISQUALIFY | Auto-reject (see rules below) |

---

## Auto-Disqualification Rules

**Immediately reject if ANY:**

| Rule | Condition |
|------|-----------|
| DQ-1 | Address outside DC |
| DQ-2 | Address outside target neighborhood boundaries |
| DQ-3 | `your_role` = Employee AND `decision_maker` = No |
| DQ-4 | Duplicate address (already in CRM) |
| DQ-5 | Phone number already submitted in last 30 days |
| DQ-6 | Business name matches known chain HQ |
| DQ-7 | Junk/test responses detected (e.g., "asdf", "test") |

**Auto-reject response:**
```
Thanks for your interest! Unfortunately, your business isn't in our
current coverage area. We'll let you know if that changes.
```

---

# Part 4: Routing Workflow

## Lead Assignment Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     LEAD ROUTING WORKFLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FORM SUBMITTED                                                 │
│       │                                                         │
│       ▼                                                         │
│  ┌─────────────────┐                                           │
│  │ AUTO-SCORING    │  Calculate 0-100 score                    │
│  │ (Instant)       │  Apply zone multiplier                    │
│  └────────┬────────┘  Check disqualification rules             │
│           │                                                     │
│       ┌───┴───┐                                                │
│       │       │                                                │
│   QUALIFIED  DISQUALIFIED                                      │
│       │           │                                            │
│       ▼           ▼                                            │
│  ┌─────────┐  ┌─────────┐                                      │
│  │ ASSIGN  │  │ AUTO    │                                      │
│  │ TO SDR  │  │ REJECT  │                                      │
│  └────┬────┘  │ EMAIL   │                                      │
│       │       └─────────┘                                      │
│       ▼                                                         │
│  ┌─────────────────┐                                           │
│  │ SDR FOLLOW-UP   │  Call/text based on tier                  │
│  │ (see cadence)   │  Qualify + schedule site visit            │
│  └────────┬────────┘                                           │
│           │                                                     │
│       ┌───┴───┐                                                │
│       │       │                                                │
│   QUALIFIED  NOT QUALIFIED                                     │
│       │           │                                            │
│       ▼           ▼                                            │
│  ┌─────────┐  ┌─────────┐                                      │
│  │ ASSIGN  │  │ NURTURE │  Add to monthly                     │
│  │ TO      │  │ LIST    │  email list                         │
│  │INSTALLER│  └─────────┘                                      │
│  └────┬────┘                                                   │
│       │                                                         │
│       ▼                                                         │
│  ┌─────────────────┐                                           │
│  │ SITE VISIT +    │  Installer confirms viability            │
│  │ INSTALL         │  Completes installation                   │
│  └────────┬────────┘                                           │
│           │                                                     │
│           ▼                                                     │
│  ┌─────────────────┐                                           │
│  │ VERIFICATION    │  72-hour hold                             │
│  │ + CLOSE         │  Host callback                            │
│  └─────────────────┘  Mark as INSTALLED                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## SDR Assignment Rules

**SDRs (Sales Development Reps) handle initial follow-up before installer routing.**

| Zone | Assigned SDR | Backup |
|------|--------------|--------|
| Dupont Circle (D1-D4) | SDR-1 | SDR-3 |
| 14th St + U St (U1-U4) | SDR-2 | SDR-3 |

**SDR responsibilities:**
1. Call/text lead within SLA (based on tier)
2. Confirm business info and decision-maker
3. Pre-qualify for indoor/outdoor
4. Schedule site visit with installer
5. Hand off to installer with notes

**SDR does NOT:**
- Perform installations
- Make final qualification decisions
- Promise specific hardware

---

## Installer Assignment Rules

**After SDR qualification, leads are assigned to installers.**

### Assignment Logic

| Factor | Assignment Rule |
|--------|-----------------|
| **Zone-based** | Installer assigned to specific micro-zones |
| **Load balancing** | Installer with fewest pending installs gets next lead |
| **Skill match** | Outdoor-capable installers get outdoor-flagged leads |
| **Capacity cap** | No installer gets >10 pending leads at once |

### Installer Roster Example

| Installer | Zones | Outdoor Certified | Max Pending |
|-----------|-------|-------------------|-------------|
| Installer-1 | D1, D2 | Yes | 10 |
| Installer-2 | D3, D4 | No | 8 |
| Installer-3 | U1, U2 | Yes | 10 |
| Installer-4 | U3, U4 | Yes | 8 |
| Installer-5 | All (backup) | Yes | 5 |

---

## CRM Pipeline Stages

| Stage | Owner | Exit Criteria |
|-------|-------|---------------|
| `New Lead` | System | Auto-scored, assigned to SDR |
| `Contacted` | SDR | Spoke to lead, confirmed interest |
| `Qualified` | SDR | DM confirmed, site visit scheduled |
| `Site Visit Scheduled` | Installer | Appointment on calendar |
| `Site Visit Complete` | Installer | Viability confirmed, install scheduled |
| `Install Scheduled` | Installer | Install date/time confirmed |
| `Installed` | Installer | Hardware live, photos submitted |
| `Verified` | System | 72hr uptime + host callback passed |
| `Closed Won` | System | Complete, commission processed |
| `Closed Lost` | SDR/Installer | Reason logged (declined, unqualified, etc.) |

---

# Part 5: Follow-Up Cadence (7-Day Conversion)

## Cadence by Lead Tier

### HOT Leads (Score 80-100)

| Day | Time | Action | Channel | Script/Note |
|-----|------|--------|---------|-------------|
| 0 | Within 4 hrs | Call #1 | Phone | "Just got your form, wanted to connect right away..." |
| 0 | +2 hrs if no answer | Text #1 | SMS | "Hi [Name], this is [SDR] following up on your coverage request..." |
| 1 | Morning | Call #2 | Phone | "Following up from yesterday..." |
| 1 | Afternoon | Email #1 | Email | Recap + value prop |
| 2 | Morning | Text #2 | SMS | "Quick question: what time works best for a call today?" |
| 3 | Morning | Call #3 | Phone | Final call attempt |
| 3 | Afternoon | Email #2 | Email | "Did we miss you?" + easy booking link |
| 5 | Morning | Text #3 | SMS | "Last check-in - still interested?" |
| 7 | Morning | Email #3 | Email | "Closing out your request" - creates urgency |

**Target:** Schedule site visit by Day 3, install by Day 7

---

### WARM Leads (Score 60-79)

| Day | Time | Action | Channel |
|-----|------|--------|---------|
| 0 | Within 24 hrs | Call #1 | Phone |
| 1 | Morning | Text #1 | SMS |
| 2 | Morning | Call #2 | Phone |
| 2 | Afternoon | Email #1 | Email |
| 4 | Morning | Text #2 | SMS |
| 5 | Morning | Call #3 | Phone |
| 7 | Morning | Email #2 | Email (final) |

**Target:** Schedule site visit by Day 5, install by Day 10

---

### COOL Leads (Score 40-59)

| Day | Time | Action | Channel |
|-----|------|--------|---------|
| 0 | Within 48 hrs | Email #1 | Email |
| 2 | Morning | Call #1 | Phone |
| 4 | Morning | Text #1 | SMS |
| 6 | Morning | Email #2 | Email |
| 7 | Morning | Call #2 | Phone (final) |

**Target:** Schedule site visit by Day 7, install by Day 14

---

### COLD Leads (Score 20-39)

| Day | Action | Channel |
|-----|--------|---------|
| 1 | Email #1 | Email |
| 5 | Email #2 | Email |
| 14 | Add to nurture list | — |

**No phone calls.** Low likelihood of conversion.

---

## Message Templates

### Text #1 (Immediate)

```
Hi [Name]! This is [SDR] from the DC Coverage Initiative. Just got
your request for free connectivity hardware at [Business Name].

Quick question: are you available for a 5-min call today to confirm
a few details? I can call anytime that works for you.
```

---

### Call Script (First Call)

```
"Hi [Name], this is [SDR] from the DC Coverage Initiative. I'm
following up on the form you filled out for [Business Name].

First off — thanks for your interest! I just have a few quick
questions to make sure we can get you set up.

1. You're the [owner/manager] — are you the person who makes
   decisions about equipment for the business? [CONFIRM]

2. Your space is about [size from form] — does that sound right?
   [CONFIRM]

3. You mentioned you'd be interested in an outdoor unit too —
   is your building something you own or lease? [CONFIRM]

Great. Based on what you've told me, [Business Name] looks like a
great fit. Here's what happens next:

We'll send one of our installers to do a quick 10-minute site visit
— just to confirm placement and make sure everything works. Then we
schedule the actual install, which takes about 15-20 minutes.

What day this week works best for that site visit?"
```

---

### Email #1 (Value Recap)

**Subject:** Your free coverage hardware request - next steps

```
Hi [Name],

Thanks for submitting your request for free mobile coverage hardware
at [Business Name]!

I tried calling earlier but missed you. Here's a quick recap of
what we're offering:

FREE HARDWARE (yours to keep):
• Indoor unit — improves cell signal inside your business
• Outdoor unit — extends coverage to the sidewalk and block

ZERO COST:
• No monthly fees
• No contracts
• Professional installation included

NEXT STEP:
We just need a quick 10-minute site visit to confirm placement. Then
we schedule the install at a time that works for you.

Can you reply with 2-3 times that work for a quick call or visit
this week?

Best,
[SDR Name]
[Phone]
```

---

### Text #2 (Day 2-3)

```
Hey [Name], following up on the coverage hardware for [Business Name].

What's the best time for a quick 10-min site visit this week? We can
work around your schedule.
```

---

### Email #3 (Urgency/Close Out)

**Subject:** Closing your coverage request

```
Hi [Name],

I've tried reaching you a few times about the free coverage hardware
for [Business Name].

We're wrapping up our current rollout in [Dupont Circle / 14th St]
and I want to make sure you don't miss out.

If you're still interested, just reply "YES" and I'll prioritize
getting you scheduled.

If the timing isn't right, no worries at all — just let me know and
I'll close out your request.

Thanks,
[SDR Name]
```

---

## Conversion Benchmarks

| Metric | Target |
|--------|--------|
| Lead → Contacted (within SLA) | 90% |
| Contacted → Qualified | 50% |
| Qualified → Site Visit Scheduled | 70% |
| Site Visit → Install Scheduled | 80% |
| Install Scheduled → Installed | 90% |
| Installed → Verified | 95% |

**Overall funnel:** 100 QR leads → 50 contacted → 25 qualified → 18 site visits → 14 installs → 13 verified

---

## Weekly QR Lead Report

```
┌─────────────────────────────────────────────────────────────────┐
│              QR LEAD REPORT — Week of Jan 20                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SUBMISSIONS                                                    │
│  ───────────                                                    │
│  Total form submissions:           47                           │
│  Auto-disqualified:                 8 (17%)                     │
│  Qualified leads:                  39 (83%)                     │
│                                                                 │
│  BY TIER                                                        │
│  ───────                                                        │
│  HOT (80-100):    12 (31%)                                     │
│  WARM (60-79):    15 (38%)                                     │
│  COOL (40-59):     9 (23%)                                     │
│  COLD (20-39):     3 (8%)                                      │
│                                                                 │
│  BY ZONE                                                        │
│  ───────                                                        │
│  Dupont Circle:   18 (D1: 8, D2: 5, D3: 3, D4: 2)              │
│  14th/U St:       21 (U1: 10, U2: 7, U3: 3, U4: 1)             │
│                                                                 │
│  CONVERSION                                                     │
│  ──────────                                                     │
│  Contacted:        35 / 39 (90%)                               │
│  Qualified:        22 / 35 (63%)                               │
│  Site visits done: 14 / 22 (64%)                               │
│  Installs complete: 9 / 14 (64%)                               │
│  Verified:          8 / 9  (89%)                               │
│                                                                 │
│  TOP PAMPHLET LOCATIONS                                        │
│  ──────────────────────                                         │
│  1. Compass Coffee (Dupont) — 6 scans, 4 qualified             │
│  2. Yoga District (14th St) — 4 scans, 3 qualified             │
│  3. Bulletin board (U St) — 3 scans, 2 qualified               │
│                                                                 │
│  ISSUES                                                        │
│  ──────                                                        │
│  - 3 leads outside zone boundaries (pamphlet spread?)          │
│  - 2 duplicate submissions (same phone number)                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Pamphlet Tracking

Each pamphlet batch gets a unique QR code:

| QR Code ID | Location Placed | Zone | Date Placed | Scans | Conversions |
|------------|-----------------|------|-------------|-------|-------------|
| QR-D1-001 | Compass Coffee counter | D1 | Jan 15 | 12 | 4 |
| QR-D1-002 | Kramerbooks bulletin | D1 | Jan 15 | 6 | 2 |
| QR-D2-001 | JR's Bar counter | D2 | Jan 16 | 8 | 3 |
| QR-U1-001 | Busboys & Poets | U1 | Jan 16 | 15 | 5 |
| QR-U2-001 | U St bulletin board | U2 | Jan 17 | 4 | 1 |

**Tracking URL format:**
```
https://[domain].com/dc-coverage?zone=dupont&src=QR-D1-001
```

This lets you measure which placement locations drive the best leads.
