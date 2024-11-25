# Question: Online Extraction vs Offline Extraction

## Online Extraction
- Occurs in **real-time** or **near real-time**
- Pulls data from the source system when new data arrive
- Used in scenarios when timely data is critical
- **Source connection**: 
### Advantages
- Provides up-to-date data for downstream processes
### Challenges
- High demand on source systems, potentially impacting their performance
- Complexity in handling real-time updates, errors, and partial data
- Requires robust infrastructure to process streaming data efficiently

## Offline Extraction
- Offline extraction retrieves data in **batch** mode, typically at scheduled intervals (e.g., hourly, nightly). 
- The data is often read from a snapshot or a backup of the source system, minimizing the impact on live operations.
### Advantages
- Reduced load on the source system during business hours.
- Simplified implementation, as data is processed in bulk.


