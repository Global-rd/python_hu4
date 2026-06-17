# hw_08_streamlit – Weather Map & Data Visualization App

Streamlit alkalmazás, ami az [Open-Meteo](https://open-meteo.com/en/docs)
API-kból kéri le egy megadott város aktuális időjárását, megjeleníti
KPI-okként, térképen mutatja a várost, és kirajzolja a következő 5 nap
óránkénti hőmérséklet-előrejelzését. Minden keresést egy SQLite
adatbázisba logol.

## Helyi futtatás

```bash
pip install -r requirements.txt
streamlit run app.py
```

Az app a `weather_log.db` SQLite fájlt automatikusan létrehozza az első
indításkor.

## Deploy – Streamlit Community Cloud

1. Hozz létre egy **saját, public** GitHub repót, és töltsd fel ebbe a
   mappa tartalmát (`app.py`, `requirements.txt`, `.streamlit/config.toml`).
2. Menj a https://share.streamlit.io oldalra, jelentkezz be a GitHub
   fiókoddal.
3. **New app** → válaszd ki a repót, a branch-et és a `app.py` fájlt →
   **Deploy**.
4. A kapott élő linket tedd be a robot_dreams repóba leadott PR leírásába.

## Fájlok

| Fájl | Leírás |
|------|--------|
| `app.py` | A teljes Streamlit alkalmazás |
| `requirements.txt` | Függőségek a deployhoz |
| `.streamlit/config.toml` | Sötét téma (a mintához hasonló kinézet) |
