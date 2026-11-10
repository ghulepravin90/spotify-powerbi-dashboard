# Spotify Dashboard - Complete DAX Measures & Formulas

This document contains all Data Analysis Expressions (DAX) used in the **Spotify Audio & Streaming Analytics Dashboard**.

---

## 1. Dedicated Date Dimension Table (`Dim_Calendar`)

In Power BI, best practice requires creating a dedicated Date Table for time intelligence functions (`DATEADD`, `TOTALMTD`, `SAMEPERIODLASTYEAR`).

Go to **Modeling** -> **New Table** and paste:

```dax
Dim_Calendar = 
ADDCOLUMNS (
    CALENDAR ( DATE(2020, 1, 1), DATE(2024, 12, 31) ),
    "Year", YEAR ( [Date] ),
    "MonthNumber", MONTH ( [Date] ),
    "MonthName", FORMAT ( [Date], "mmm" ),
    "MonthYear", FORMAT ( [Date], "mmm yyyy" ),
    "MonthYearSort", YEAR ( [Date] ) * 100 + MONTH ( [Date] ),
    "Quarter", "Q" & FORMAT ( [Date], "q" ),
    "YearQuarter", YEAR ( [Date] ) & " - Q" & FORMAT ( [Date], "q" )
)
```

> **Important Configuration in Power BI:**
> 1. Select the `MonthName` column in `Dim_Calendar`.
> 2. Click **Column Tools** > **Sort by Column** > select `MonthNumber`.
> 3. Select the `MonthYear` column > **Sort by Column** > select `MonthYearSort`.
> 4. In Model View, create a **1-to-many relationship** from `Dim_Calendar[Date]` to `spotify_tracks_data[release_date]`.

---

## 2. Core Volume & Reach KPI Measures

Create a dedicated measure table: **Home** > **Enter Data** > Name it `_Measures`. Then right-click `_Measures` and select **New Measure**.

### Total Streams
```dax
Total Streams = 
SUM ( spotify_tracks_data[streams] )
```

### Total Streams (Formatted for KPI Cards: Billions / Millions)
```dax
Total Streams Formatted = 
VAR StreamsValue = [Total Streams]
RETURN
    SWITCH (
        TRUE (),
        StreamsValue >= 1000000000, FORMAT ( StreamsValue / 1000000000, "0.00" ) & " B",
        StreamsValue >= 1000000, FORMAT ( StreamsValue / 1000000, "0.0" ) & " M",
        StreamsValue >= 1000, FORMAT ( StreamsValue / 1000, "0.0" ) & " K",
        FORMAT ( StreamsValue, "#,##0" )
    )
```

### Total Tracks
```dax
Total Tracks = 
COUNTROWS ( spotify_tracks_data )
```

### Total Artists
```dax
Total Artists = 
DISTINCTCOUNT ( spotify_tracks_data[artist_name] )
```

### Average Popularity
```dax
Avg Popularity = 
ROUND ( AVERAGE ( spotify_tracks_data[popularity] ), 1 )
```

### Average Streams Per Track
```dax
Avg Streams per Track = 
DIVIDE ( [Total Streams], [Total Tracks], 0 )
```

### Total In Playlists
```dax
Total Playlist Adds = 
SUM ( spotify_tracks_data[in_spotify_playlists] )
```

---

## 3. Album Tracks vs. Singles Analysis

These measures fulfill the resume requirement: *"Compared album tracks vs. singles"*.

### Album Tracks Count
```dax
Album Tracks Count = 
CALCULATE (
    [Total Tracks],
    spotify_tracks_data[track_type] = "Album Track"
)
```

### Singles Count
```dax
Singles Count = 
CALCULATE (
    [Total Tracks],
    spotify_tracks_data[track_type] = "Single"
)
```

### Album Streams
```dax
Album Streams = 
CALCULATE (
    [Total Streams],
    spotify_tracks_data[track_type] = "Album Track"
)
```

### Single Streams
```dax
Single Streams = 
CALCULATE (
    [Total Streams],
    spotify_tracks_data[track_type] = "Single"
)
```

### Album Stream Share %
```dax
Album Stream Share % = 
DIVIDE ( [Album Streams], [Total Streams], 0 )
```
*(Format as Percentage `%` with 1 decimal place)*

### Single Stream Share %
```dax
Single Stream Share % = 
DIVIDE ( [Single Streams], [Total Streams], 0 )
```
*(Format as Percentage `%` with 1 decimal place)*

### Average Streams - Album vs Single
```dax
Avg Streams per Album Track = 
DIVIDE ( [Album Streams], [Album Tracks Count], 0 )

Avg Streams per Single = 
DIVIDE ( [Single Streams], [Singles Count], 0 )
```

---

## 4. Explicit vs. Non-Explicit Songs Analysis

These measures fulfill the resume requirement: *"Compared explicit vs. non-explicit songs"*.

### Explicit Tracks Count
```dax
Explicit Tracks Count = 
CALCULATE (
    [Total Tracks],
    spotify_tracks_data[is_explicit] = "Explicit"
)
```

### Non-Explicit Tracks Count
```dax
Non-Explicit Tracks Count = 
CALCULATE (
    [Total Tracks],
    spotify_tracks_data[is_explicit] = "Non-Explicit"
)
```

### Explicit Track %
```dax
Explicit Track Share % = 
DIVIDE ( [Explicit Tracks Count], [Total Tracks], 0 )
```
*(Format as Percentage `%`)*

### Explicit Streams
```dax
Explicit Streams = 
CALCULATE (
    [Total Streams],
    spotify_tracks_data[is_explicit] = "Explicit"
)
```

### Non-Explicit Streams
```dax
Non-Explicit Streams = 
CALCULATE (
    [Total Streams],
    spotify_tracks_data[is_explicit] = "Non-Explicit"
)
```

### Explicit Stream Share %
```dax
Explicit Stream Share % = 
DIVIDE ( [Explicit Streams], [Total Streams], 0 )
```

### Average Popularity: Explicit vs Non-Explicit
```dax
Avg Popularity Explicit = 
CALCULATE (
    [Avg Popularity],
    spotify_tracks_data[is_explicit] = "Explicit"
)

Avg Popularity Non-Explicit = 
CALCULATE (
    [Avg Popularity],
    spotify_tracks_data[is_explicit] = "Non-Explicit"
)
```

---

## 5. Monthly Listener Trends & Time-Intelligence Measures

These measures fulfill: *"Tracked listener trends by month with slicers and KPI cards"*.

### Streams Month-to-Date (MTD)
```dax
Streams MTD = 
TOTALMTD ( [Total Streams], Dim_Calendar[Date] )
```

### Streams Prior Month (MoM Base)
```dax
Streams Prior Month = 
CALCULATE (
    [Total Streams],
    DATEADD ( Dim_Calendar[Date], -1, MONTH )
)
```

### Month-over-Month (MoM) Stream Growth %
```dax
MoM Stream Growth % = 
VAR CurrentMonth = [Total Streams]
VAR PreviousMonth = [Streams Prior Month]
RETURN
    IF (
        ISBLANK ( PreviousMonth ) || PreviousMonth = 0,
        BLANK (),
        DIVIDE ( CurrentMonth - PreviousMonth, PreviousMonth, 0 )
    )
```
*(Format as Percentage `%`)*

### Tracks Released This Month
```dax
Tracks Released = 
CALCULATE (
    [Total Tracks],
    USERELATIONSHIP ( spotify_tracks_data[release_date], Dim_Calendar[Date] )
)
```

---

## 6. Dynamic Ranking & Top Performers

### Artist Rank by Streams
```dax
Artist Rank = 
IF (
    HASONEVALUE ( spotify_tracks_data[artist_name] ),
    RANKX (
        ALL ( spotify_tracks_data[artist_name] ),
        [Total Streams],
        ,
        DESC,
        DENSE
    )
)
```

### Track Rank by Streams
```dax
Track Rank = 
IF (
    HASONEVALUE ( spotify_tracks_data[track_name] ),
    RANKX (
        ALL ( spotify_tracks_data[track_name] ),
        [Total Streams],
        ,
        DESC,
        DENSE
    )
)
```

### Top 10 Artist Streams Filter
```dax
Is Top 10 Artist = 
IF ( [Artist Rank] <= 10, 1, 0 )
```

---

## 7. Audio Features Averages

Useful for radar charts, matrix visual, or scatter plots analyzing danceability, energy, and mood.

```dax
Avg Danceability % = 
ROUND ( AVERAGE ( spotify_tracks_data[danceability_%] ), 1 )

Avg Energy % = 
ROUND ( AVERAGE ( spotify_tracks_data[energy_%] ), 1 )

Avg Valence (Positivity) % = 
ROUND ( AVERAGE ( spotify_tracks_data[valence_%] ), 1 )

Avg BPM = 
ROUND ( AVERAGE ( spotify_tracks_data[bpm] ), 0 )

Avg Acousticness % = 
ROUND ( AVERAGE ( spotify_tracks_data[acousticness_%] ), 1 )
```
