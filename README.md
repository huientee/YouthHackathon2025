YouthHackathon2025

🌐 Bubbly — Youth Media & Information Literacy + Mental Health Companion

Bubbly pipeline: Data Collection → Modelling → Gemini AI → Visualization

🚀 Problem Statement
Young people today are trapped in a paradox: their digital worlds, designed for connection, are increasingly causing isolation, anxiety, and informational malnutrition. Algorithmic filter bubbles on social media platforms create echo chambers, while doomscrolling fuels anxiety.
Most current “solutions” focus on screen-time punishment or dry lessons, which treat the symptoms with shame, not the cause with compassion.

🎯 Objective
Bubbly is a mobile-first prototype that redefines media literacy:
Empower youth with clear, visual feedback on their “digital diet.”
Support mental well-being through an empathetic, non-judgmental AI companion.
Nudge users into curiosity-driven exploration instead of passive doomscrolling.
Build resilience against misinformation and echo chambers with playful, engaging tools.


🧩 Prototype Features
1. BubblePal (AI Companion)
Empathetic chatbot (Gemini API via Flask)
Validates emotions first, then gently suggests mindful steps
Unlockable skins & accessories with BubbleCoins

2. BubbleTrack (Analytics Dashboard)
Visual “digital diet” (pie chart) of user’s browsing session
Shows balance of Negative / Diversity / Novelty / Friend metrics
Generates Session Report (PNG/PDF) with suggestions

3. Simulation Mode
Interactive sliders to simulate algorithm weights
Watch feed reorder instantly (education through play)

4. Rewards System
Daily/weekly tasks → BubbleCoins
Redeem for cosmetics (hats, glasses, skins, pixel town buildings)

🛠️ Technical Architecture
Frontend (HTML/JS, mock mobile screens):
  main.html → Start Journey hub, tasks, avatar customization
  chat.html → AI Bobo companion (supportive chat)
  piechart.html → Visualization of “digital diet” (sentiment, diversity, novelty, friend)
  sim.html → Interactive simulation of last 30 minutes’ posts with adjustable weights
  
Backend (Flask + Gemini):
  bubblechat.py → Flask API for AI Bobo
  
Endpoints:
  /init → greeting seed
  /chat → send message → Gemini 1.5 Flash (with custom system prompt)
  /health → service check
Data Flow:
  Start Journey → frontend triggers backend tracking of posts (via social media APIs / mock data for demo).
  NLP Processing (backend) → sentiment, bias, diversity, novelty metrics calculated.
  Visualization → PieChart dashboard shows aggregated “information diet.”
  Simulation → last 30 minutes of posts re-ranked by user’s chosen weights (negative/diversity/novelty/friend).
  AI Bobo → supports the journey with empathetic chat, explanations, and gentle nudges.
  Gamification → task system + BubbleCoins unlock avatar customization.

Minimal API (proposal-level)
  POST /oauth/callback → store user token (encrypted)
  GET /feeds?since=... → fetch session posts (per platform)
  POST /nlp/analyze → returns metrics per post + aggregates (for pie chart)
  GET /simulation/last30 → last window posts (features only)
  POST /simulation/rerank → {weights} → ranked list
  POST /chat → {message} → Gemini reply (with safety filter)
  GET /report/export → PNG/PDF summary

🌱 Sustainability, Scalability, Feasibility
  Sustainability: Freemium model (skins/customization) + NGO/educational licenses. Aligns with UNESCO SDGs on digital literacy & youth mental health.
  Scalability: Start with web demo → expand to Android app → integrate with classrooms/NGOs globally.
  Feasibility: Hackathon MVP uses HTML/JS mockups + Flask/Gemini backend. Extendable to native mobile with on-device NLP.

🎥 Demo & Deliverables
  3-min pitch video (YouTube link / file)
  Prototype (HTML pages + Flask backend)

Proposal PDF (this README)
📂 Repository Structure

├── bubblechat.py        # Flask backend for chat

├── main.html            # Home page (avatar, tasks)

├── chat.html            # Chat UI

├── piechart.html        # Analytics dashboard

├── sim.html             # Simulation sliders

📌 How to Run (Demo Mode)
  -Install dependencies
  -pip install flask flask-cors google-generativeai
  -Add your Gemini API key in bubblechat.py.
  -Run the backend
  -python bubblechat.py serve --port 5050
  -Open main.html in your browser (mock mobile screen).
  -Chat with BubblePal, view Analytics, and play with Simulation.
  
✨ Bubbly isn’t about punishing screen time — it’s about turning algorithm awareness into a playful, caring daily habit.
