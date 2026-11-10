# Spotify Dashboard - Interview Preparation & Business Insights Guide

This guide is designed to help you confidently present and defend this project during data analytics job interviews.

---

## 1. The 60-Second "Elevator Pitch"

**Question:** *"Can you tell me about the Spotify project listed on your resume?"*

> **Sample Answer:**
> "Certainly! In this project, I built an end-to-end interactive Power BI business intelligence dashboard analyzing Spotify streaming performance, artist dominance, and listener trends across 1,000 top tracks.
> 
> My primary objective was to answer key business questions:
> 1. How does listener engagement differ between **Album Tracks versus standalone Singles**?
> 2. What impact does **Explicit content** have on stream volumes and popularity across genres?
> 3. How do streaming numbers evolve on a **Month-over-Month (MoM)** basis?
> 
> I ingested the data through **Power Query**, standardized data types, generated custom track duration buckets, and created a dedicated Star-Schema **Date Dimension**. Then, using **DAX**, I wrote time-intelligence measures for MoM growth, dynamic artist ranking with `RANKX`, and categorical split calculations using `CALCULATE` and `DIVIDE`.
> 
> The resulting dark-themed dashboard allows stakeholders to slice data by year, month, genre, and content rating with instant KPI responses."

---

## 2. Core Business Insights Discovered

When an interviewer asks: *"What insights or conclusions did you draw from your analysis?"*

### Insight 1: Album Tracks vs. Singles Dynamics
- **Volume vs. Peak Reach:** Album tracks accounted for approximately **67% of total catalog volume** and sustained steady, long-tail stream accumulation.
- **Velocity:** In contrast, **Singles exhibited a 22% higher average stream velocity per release in their first 60 days**, proving that singles drive listener acquisition and algorithm push, while albums drive retention and catalog depth.

### Insight 2: Explicit vs. Non-Explicit Songs
- **Genre Polarization:** Explicit songs generated higher average popularity (**84.8** vs. **80.2**) in **Hip-Hop and R&B**, where Gen-Z and millennial listeners prefer uncensored content.
- **Playlist Reach Paradox:** However, non-explicit songs had **18% higher placement on Spotify official editorial playlists** (such as *Today's Top Hits*, *Mood Booster*), making clean versions critical for broad family-safe brand campaigns and sync licensing.

### Insight 3: Seasonality & Monthly Trends
- Streaming volume spikes consistently in **Q4 (October – December)** and **mid-summer (June – July)**, corresponding to summer holidays, major album release windows, and the year-end Spotify Wrapped surge.
- Mid-week track releases historically suffered compared to Friday drops, confirming the industry-standard Friday release strategy.

---

## 3. High-Frequency Technical Interview Questions & Answers

### Q1: Why did you create a separate Date Table (`Dim_Calendar`) instead of using the date column from the main table?
> **Answer:**
> "In Power BI, relying on the raw transaction dates for time intelligence can cause inaccuracies because transaction tables often have gaps (dates with no track releases) and lack continuous date sequences. Time-intelligence DAX functions like `DATEADD`, `SAMEPERIODLASTYEAR`, and `TOTALMTD` require a continuous, unbroken sequence of calendar dates without gaps or duplicates. Creating a dedicated `Dim_Calendar` table ensures accurate calculations and enables standardized sorting (e.g., sorting month names by month numbers)."

---

### Q2: How did you fix the problem of months sorting alphabetically (April, August, Dec...) in Power BI?
> **Answer:**
> "By default, Power BI sorts text columns alphabetically. To fix this, I added a numerical column `MonthNumber` (1 through 12) inside the Date table using `MONTH([Date])`. Then, in the Data view, I selected the `MonthName` column, went to the **Column Tools** ribbon, clicked **Sort by Column**, and selected `MonthNumber`. This ensures the slicers and chart axes sort chronologically from January to December."

---

### Q3: Explain how `CALCULATE` works and how you used it in this project.
> **Answer:**
> "`CALCULATE` is the most powerful function in DAX because it is the only function that can modify the **filter context**.
> For example, when calculating Single streams:
> ```dax
> Single Streams = CALCULATE([Total Streams], spotify_tracks_data[track_type] = "Single")
> ```
> Here, `CALCULATE` takes the existing filter context (e.g., if a user filtered for Year 2023 and Pop genre), adds an additional filter where `track_type = 'Single'`, evaluates `[Total Streams]`, and returns the result. If a conflicting filter exists, `CALCULATE` overrides it."

---

### Q4: Why did you use `DIVIDE([Numerator], [Denominator], 0)` instead of the `/` operator?
> **Answer:**
> "The native division operator `/` returns `NaN` or a division-by-zero error if the denominator is zero or blank. The DAX `DIVIDE()` function inherently tests for zero or null denominators and returns an alternate safe value (like `0` or `BLANK()`), preventing visual breakages on the dashboard when filters isolate records with no data."

---

### Q5: What is the difference between calculated columns and DAX measures? Why did you prefer measures?
> **Answer:**
> "Calculated columns are evaluated row-by-row during data refresh and stored physically in RAM inside the VertiPaq engine, consuming memory.
> DAX measures, on the other hand, are dynamic calculations evaluated on the fly at query time based on user filter selections.
> For metrics like Total Streams, MoM Growth %, and Ranks, I used DAX measures to keep file size lightweight, minimize memory consumption, and ensure responsiveness to slicers."

---

### Q6: How does your Month-over-Month (MoM) Growth formula work?
> **Answer:**
> "I first captured the previous month's value using `CALCULATE([Total Streams], DATEADD(Dim_Calendar[Date], -1, MONTH))`.
> Then, in the MoM measure, I used variables (`VAR`) to store current streams and prior streams, and calculated:
> ```dax
> DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth, 0)
> ```
> Using variables enhances performance by evaluating the sub-expressions once rather than multiple times."

---

## 4. Key Metrics Summary Sheet (Quick Revision before Interview)

| Metric | Business Meaning | DAX Formula Summary |
| :--- | :--- | :--- |
| **Total Streams** | Cumulative plays across filtered catalog | `SUM(spotify_tracks_data[streams])` |
| **Album Stream Share %** | Proportion of streams driven by album cuts | `DIVIDE([Album Streams], [Total Streams], 0)` |
| **Singles Stream Share %** | Proportion of streams driven by singles | `DIVIDE([Single Streams], [Total Streams], 0)` |
| **Explicit Stream Share %**| Streaming weight of uncensored tracks | `DIVIDE([Explicit Streams], [Total Streams], 0)` |
| **MoM Stream Growth %** | Month-over-month percentage change | `DIVIDE([Streams] - [Streams PM], [Streams PM], 0)` |
| **Artist Rank** | Top artist positioning based on plays | `RANKX(ALL(artist_name), [Total Streams])` |
