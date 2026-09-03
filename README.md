<img src="assets/banner.svg" width="100%" alt=""/>

<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/Espa%C3%B1ol-1B6AB4?style=for-the-badge&labelColor=1B6AB4" alt="Español"/></a>
<a href="README.en.md"><img src="https://img.shields.io/badge/English-6FC8F8?style=for-the-badge&labelColor=A8DCFF&color=6FC8F8" alt="English"/></a>

<br><br>

[![Email](https://img.shields.io/badge/anfeog@gmail.com-2274BD?style=flat-square&logo=gmail&logoColor=white)](mailto:anfeog@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-3189CF?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/anfeog)
![Ubicacion](https://img.shields.io/badge/Bogot%C3%A1%2C%20Colombia-A8DCFF?style=flat-square&logo=googlemaps&logoColor=1B6AB4)

</div>

## Sobre mí

Estudiante de **Ingeniería Industrial** en la Universidad de La Sabana (8.º semestre, grado estimado 2027-2), con énfasis en **analítica de datos**: Big Data, Machine Learning y visualización.

Trabajo en el punto donde se cruzan el proceso y el código: automatizo tareas manuales con Python, construyo dashboards y modelos de simulación, y mido el resultado. Mi último proyecto en producción **redujo una revisión de nómina de dos días a una hora**.



| | |
|---|---|
| **Formación** | Ingeniería Industrial — Universidad de La Sabana · énfasis en Analítica de Datos |
| **Certificaciones** | KAIZEN Lean Manufacturing Foundations (32 h) — Kaizen Institute Colombia, 2026 |
| **Idiomas** | Español nativo · Inglés B2/C1 — TOEFL iBT 94 |

<img src="assets/divider.svg" width="100%" alt=""/>

## Stack

**Lenguajes y análisis**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Backend y web**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Turso](https://img.shields.io/badge/Turso-4FF8D2?style=flat-square&logo=sqlite&logoColor=black)

**Datos y procesos**

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white)
![Lean](https://img.shields.io/badge/Lean_Manufacturing-2274BD?style=flat-square)
![Simulacion](https://img.shields.io/badge/Simulaci%C3%B3n-2274BD?style=flat-square)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

<img src="assets/divider.svg" width="100%" alt=""/>

## Proyectos

### [Duolocke Z Jalmeida](https://github.com/anfeog/DUOLOCKE) · [ver en vivo ↗](https://duolocke-z-jalmeida.onrender.com)

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Turso](https://img.shields.io/badge/Turso-4FF8D2?style=flat-square&logo=sqlite&logoColor=black)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black)

Marcador web compartido y mobile-first para llevar una partida cooperativa entre dos jugadores: vidas, medallas, combates de control y registro de bajas, sincronizado entre ambos móviles.

- **Problema:** el seguimiento se hacía en papel o en una hoja de cálculo y se desincronizaba entre los dos jugadores.
- **Solución:** API en Node/Express sobre Turso, frontend instalable como PWA, y un motor de reglas sin dependencias (`src/rules.js`) que calcula bloqueos de avance y condición de cierre. Autenticación por PIN con rate-limit por IP.
- **Decisión técnica:** vanilla JS deliberado — para dos usuarios y un puñado de registros, un framework habría sido sobreingeniería.
- **Estado:** desplegado y en uso real.

### [Polla Futbolera](https://github.com/anfeog/polla-futbolera)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)

Plataforma de predicciones deportivas usada por un grupo real de usuarios durante el Mundial 2026.

- **Solución:** backend en FastAPI + Jinja2, frontend en HTML/Tailwind/JS, instalable como PWA.
- **Automatización:** sincronización de marcadores y goleadores vía APIs externas cada 5 minutos, con SQLite/Turso y cálculo de puntajes y tabla de posiciones en vivo.

### Pre-validador de nómina — Craftmulti · 2026

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

- **Problema:** la revisión de nómina cruzaba reportes de RRHH a mano, con riesgo de error y sin margen antes del cierre mensual.
- **Solución:** sistema en Python (Flask + pandas) que compara los reportes y marca automáticamente las inconsistencias.
- **Impacto:** el tiempo de revisión pasó **de 2 días a 1 hora**.

<img src="assets/divider.svg" width="100%" alt=""/>

## Proyectos de ingeniería industrial

### Simulación de filas en confitería — Cine Colombia · 2025

- **Problema:** las configuraciones de cajas y personal se decidían sin evidencia de su efecto real sobre la espera.
- **Solución:** modelo de simulación del sistema de atención, con análisis de recorridos de clientes y patrones de llegada en hora pico.
- **Resultado:** escenarios cuantificados de mejora de la eficiencia del servicio.

### Mejora de tiempos en consulta externa — Clínica Universidad de La Sabana · 2024

- **Problema:** tiempos de espera altos sin trazabilidad de dónde se perdía el tiempo.
- **Solución:** registro de tiempos de atención y clasificación de actividades críticas del proceso.
- **Resultado:** cuellos de botella identificados y propuestas de optimización para reducir la espera.

### Análisis de seguridad en refinado de aceite — Alianza Team · 2024

- **Alcance:** verificación de cumplimiento de normativas internacionales (ISO) y legislación de seguridad ocupacional, en contacto directo con la planta en México.
- **Resultado:** riesgos de incendio y salud laboral identificados, con medidas preventivas alineadas a estándares de la industria.

<img src="assets/divider.svg" width="100%" alt=""/>

## Estadísticas

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=anfeog&show_icons=true&hide_border=true&border_radius=8&bg_color=0C3D6B&title_color=A8DCFF&text_color=E8F4FF&icon_color=6FC8F8" alt=""/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=anfeog&layout=compact&hide_border=true&border_radius=8&bg_color=0C3D6B&title_color=A8DCFF&text_color=E8F4FF" alt=""/>

</div>

## Contacto

Abierto a hablar de analítica de datos, automatización de procesos, simulación e investigación de operaciones — y a escuchar propuestas de práctica.

<div align="center">

[![Email](https://img.shields.io/badge/anfeog@gmail.com-2274BD?style=for-the-badge&logo=gmail&logoColor=white)](mailto:anfeog@gmail.com)
[![LinkedIn](https://img.shields.io/badge/linkedin.com/in/anfeog-3189CF?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/anfeog)

</div>

<img src="assets/divider.svg" width="100%" alt=""/>
