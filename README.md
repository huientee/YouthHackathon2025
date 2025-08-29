This project was developed for the **UNESCO Youth Hackathon (Media & Information Literacy track).**

Our purpose is to help young users see their algorithm bubble:
  Track what kind of content they are exposed to
  Classify topics and visualize their “information diet”
  Let them interactively re-rank feeds to understand algorithm weightage
  Provide gentle emotional support and gamification to make the experience engaging

**Prototype Components**

- Frontend (HTML/JS, mock mobile screens)
  main.html → Start Journey Hub
  
    User consent, start session, task list, avatar customization
  
  chat.html → AI Bobo Companion
  
    Gemini-powered chat for empathy & explanations (not core, only supportive)
  
  piechart.html → Topic Pie Chart Visualization
  
    Shows proportions of content categories (education, tech, entertainment, etc.)
  
  sim.html → Interactive Simulation
    Re-rank last 30 minutes of posts with adjustable weights (diersity, novelty, bias)

- Backend / Processing (Python)
  tracker.py → Tracking Module
  
    Fetches posts from social media APIs (OAuth) or fallback demo JSON
  
    Stores a rolling 30-minute buffer of session posts

  nlp_topic.py → Topic Analysis Module
  
    Runs NLP classification → assigns each post a topic (education, tech, news, etc.)
  
    Calculates features for simulation (novelty, friend, optional sentiment)
  
    Exports clean JSON file for frontend visualization & simulation
  
  bubblechat.py → Flask API + Gemini
  
    /init → greeting seed
  
    /chat → send user message → Gemini 1.5 Flash with custom prompt
  
    /health → prompt check
  
    Bobo explains metrics, responds empathetically, and handles crisis keywords with safe fixed responses
  

**Data Flow**
  1. Start Journey → User consents, session begins in main.html
  2. Track Social Media → tracker.py fetches recent posts, stores 30-min buffer
  3. NLP Topic Analysis → nlp_topic.py classifies topics & generates features
  4. Visualization → piechart.html renders information diet as topic pie chart
  5. Simulation → sim.html loads last-30-min posts, applies weight sliders to re-rank feed
  6. AI Bobo Companion → chat.html explains metrics & gives empathetic support
  7. Gamification → tasks → coins → Bobo customization
