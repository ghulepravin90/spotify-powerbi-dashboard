# Spotify Power BI Dashboard - Visual Design & Wireframe Guide

This guide gives the layout, visual choices, formatting parameters, and color themes needed to build a polished Spotify-themed dashboard.

---

## 1. Visual Theme & Palette (Spotify Dark Mode)

To match the authentic Spotify branding:
- **Canvas Background:** `#121212` (Spotify Dark Neutral)
- **Card / Visual Container Fill:** `#181818` (Card Dark Grey)
- **Container Border:** `#282828` (Subtle boundary line, 1px rounded corner radius 8px)
- **Primary Accent / Highlight:** `#1DB954` (Spotify Electric Green)
- **Secondary Accent:** `#1ED760` (Light Green) or `#38EF7D`
- **Contrast Accent (Explicit / Singles):** `#FF4B4B` (Coral Red) or `#A855F7` (Purple)
- **Primary Text:** `#FFFFFF` (White)
- **Secondary / Label Text:** `#B3B3B3` (Light Silver Grey)
- **Gridlines & Dividers:** `#333333`

---

## 2. Canvas Layout Structure (16:9 Aspect Ratio)

```
+---------------------------------------------------------------------------------------------------------------+
|  [LOGO] SPOTIFY STREAMING & MUSIC INTELLIGENCE DASHBOARD                       Last Refreshed: [Dynamic Date] |
+---------------------------------------------------------------------------------------------------------------+
|  SLICERS BAR: [ Year: All v ]  [ Month: All v ]  [ Genre: All v ]  [ Track Type: All v ]  [ Explicit: All v ]  |
+---------------------------------------------------------------------------------------------------------------+
|  KPI CARDS ROW:                                                                                               |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+               |
|  |   TOTAL STREAMS    |  |    TOTAL TRACKS    |  |   TOTAL ARTISTS    |  |   AVG POPULARITY   |               |
|  |     674.8 B        |  |       1,000        |  |        115         |  |        82.4        |               |
|  |   MoM: +6.4% ^     |  |   Singles: 32%     |  |   Top: The Weeknd  |  |   Benchmark: 80+   |               |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+               |
+---------------------------------------------------------------------------------------------------------------+
|  MAIN VISUAL SECTION:                                                                                         |
|  +---------------------------------------------+  +--------------------------------------------------------+  |
|  | [VISUAL 1: AREA / LINE CHART]               |  | [VISUAL 2: DONUT / 100% STACKED BAR]                   |  |
|  | Monthly Listener Trends & Streams           |  | Album Tracks vs Singles Share                          |  |
|  | (X: Dim_Calendar[MonthYear], Y: Total Streams|  | (Values: [Album Stream Share %], [Single Stream Share %|  |
|  | Tooltip: MoM Growth %, Tracks Released)     |  |  Legend: Album Track (68%), Single (32%))              |  |
|  +---------------------------------------------+  +--------------------------------------------------------+  |
|                                                                                                               |
|  +---------------------------------------------+  +--------------------------------------------------------+  |
|  | [VISUAL 3: HORIZONTAL CLUSTERED BAR]        |  | [VISUAL 4: STACKED BAR / DONUT]                        |  |
|  | Top 10 Artists by Total Streams             |  | Explicit vs Non-Explicit Content Comparison            |  |
|  | (Y: artist_name, X: Total Streams)          |  | (Streams & Popularity by Explicit Status)              |  |
|  | Highlight: Top 1 (The Weeknd / Taylor Swift)|  | Explicit: 37% Vol | Non-Explicit: 63% Vol              |  |
|  +---------------------------------------------+  +--------------------------------------------------------+  |
|                                                                                                               |
|  +---------------------------------------------------------------------------------------------------------+  |
|  | [VISUAL 5: SCATTER / MATRIX PLOT]                                                                       |  |
|  | Audio Energy vs. Danceability Correlation (Bubble Size: Total Streams, Color: Genre)                   |  |
|  +---------------------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------------------+
```

---

## 3. Step-by-Step Visual Configurations

### Visual 1: Slicer Bar (Top Ribbon)
- **Visual Type:** Slicer (Button / Dropdown style)
- **Fields:**
  1. `Dim_Calendar[Year]` -> Dropdown / Tile
  2. `Dim_Calendar[MonthName]` -> Dropdown (Ensure sorted by MonthNumber)
  3. `spotify_tracks_data[genre]` -> Dropdown
  4. `spotify_tracks_data[track_type]` -> Tile ("Album Track" | "Single")
  5. `spotify_tracks_data[is_explicit]` -> Tile ("Explicit" | "Non-Explicit")

### Visual 2: KPI Summary Cards (New Card Visual)
- **Visual Type:** Card (New)
- **Cards configured:**
  1. **Card 1:** Measure `[Total Streams Formatted]`. Subtitle: "MoM Growth" with measure `[MoM Stream Growth %]`.
  2. **Card 2:** Measure `[Total Tracks]`. Subtitle: "Active Catalog".
  3. **Card 3:** Measure `[Total Artists]`. Subtitle: "Unique Creators".
  4. **Card 4:** Measure `[Avg Popularity]`. Subtitle: "Out of 100".
- **Formatting:** Font color: `#1DB954` (Green) for primary values; `#FFFFFF` for titles; `#B3B3B3` for subtitles.

### Visual 3: Monthly Listener Streaming Trends (Area Chart / Line Chart)
- **Visual Type:** Area Chart
- **X-Axis:** `Dim_Calendar[MonthYear]` (Sorted by `MonthYearSort`)
- **Y-Axis:** `[Total Streams]`
- **Secondary Y-Axis / Tooltips:** `[MoM Stream Growth %]`, `[Tracks Released]`
- **Stroke Color:** `#1DB954` with smooth gradient area fill (`#1DB954` at 40% transparency to 0%).

### Visual 4: Album Tracks vs. Singles Breakdown (Donut Chart)
- **Visual Type:** Donut Chart
- **Legend:** `spotify_tracks_data[track_type]`
- **Values:** `[Total Streams]`
- **Detail Labels:** Data value & percent of total.
- **Colors:**
  - Album Track: `#1DB954` (Spotify Green)
  - Single: `#A855F7` (Electric Violet)
- **Key Business Story:** Explains how albums carry catalog depth while singles drive short-term spike velocity.

### Visual 5: Explicit vs. Non-Explicit Comparison (Clustered Column or 100% Stacked Bar)
- **Visual Type:** Clustered Column Chart
- **X-Axis:** `spotify_tracks_data[genre]`
- **Y-Axis:** `[Total Streams]`
- **Legend:** `spotify_tracks_data[is_explicit]`
- **Colors:**
  - Explicit: `#FF4B4B` (Red)
  - Non-Explicit: `#22C55E` (Emerald Green)
- **Key Business Story:** Shows Hip-Hop is over 70% explicit, while Pop & Acoustic genres are predominantly clean.

### Visual 6: Top 10 Artists Leaderboard (Clustered Bar Chart)
- **Visual Type:** Clustered Bar Chart (Horizontal)
- **Y-Axis:** `spotify_tracks_data[artist_name]`
- **X-Axis:** `[Total Streams]`
- **Data Labels:** ON (Display units: Billions `0.00 B`)
- **Visual Filter:** Filter type: `Top N` -> Show top `10` by `[Total Streams]`.

---

## 4. Polishing & User Experience (UX)

1. **Tooltips Page (Report Page Tooltip):**
   - Create a hidden 320x240 px canvas named `Artist_Tooltip`.
   - Add mini cards showing: Artist's top track name, total tracks in catalog, and avg popularity.
   - Connect it to the Top 10 Artists visual so hovering over any artist displays immediate rich context.

2. **Reset Filters Button:**
   - Add a bookmark capturing default unfiltered state.
   - Insert a button: **Insert** > **Buttons** > **Reset**.
   - Assign Action: Bookmark -> "Default State".
