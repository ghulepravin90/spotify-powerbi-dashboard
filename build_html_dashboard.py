import csv
import json

csv_path = r"C:\Users\Pravin Ghule\Downloads\BT_Mini_Project\Spotify_PowerBI_Project\spotify_tracks_data.csv"
html_path = r"C:\Users\Pravin Ghule\Downloads\BT_Mini_Project\Spotify_PowerBI_Project\spotify_dashboard_preview.html"

tracks = []
with open(csv_path, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        tracks.append({
            "id": row["track_id"],
            "name": row["track_name"],
            "artist": row["artist_name"],
            "album": row["album_name"],
            "date": row["release_date"],
            "year": int(row["release_year"]),
            "month": int(row["release_month"]),
            "month_name": row["release_month_name"],
            "genre": row["genre"],
            "type": row["track_type"],
            "explicit": row["is_explicit"],
            "pop": int(row["popularity"]),
            "streams": int(row["streams"]),
            "playlists": int(row["in_spotify_playlists"]),
            "dance": int(row["danceability_%"]),
            "energy": int(row["energy_%"]),
            "valence": int(row["valence_%"])
        })

json_tracks = json.dumps(tracks)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spotify Audio & Streaming Analytics Dashboard | Power BI Simulation</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    :root {{
      --bg-base: #121212;
      --bg-surface: #181818;
      --bg-surface-hover: #222222;
      --card-bg: #1e1e1e;
      --card-border: #2a2a2a;
      --spotify-green: #1DB954;
      --spotify-green-hover: #1ed760;
      --accent-purple: #9d4edd;
      --accent-red: #ff4b4b;
      --text-primary: #ffffff;
      --text-secondary: #b3b3b3;
      --text-muted: #727272;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    body {{
      background-color: var(--bg-base);
      color: var(--text-primary);
      padding: 24px;
      min-height: 100vh;
    }}
    .dashboard-container {{
      max-width: 1440px;
      margin: 0 auto;
    }}
    /* Header */
    .header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 24px;
      background: linear-gradient(135deg, #181818 0%, #202020 100%);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      margin-bottom: 20px;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .spotify-logo {{
      width: 42px;
      height: 42px;
      background: var(--spotify-green);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      color: #000;
      font-size: 24px;
    }}
    .header-title h1 {{
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}
    .header-title p {{
      font-size: 13px;
      color: var(--text-secondary);
      margin-top: 2px;
    }}
    .badge-pill {{
      background: rgba(29, 185, 84, 0.15);
      color: var(--spotify-green);
      border: 1px solid rgba(29, 185, 84, 0.4);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }}
    /* Filters Bar */
    .filters-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)) 100px;
      gap: 12px;
      background: var(--bg-surface);
      border: 1px solid var(--card-border);
      padding: 14px 20px;
      border-radius: 10px;
      margin-bottom: 24px;
      align-items: center;
    }}
    .filter-group {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .filter-group label {{
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}
    .filter-group select {{
      background: #242424;
      color: var(--text-primary);
      border: 1px solid #3a3a3a;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 13px;
      outline: none;
      cursor: pointer;
      transition: border 0.2s;
    }}
    .filter-group select:focus {{
      border-color: var(--spotify-green);
    }}
    .btn-reset {{
      background: #333333;
      color: var(--text-primary);
      border: none;
      padding: 9px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      align-self: flex-end;
      height: 36px;
      transition: background 0.2s;
    }}
    .btn-reset:hover {{
      background: #444;
    }}
    /* KPI Cards */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .kpi-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 18px 20px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.4);
    }}
    .kpi-label {{
      font-size: 12px;
      color: var(--text-secondary);
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }}
    .kpi-value {{
      font-size: 28px;
      font-weight: 700;
      color: var(--spotify-green);
      line-height: 1.2;
    }}
    .kpi-subtext {{
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .kpi-positive {{
      color: #1ed760;
    }}
    /* Charts Grid */
    .charts-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }}
    .charts-grid-equal {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }}
    .chart-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 20px;
      display: flex;
      flex-direction: column;
    }}
    .chart-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}
    .chart-card-title {{
      font-size: 15px;
      font-weight: 600;
      color: var(--text-primary);
    }}
    .chart-card-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
    }}
    .chart-canvas-container {{
      position: relative;
      flex-grow: 1;
      min-height: 260px;
      width: 100%;
    }}
    /* Top Table */
    .track-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .track-table th {{
      text-align: left;
      color: var(--text-muted);
      font-weight: 600;
      padding: 10px 8px;
      border-bottom: 1px solid #333;
    }}
    .track-table td {{
      padding: 10px 8px;
      border-bottom: 1px solid #282828;
      color: var(--text-secondary);
    }}
    .track-table tr:hover td {{
      background: #252525;
      color: #fff;
    }}
    .tag {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
    }}
    .tag-album {{ background: rgba(29, 185, 84, 0.2); color: #1ed760; }}
    .tag-single {{ background: rgba(157, 78, 221, 0.2); color: #c77dff; }}
    .tag-explicit {{ background: rgba(255, 75, 75, 0.2); color: #ff6b6b; }}
    .tag-clean {{ background: rgba(100, 100, 100, 0.2); color: #aaa; }}
    
    @media (max-width: 900px) {{
      .charts-grid, .charts-grid-equal {{
        grid-template-columns: 1fr;
      }}
      .filters-bar {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <div class="dashboard-container">
    <!-- Header -->
    <header class="header">
      <div class="header-left">
        <div class="spotify-logo">♫</div>
        <div class="header-title">
          <h1>Spotify Audio & Streaming Analytics Dashboard</h1>
          <p>Portfolio Project | Pravin Ghule | Power BI & DAX Architecture</p>
        </div>
      </div>
      <div>
        <span class="badge-pill">Interactive Simulation</span>
      </div>
    </header>

    <!-- Slicers Bar -->
    <div class="filters-bar">
      <div class="filter-group">
        <label>Release Year</label>
        <select id="filterYear">
          <option value="ALL">All Years (2020-2024)</option>
          <option value="2024">2024</option>
          <option value="2023">2023</option>
          <option value="2022">2022</option>
          <option value="2021">2021</option>
          <option value="2020">2020</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Genre</label>
        <select id="filterGenre">
          <option value="ALL">All Genres</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Track Type</label>
        <select id="filterTrackType">
          <option value="ALL">All (Album & Singles)</option>
          <option value="Album Track">Album Tracks Only</option>
          <option value="Single">Singles Only</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Content Rating</label>
        <select id="filterExplicit">
          <option value="ALL">All Content</option>
          <option value="Explicit">Explicit Tracks</option>
          <option value="Non-Explicit">Clean / Non-Explicit</option>
        </select>
      </div>

      <button class="btn-reset" id="resetBtn">Reset</button>
    </div>

    <!-- KPI Summary Row -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Total Streams</div>
        <div class="kpi-value" id="kpiStreams">0 B</div>
        <div class="kpi-subtext"><span class="kpi-positive">▲ MoM Avg +5.8%</span> | Global plays</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Total Tracks Analyzed</div>
        <div class="kpi-value" id="kpiTracks">0</div>
        <div class="kpi-subtext" id="kpiTrackSplit">Album vs Singles</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Unique Artists</div>
        <div class="kpi-value" id="kpiArtists">0</div>
        <div class="kpi-subtext" id="kpiTopArtist">Top Artist: -</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Average Popularity</div>
        <div class="kpi-value" id="kpiPopularity">0</div>
        <div class="kpi-subtext">Scale: 0 - 100 Index</div>
      </div>
    </div>

    <!-- Main Charts Section 1: Trend & Track Type -->
    <div class="charts-grid">
      <div class="chart-card">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title">Monthly Listener Trends & Cumulative Streams</div>
            <div class="chart-card-subtitle">Tracking aggregate streams across release months</div>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="monthlyTrendChart"></canvas>
        </div>
      </div>

      <div class="chart-card">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title">Album Tracks vs. Singles</div>
            <div class="chart-card-subtitle">Share of Total Streams</div>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="albumSingleChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Charts Section 2: Explicit Comparison & Top Artists -->
    <div class="charts-grid-equal">
      <div class="chart-card">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title">Explicit vs. Non-Explicit Songs</div>
            <div class="chart-card-subtitle">Total Streams & Catalog Volume by Rating</div>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="explicitChart"></canvas>
        </div>
      </div>

      <div class="chart-card">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title">Top 10 Artists by Total Streams</div>
            <div class="chart-card-subtitle">Cumulative plays across filtered catalog</div>
          </div>
        </div>
        <div class="chart-canvas-container">
          <canvas id="topArtistsChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Top 10 Streaming Tracks Table -->
    <div class="chart-card" style="margin-bottom: 24px;">
      <div class="chart-card-header">
        <div>
          <div class="chart-card-title">Top 10 High-Performing Tracks in Filtered View</div>
          <div class="chart-card-subtitle">Detailed breakdown of top songs, popularity, and streams</div>
        </div>
      </div>
      <div style="overflow-x: auto;">
        <table class="track-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Track Title</th>
              <th>Artist</th>
              <th>Album</th>
              <th>Genre</th>
              <th>Type</th>
              <th>Rating</th>
              <th>Popularity</th>
              <th>Total Streams</th>
            </tr>
          </thead>
          <tbody id="topTracksTableBody">
            <!-- Dynamically populated -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    const allTracks = {json_tracks};

    // Populate Genre Slicer
    const genreSelect = document.getElementById('filterGenre');
    const genres = Array.from(new Set(allTracks.map(t => t.genre))).sort();
    genres.forEach(g => {{
      const opt = document.createElement('option');
      opt.value = g;
      opt.textContent = g;
      genreSelect.appendChild(opt);
    }});

    // Chart instances
    let trendChart = null;
    let albumSingleChart = null;
    let explicitChart = null;
    let topArtistsChart = null;

    function formatNumber(num) {{
      if (num >= 1e9) return (num / 1e9).toFixed(2) + ' B';
      if (num >= 1e6) return (num / 1e6).toFixed(1) + ' M';
      if (num >= 1e3) return (num / 1e3).toFixed(0) + ' K';
      return num.toLocaleString();
    }}

    function updateDashboard() {{
      const year = document.getElementById('filterYear').value;
      const genre = document.getElementById('filterGenre').value;
      const trackType = document.getElementById('filterTrackType').value;
      const explicit = document.getElementById('filterExplicit').value;

      // Filter data
      const filtered = allTracks.filter(t => {{
        if (year !== 'ALL' && t.year !== parseInt(year)) return false;
        if (genre !== 'ALL' && t.genre !== genre) return false;
        if (trackType !== 'ALL' && t.type !== trackType) return false;
        if (explicit !== 'ALL' && t.explicit !== explicit) return false;
        return true;
      }});

      // KPIs
      const totalStreams = filtered.reduce((acc, t) => acc + t.streams, 0);
      const totalTracks = filtered.length;
      const uniqueArtists = new Set(filtered.map(t => t.artist)).size;
      const avgPop = totalTracks > 0 ? (filtered.reduce((acc, t) => acc + t.pop, 0) / totalTracks).toFixed(1) : 0;

      const albumCount = filtered.filter(t => t.type === 'Album Track').length;
      const singleCount = filtered.filter(t => t.type === 'Single').length;
      const albumPct = totalTracks > 0 ? Math.round((albumCount / totalTracks) * 100) : 0;

      // Artist streaming aggregates
      const artistStreamMap = {{}};
      filtered.forEach(t => {{
        artistStreamMap[t.artist] = (artistStreamMap[t.artist] || 0) + t.streams;
      }});
      const sortedArtists = Object.entries(artistStreamMap).sort((a,b) => b[1] - a[1]);
      const topArtistName = sortedArtists.length > 0 ? sortedArtists[0][0] : 'N/A';

      // Update KPI DOM
      document.getElementById('kpiStreams').textContent = formatNumber(totalStreams);
      document.getElementById('kpiTracks').textContent = totalTracks.toLocaleString();
      document.getElementById('kpiArtists').textContent = uniqueArtists.toLocaleString();
      document.getElementById('kpiPopularity').textContent = avgPop;
      document.getElementById('kpiTrackSplit').textContent = `Albums: ${{albumPct}}% | Singles: ${{100 - albumPct}}%`;
      document.getElementById('kpiTopArtist').textContent = `Top: ${{topArtistName}}`;

      // 1. Monthly Trend Data
      const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
      const monthlyStreams = new Array(12).fill(0);
      filtered.forEach(t => {{
        if (t.month >= 1 && t.month <= 12) {{
          monthlyStreams[t.month - 1] += t.streams;
        }}
      }});

      if (trendChart) trendChart.destroy();
      const ctxTrend = document.getElementById('monthlyTrendChart').getContext('2d');
      trendChart = new Chart(ctxTrend, {{
        type: 'line',
        data: {{
          labels: monthNames,
          datasets: [{{
            label: 'Streams',
            data: monthlyStreams,
            borderColor: '#1DB954',
            backgroundColor: 'rgba(29, 185, 84, 0.15)',
            borderWidth: 3,
            fill: true,
            tension: 0.35,
            pointBackgroundColor: '#1DB954',
            pointRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => 'Streams: ' + formatNumber(ctx.raw)
              }}
            }}
          }},
          scales: {{
            x: {{ grid: {{ color: '#262626' }}, ticks: {{ color: '#b3b3b3' }} }},
            y: {{ 
              grid: {{ color: '#262626' }}, 
              ticks: {{ 
                color: '#b3b3b3',
                callback: (val) => formatNumber(val)
              }} 
            }}
          }}
        }}
      }});

      // 2. Album vs Single Streams Donut Chart
      const albumStreams = filtered.filter(t => t.type === 'Album Track').reduce((a, t) => a + t.streams, 0);
      const singleStreams = filtered.filter(t => t.type === 'Single').reduce((a, t) => a + t.streams, 0);

      if (albumSingleChart) albumSingleChart.destroy();
      const ctxAlbum = document.getElementById('albumSingleChart').getContext('2d');
      albumSingleChart = new Chart(ctxAlbum, {{
        type: 'doughnut',
        data: {{
          labels: ['Album Tracks', 'Singles'],
          datasets: [{{
            data: [albumStreams, singleStreams],
            backgroundColor: ['#1DB954', '#9d4edd'],
            borderColor: '#181818',
            borderWidth: 3
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{
              position: 'bottom',
              labels: {{ color: '#fff', boxWidth: 12, padding: 14 }}
            }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => ctx.label + ': ' + formatNumber(ctx.raw)
              }}
            }}
          }}
        }}
      }});

      // 3. Explicit vs Non-Explicit Comparison Bar Chart
      const expStreams = filtered.filter(t => t.explicit === 'Explicit').reduce((a, t) => a + t.streams, 0);
      const nonExpStreams = filtered.filter(t => t.explicit === 'Non-Explicit').reduce((a, t) => a + t.streams, 0);
      const expCount = filtered.filter(t => t.explicit === 'Explicit').length;
      const nonExpCount = filtered.filter(t => t.explicit === 'Non-Explicit').length;

      if (explicitChart) explicitChart.destroy();
      const ctxExp = document.getElementById('explicitChart').getContext('2d');
      explicitChart = new Chart(ctxExp, {{
        type: 'bar',
        data: {{
          labels: ['Explicit', 'Non-Explicit'],
          datasets: [
            {{
              label: 'Total Streams',
              data: [expStreams, nonExpStreams],
              backgroundColor: ['#ff4b4b', '#1DB954'],
              borderRadius: 6,
              yAxisID: 'y'
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => 'Streams: ' + formatNumber(ctx.raw)
              }}
            }}
          }},
          scales: {{
            x: {{ grid: {{ display: false }}, ticks: {{ color: '#b3b3b3' }} }},
            y: {{ 
              grid: {{ color: '#262626' }}, 
              ticks: {{ 
                color: '#b3b3b3',
                callback: (val) => formatNumber(val)
              }} 
            }}
          }}
        }}
      }});

      // 4. Top 10 Artists Horizontal Bar Chart
      const top10 = sortedArtists.slice(0, 10);
      const top10Names = top10.map(a => a[0]);
      const top10Streams = top10.map(a => a[1]);

      if (topArtistsChart) topArtistsChart.destroy();
      const ctxArtists = document.getElementById('topArtistsChart').getContext('2d');
      topArtistsChart = new Chart(ctxArtists, {{
        type: 'bar',
        indexAxis: 'y',
        data: {{
          labels: top10Names,
          datasets: [{{
            label: 'Streams',
            data: top10Streams,
            backgroundColor: '#1ed760',
            borderRadius: 4
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ display: false }},
            tooltip: {{
              callbacks: {{
                label: (ctx) => 'Streams: ' + formatNumber(ctx.raw)
              }}
            }}
          }},
          scales: {{
            x: {{ 
              grid: {{ color: '#262626' }}, 
              ticks: {{ 
                color: '#b3b3b3',
                callback: (val) => formatNumber(val)
              }} 
            }},
            y: {{ grid: {{ display: false }}, ticks: {{ color: '#b3b3b3' }} }}
          }}
        }}
      }});

      // 5. Populate Top Tracks Table
      const topTracks = [...filtered].sort((a,b) => b.streams - a.streams).slice(0, 10);
      const tbody = document.getElementById('topTracksTableBody');
      tbody.innerHTML = '';
      topTracks.forEach((t, index) => {{
        const tr = document.createElement('tr');
        const typeClass = t.type === 'Album Track' ? 'tag-album' : 'tag-single';
        const expClass = t.explicit === 'Explicit' ? 'tag-explicit' : 'tag-clean';
        tr.innerHTML = `
          <td>${{index + 1}}</td>
          <td style="font-weight: 600; color: #fff;">${{t.name}}</td>
          <td>${{t.artist}}</td>
          <td>${{t.album}}</td>
          <td>${{t.genre}}</td>
          <td><span class="tag ${{typeClass}}">${{t.type}}</span></td>
          <td><span class="tag ${{expClass}}">${{t.explicit}}</span></td>
          <td>${{t.pop}}</td>
          <td style="color: #1ed760; font-weight: 600;">${{formatNumber(t.streams)}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Event listeners
    ['filterYear', 'filterGenre', 'filterTrackType', 'filterExplicit'].forEach(id => {{
      document.getElementById(id).addEventListener('change', updateDashboard);
    }});

    document.getElementById('resetBtn').addEventListener('click', () => {{
      document.getElementById('filterYear').value = 'ALL';
      document.getElementById('filterGenre').value = 'ALL';
      document.getElementById('filterTrackType').value = 'ALL';
      document.getElementById('filterExplicit').value = 'ALL';
      updateDashboard();
    }});

    // Initialize
    updateDashboard();
  </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated interactive dashboard preview at: {html_path}")
