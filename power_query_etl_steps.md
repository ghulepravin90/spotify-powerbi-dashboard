# Power Query ETL & Data Modeling Guide

This guide details the step-by-step ETL (Extract, Transform, Load) procedures performed in Power Query for the **Spotify Analytics Dashboard**.

---

## 1. Data Ingestion (Extract)

1. Open **Power BI Desktop**.
2. Click **Get Data** > **Text/CSV**.
3. Browse and select `spotify_tracks_data.csv`.
4. Click **Transform Data** (Do NOT click 'Load' immediately; always clean data first).

---

## 2. Power Query Data Cleaning Steps (Transform)

### Step 1: Promote Headers & Validate Column Names
Ensure row 1 is recognized as the header row:
- Under **Home** tab > click **Use First Row as Headers**.

### Step 2: Set Strict Data Types
Assign explicit data types to optimize compression and DAX calculation speed:

| Column Name | Target Data Type in Power Query | Reason |
| :--- | :--- | :--- |
| `track_id` | Text (`type text`) | Unique alphanumeric identifier |
| `track_name` | Text (`type text`) | Track title |
| `artist_name` | Text (`type text`) | Lead performing artist |
| `album_name` | Text (`type text`) | Album / Collection title |
| `release_date` | Date (`type date`) | Enables date joins and time-intelligence |
| `release_year` | Whole Number (`Int64.Type`) | Filter slicing |
| `release_month` | Whole Number (`Int64.Type`) | Numerical sort key |
| `release_month_name`| Text (`type text`) | Slicer display name |
| `release_day` | Whole Number (`Int64.Type`) | Calendar day |
| `genre` | Text (`type text`) | Categorical slicing |
| `track_type` | Text (`type text`) | "Album Track" vs "Single" |
| `is_explicit` | Text (`type text`) | "Explicit" vs "Non-Explicit" |
| `popularity` | Whole Number (`Int64.Type`) | Score 0 to 100 |
| `streams` | Whole Number (`Int64.Type`) | Global total plays |
| `in_spotify_playlists` | Whole Number (`Int64.Type`) | Playlist presence |
| `duration_ms` | Whole Number (`Int64.Type`) | Milliseconds |
| `duration_sec` | Whole Number (`Int64.Type`) | Seconds |
| `bpm` | Whole Number (`Int64.Type`) | Tempo |
| `danceability_%` | Whole Number (`Int64.Type`) | Audio metric (0-100) |
| `energy_%` | Whole Number (`Int64.Type`) | Audio metric (0-100) |
| `valence_%` | Whole Number (`Int64.Type`) | Audio metric (0-100) |
| `acousticness_%` | Whole Number (`Int64.Type`) | Audio metric (0-100) |
| `speechiness_%` | Whole Number (`Int64.Type`) | Audio metric (0-100) |

### Step 3: Remove Duplicates & Blank Rows
- Click the column header drop-down on `track_id` > **Remove Duplicates**.
- Check `track_name` and `artist_name` for null or blank entries. Power BI UI: **Remove Rows** > **Remove Blank Rows**.

### Step 4: Add Duration Category (Conditional Column)
To analyze streaming behavior by track length:
1. Go to **Add Column** tab > **Conditional Column**.
2. Name the column: `Track_Length_Category`.
3. Set conditions:
   - If `duration_sec` `<` `180` Then `Short (< 3 mins)`
   - Else If `duration_sec` `<=` `240` Then `Standard (3 - 4 mins)`
   - Else `Long (> 4 mins)`

### Step 5: Power Query Advanced Editor M Code Reference
If you prefer pasting the entire M transformation script:

```powerquery
let
    Source = Csv.Document(File.Contents("C:\Users\Pravin Ghule\Downloads\BT_Mini_Project\Spotify_PowerBI_Project\spotify_tracks_data.csv"),[Delimiter=",", Columns=23, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"track_id", type text}, 
        {"track_name", type text}, 
        {"artist_name", type text}, 
        {"album_name", type text}, 
        {"release_date", type date}, 
        {"release_year", Int64.Type}, 
        {"release_month", Int64.Type}, 
        {"release_month_name", type text}, 
        {"release_day", Int64.Type}, 
        {"genre", type text}, 
        {"track_type", type text}, 
        {"is_explicit", type text}, 
        {"popularity", Int64.Type}, 
        {"streams", Int64.Type}, 
        {"in_spotify_playlists", Int64.Type}, 
        {"duration_ms", Int64.Type}, 
        {"duration_sec", Int64.Type}, 
        {"bpm", Int64.Type}, 
        {"danceability_%", Int64.Type}, 
        {"energy_%", Int64.Type}, 
        {"valence_%", Int64.Type}, 
        {"acousticness_%", Int64.Type}, 
        {"speechiness_%", Int64.Type}
    }),
    #"Removed Duplicates" = Table.Distinct(#"Changed Type", {"track_id"}),
    #"Added Conditional Column" = Table.AddColumn(#"Removed Duplicates", "Track_Length_Category", each if [duration_sec] < 180 then "Short (< 3 mins)" else if [duration_sec] <= 240 then "Standard (3 - 4 mins)" else "Long (> 4 mins)", type text)
in
    #"Added Conditional Column"
```

---

## 3. Data Modeling & Relationships (Load)

After clicking **Close & Apply**:
1. Switch to **Model View** (icon on left navigation bar in Power BI).
2. Create the Date Table using the DAX script provided in `dax_measures.md` (`Dim_Calendar`).
3. Connect the tables:
   - **From:** `Dim_Calendar[Date]` (1)
   - **To:** `spotify_tracks_data[release_date]` (*)
   - **Cardinality:** One to Many (1:*)
   - **Cross Filter Direction:** Single
4. Create an empty measure table `_Measures` to store all DAX calculations in one clean folder.
