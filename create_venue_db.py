#!/usr/bin/env python3
"""
Create SQLite database from venue CSV for Superset integration.
"""

import csv
import sqlite3


def get_priority_tier(score):
    """Convert numeric score to priority tier."""
    if score >= 85:
        return "Priority"
    elif score >= 60:
        return "High"
    elif score >= 45:
        return "Medium"
    else:
        return "Low"


def main():
    db_path = "venues.db"
    csv_path = "dc-venues.csv"

    # Connect to SQLite (creates file if doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Drop existing table if present
    cursor.execute("DROP TABLE IF EXISTS venues")

    # Create venues table
    cursor.execute("""
        CREATE TABLE venues (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT,
            category TEXT,
            neighborhood TEXT,
            rating REAL,
            reviews INTEGER,
            price TEXT,
            score INTEGER,
            priority_tier TEXT,
            lat REAL,
            lng REAL,
            phone TEXT,
            yelp_id TEXT
        )
    """)

    # Read CSV and insert rows
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows_inserted = 0

        for row in reader:
            score = int(row["Score"]) if row["Score"] else 0
            priority_tier = get_priority_tier(score)

            cursor.execute("""
                INSERT INTO venues (
                    id, name, address, category, neighborhood,
                    rating, reviews, price, score, priority_tier,
                    lat, lng, phone, yelp_id
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["ID"],
                row["Name"],
                row["Address"],
                row["Category"],
                row["Neighborhood"],
                float(row["Rating"]) if row["Rating"] else None,
                int(row["Reviews"]) if row["Reviews"] else None,
                row["Price"] or None,
                score,
                priority_tier,
                float(row["Lat"]) if row["Lat"] else None,
                float(row["Lng"]) if row["Lng"] else None,
                row["Phone"] or None,
                row["YelpID"]
            ))
            rows_inserted += 1

    conn.commit()

    # Create indexes for common queries
    cursor.execute("CREATE INDEX idx_score ON venues(score DESC)")
    cursor.execute("CREATE INDEX idx_priority_tier ON venues(priority_tier)")
    cursor.execute("CREATE INDEX idx_neighborhood ON venues(neighborhood)")
    cursor.execute("CREATE INDEX idx_category ON venues(category)")

    conn.commit()

    # Print summary
    print(f"Database created: {db_path}")
    print(f"Total venues: {rows_inserted}")

    # Show breakdown
    cursor.execute("SELECT priority_tier, COUNT(*) FROM venues GROUP BY priority_tier ORDER BY score DESC")
    print("\nBy Priority Tier:")
    for tier, count in cursor.fetchall():
        print(f"  {tier}: {count}")

    cursor.execute("SELECT neighborhood, COUNT(*) FROM venues GROUP BY neighborhood ORDER BY COUNT(*) DESC")
    print("\nBy Neighborhood:")
    for hood, count in cursor.fetchall():
        print(f"  {hood}: {count}")

    cursor.execute("SELECT category, COUNT(*) FROM venues GROUP BY category ORDER BY COUNT(*) DESC")
    print("\nBy Category:")
    for cat, count in cursor.fetchall():
        print(f"  {cat}: {count}")

    conn.close()
    print(f"\nDone! Connect Superset to: {db_path}")


if __name__ == "__main__":
    main()
