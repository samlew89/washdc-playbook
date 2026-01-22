cat > WORKPLAN.md <<'EOF'
# WORKPLAN.md — DC Hyper-Density Deployment Dashboard

## Project Goal
Create a highly readable, operator-friendly dashboard for driving hyper-dense Helium Mobile hotspot deployments in Washington DC, focused on:
- Dupont Circle
- 14th St NW + U St Corridor (Logan Circle / Shaw edge)

The dashboard should prioritize:
- Venue lead generation + qualification
- Dense clustering within defined pods/zones
- Clear "what to do next" for outreach + installs
- Hardware planning tied to venue pipeline

## Immediate Workstream: Improve Lead Lists + Pipeline Tab (Readability)
### Required New Section Order
1) Interactive Density Map
2) Priority Venues (Top 50, score 85+)
3) Dupont Circle Venues (collapsible, searchable)
4) 14th St + U St Corridor Venues (collapsible, searchable)
5) Hardware Required

### Remove These Sections
- Data Files section
- Quick Stats by Stage section

### Make Pod/Zone Labels Human Readable
Do not show raw codes in the UI.
Use:
- D1 = Dupont - Connecticut Ave
- D2 = Dupont - 17th St Strip
- D3 = Dupont - Dupont Ring
- D4 = Dupont - P St / 20th
- U1 = 14th/U - 14th St Main
- U2 = 14th/U - U St Corridor
- U3 = 14th/U - Shaw / 9th St
- U4 = 14th/U - V/W / Columbia Heights

### Scoring Transparency
Add "How scoring works" plus per-venue score breakdown.
Show the real weights from the scoring function in the repo.

## Definition of Done
- Map remains top
- Priority list then neighborhood lists
- No pod codes shown as primary labels
- Scoring is understandable and transparent
- App runs cleanly
EOF


