
# ✅ SixIntel Project – To-Do List

## 🟢 Phase 1: Core Web Functionality

### 🔹 Landing & Navigation
- [x] Create landing page with NA/EU region options
- [x] Create region-specific home pages
- [x] Create navigation bar using layout template

### 🔹 Data Display
- [x] Create standings pages for NA and EU
- [x] Create stats pages 

### 🔹 Manual Data Management
- [x] Use local JSON files for standings (`na_standings.json`, `eu_standings.json`)
- [x] Add all players on JSON files
- [x] Add teams to players on JSON files
- [x] Add a command-line script to update standings JSON interactively
- [ ] Make the script update everything incluing KOST KPR, etc
- [ ] (Optional) Create admin web form to update standings from the browser

## 🛠 Phase 2: Automation & Scraping

### 🔹 Scraping Engine
- [ ] Fix or improve Selenium scraping to pull standings automatically
- [ ] Support scraping multiple regions (NA, EU, LATAM)
- [ ] Cache results locally to avoid re-scraping each run

### 🔹 Scheduled Sync
- [ ] Add a `cron` job or background thread to update data daily or weekly
- [ ] Log updates to a file for audit/debugging

## 🎨 Phase 3: UI/UX Enhancements

### 🔹 Polish Layout
- [x] Use TailwindCSS for styling
- [x] Add league logos / team icons
- [x] Add country flags for players
- [ ] Make tables sortable or filterable (JS or Alpine.js)

### 🔹 Mobile Support
- [ ] Test layout on mobile
- [ ] Adjust spacing/fonts for small screens

## 📊 Phase 4: Stats System

### 🔹 Basic Stats
- [ ] Add match-level stats (e.g., maps played, rounds won)
- [ ] Show team K/D ratio, win % per map

### 🔹 Advanced Features
- [ ] Add player-level stats (headshots, rating, etc.)
- [ ] Add charts (bar/line graphs using Chart.js or Recharts)
- [ ] Compare teams side-by-side

## 🌐 Phase 5: Hosting & Deployment

### 🔹 Local Hosting
- [x] Run on `localhost:5000`

### 🔹 Production
- [x] Prepare app for production using `gunicorn` or `waitress`
- [x] Host on AWS (EC2 or Lightsail) or Linode
- [x] Set up custom domain 
- [ ] Set up HTTPS (via Certbot)
- [ ] Run ads

## 📝 Project Management

### 🔹 Dev Workflow
- [x] Add `.gitignore`
- [ ] Create `requirements.txt` and `README.md`
- [ ] Document manual update process in `docs/`
