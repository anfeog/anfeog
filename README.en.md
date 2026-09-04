<img src="assets/banner.svg" width="100%" alt=""/>

<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/Espa%C3%B1ol-6FC8F8?style=for-the-badge&labelColor=A8DCFF&color=6FC8F8" alt="Español"/></a>
<a href="README.en.md"><img src="https://img.shields.io/badge/English-1B6AB4?style=for-the-badge&labelColor=1B6AB4" alt="English"/></a>

<br><br>

[![Email](https://img.shields.io/badge/anfeog@gmail.com-2274BD?style=flat-square&logo=gmail&logoColor=white)](mailto:anfeog@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-3189CF?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/anfeog)
![Location](https://img.shields.io/badge/Bogot%C3%A1%2C%20Colombia-A8DCFF?style=flat-square&logo=googlemaps&logoColor=1B6AB4)

</div>

## About

Industrial Engineering student at Universidad de La Sabana (8th semester, expected graduation 2027-2), focused on **data analytics**: Big Data, Machine Learning and visualization.

I work where process meets code: automating manual tasks with Python, building dashboards and simulation models, and measuring the outcome. My most recent production project **cut a payroll review from two days to one hour**.

Looking for an internship where optimization and data analysis translate into measurable results.

| | |
|---|---|
| **Education** | Industrial Engineering — Universidad de La Sabana · Data Analytics focus |
| **Certifications** | KAIZEN Lean Manufacturing Foundations (32 h) — Kaizen Institute Colombia, 2026 |
| **Languages** | Spanish native · English B2/C1 — TOEFL iBT 94 |

<img src="assets/divider.svg" width="100%" alt=""/>

## Stack

**Languages and analysis**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Backend and web**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Turso](https://img.shields.io/badge/Turso-4FF8D2?style=flat-square&logo=sqlite&logoColor=black)

**Mobile**

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)
![Riverpod](https://img.shields.io/badge/Riverpod-4B32C3?style=flat-square)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white)

**Data and process**

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)
![Lean](https://img.shields.io/badge/Lean_Manufacturing-2274BD?style=flat-square)
![Simulation](https://img.shields.io/badge/Simulation-2274BD?style=flat-square)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

<img src="assets/divider.svg" width="100%" alt=""/>

## Projects

### [PokéNotes](https://github.com/anfeog/pokenotes)

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)
![Riverpod](https://img.shields.io/badge/Riverpod-4B32C3?style=flat-square)
![Hive](https://img.shields.io/badge/Hive-FFB300?style=flat-square)
![Android](https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white)

An Android app for taking live notes on what the opponent reveals during a competitive match: moves, item, ability and loose observations, jotted down at speed mid-game.

- **Problem:** the information that decides the match is revealed bit by bit and forgotten as soon as it ends; a phone's notes app is slow and unstructured exactly when there is no time.
- **Solution:** a **fully offline** Flutter app that persists on every keystroke — killing the app mid-match loses nothing. The full PokeAPI index (1,351 species, 937 moves) is cached in **2 requests** by deriving the sprite URL from the id, instead of 1,351 calls.
- **Technical call:** the record is *append-only* and the rule lives in the domain, not the UI: once a match is saved the model **rejects** overwriting what was logged and only allows filling gaps and adding notes. No screen can bypass it by accident.
- **Deliberate scope:** no damage calculator and no strategy hints — it only records what you observe, with a test that enforces it. That is what keeps it within what is allowed in formats where phones are permitted.
- **Status:** finished. 78 tests, release APK in use.

### [Duolocke Z Jalmeida](https://github.com/anfeog/DUOLOCKE) · [live demo ↗](https://duolocke-z-jalmeida.onrender.com)

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Turso](https://img.shields.io/badge/Turso-4FF8D2?style=flat-square&logo=sqlite&logoColor=black)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)

A shared, mobile-first web scoreboard for tracking a two-player co-op run: lives, badges, checkpoint battles and a knockout log, kept in sync across both phones.

- **Problem:** tracking was done on paper or in a spreadsheet and drifted out of sync between the two players.
- **Solution:** a Node/Express API over Turso, a frontend installable as a PWA, and a dependency-free rules engine (`src/rules.js`) that computes progression locks and the end-of-run condition. PIN auth with per-IP rate limiting.
- **Technical call:** vanilla JS on purpose — for two users and a handful of records, a framework would have been over-engineering.
- **Status:** deployed and in active use.

### [Polla Futbolera](https://github.com/anfeog/polla-futbolera)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)

A sports prediction platform used by a real group of users throughout the 2026 World Cup.

- **Solution:** FastAPI + Jinja2 backend, HTML/Tailwind/JS frontend, installable as a PWA.
- **Automation:** scores and goalscorers synced through external APIs every 5 minutes, with SQLite/Turso and live scoring and standings.

### Payroll pre-validator — Craftmulti · 2026

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

- **Problem:** payroll review meant cross-checking HR reports by hand, error-prone and with no slack before the monthly close.
- **Solution:** a Python system (Flask + pandas) that compares the reports and automatically flags inconsistencies.
- **Impact:** review time went **from 2 days to 1 hour**.

<img src="assets/divider.svg" width="100%" alt=""/>

## Industrial engineering projects

### Concession queue simulation — Cine Colombia · 2025

- **Problem:** register and staffing configurations were decided without evidence of their real effect on waiting time.
- **Solution:** a simulation model of the service system, with analysis of customer paths and peak-hour arrival patterns.
- **Result:** quantified scenarios for improving service efficiency.

### Outpatient care time improvement — Clínica Universidad de La Sabana · 2024

- **Problem:** long waiting times with no traceability of where the time was actually lost.
- **Solution:** recording of service times and classification of the process's critical activities.
- **Result:** bottlenecks identified and optimization proposals to reduce waiting time.

### Safety analysis in oil refining — Alianza Team · 2024

- **Scope:** verified compliance with international standards (ISO) and occupational safety legislation, in direct contact with the plant in Mexico.
- **Result:** fire and occupational health risks identified, with preventive measures aligned to industry standards.

<img src="assets/divider.svg" width="100%" alt=""/>

## Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=anfeog&show_icons=true&hide_border=true&border_radius=8&bg_color=0C3D6B&title_color=A8DCFF&text_color=E8F4FF&icon_color=6FC8F8" alt=""/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=anfeog&layout=compact&hide_border=true&border_radius=8&bg_color=0C3D6B&title_color=A8DCFF&text_color=E8F4FF" alt=""/>

</div>

## Contact

Happy to talk about data analytics, process automation, simulation and operations research — and to hear about internship opportunities.

<div align="center">

[![Email](https://img.shields.io/badge/anfeog@gmail.com-2274BD?style=for-the-badge&logo=gmail&logoColor=white)](mailto:anfeog@gmail.com)
[![LinkedIn](https://img.shields.io/badge/linkedin.com/in/anfeog-3189CF?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/anfeog)

</div>

<img src="assets/divider.svg" width="100%" alt=""/>
