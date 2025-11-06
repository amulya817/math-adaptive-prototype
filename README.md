# Math Adventures — AI-Powered Adaptive Learning Prototype

## 🎯 Objective
An adaptive math learning app for children (ages 5–10).  
It generates puzzles, tracks performance, and adjusts difficulty dynamically based on the learner’s progress.

## 🧠 Features
- Three difficulty levels: Easy, Medium, Hard  
- Tracks correctness and response time  
- Adaptive logic to promote or demote levels automatically  
- Displays performance summary  
- Logs session details to a text file

## 🏗️ Project Structure
math-adaptive-prototype/
├─ README.md  
├─ requirements.txt  
└─ src/  
   ├─ main.py  
   ├─ puzzle_generator.py  
   ├─ tracker.py  
   └─ adaptive_engine.py  

## 🚀 How to Run
1. Open terminal in this folder.  
2. Run:  

## 🧩 Adaptive Logic (Rule-based)
- If accuracy > 80% and avg_time < 5s → increase difficulty  
- If accuracy < 50% or avg_time > 10s → decrease difficulty  
- Otherwise → stay at same level  

## 📊 Key Metrics
- Accuracy (% of correct answers)
- Average response time (seconds)
- Recommended next difficulty level

## 🌱 Future Improvements
- Add ML-based difficulty prediction  
- Integrate GUI using Streamlit  
- Store detailed analytics for each learner

