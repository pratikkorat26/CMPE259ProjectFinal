# 📘 Personalized Fitness & Health Tracker Virtual Assistant (VA)

**Author**: Pratikkumar Dalsukhbhai Korat  
**SJSU ID**: 017512508  
**Course**: CMPE259 - Spring 2025 (LLM-Based Virtual Assistant Project)  
**Instructor**: Professor Jorjeta Jetcheva  
**Project Type**: Individual  

---

## 🧠 Project Overview

This project implements a **Personalized Fitness & Health Tracker Virtual Assistant** using **Large Language Models (LLMs)**. The assistant enables users to monitor and analyze personal health metrics — such as heart rate, blood pressure, SpO₂ levels, and sleep stages — through queries processed via a conversational interface.

It uses a **hybrid approach**:
- Structured health data from a **local SQLite database**
- External health knowledge from **real-time web search**

---

## 🎯 Use Case

The assistant acts as a personal health coach by answering user queries like:
- "What was my average heart rate last week?"
- "Compare my deep vs light sleep duration for last night."
- "Suggest ways to improve my oxygen levels."

The system includes:
- **Heart Metrics**: Heart rate, systolic/diastolic blood pressure, blood oxygen levels
- **Sleep Metrics**: Duration, quality score, REM/Deep/Light sleep stages

---

## 🧰 Tools & Architecture

- **LLMs Used**:
  - `Gemma 3B / 27B`: For high-quality reasoning and analysis
  - `Qwen 4B`: For lighter, faster inference and comparisons

- **Tools Integrated**:
  - `SQLite`: For storing one-year simulated heart and sleep data
  - `Web Search API`: SerpAPI or DuckDuckGo wrapper for health tips
  - (Optional) `Streamlit` or `Gradio`: For a front-end user interface

---

## 🧪 Features

- Query health trends over time
- Detect anomalies and spikes in vitals
- Compare metrics across days or weeks
- Integrate external health advice for personalized suggestions
- Evaluate LLM performance based on response quality, tool usage, and robustness

---

## 💬 Example Queries
20 pre-defined user queries include:

1. What was my average heart rate last week?
2. Show me my sleep quality trends over the past month.
3. When was the last time my oxygen level dropped below 95?
4. Did I meet my sleep goal this week?
5. What's the average systolic pressure during the day?
6. Find when my heart rate spiked above 100 in the last 30 days.
7. Suggest ways to improve sleep quality.
8. Compare my deep vs light sleep duration for last night.
9. What’s the trend of my heart rate on weekends?
10. Did I sleep more on weekdays or weekends this month?
11. Is there any correlation between poor sleep and high heart rate?
12. How much time did I spend in REM sleep on average?
13. Was my oxygen level stable last night?
14. Find days when I had less than 6 hours of sleep.
15. What’s my longest uninterrupted sleep streak?
16. Give me a weekly summary of my health metrics.
17. Suggest recovery tips based on my recent vitals.
18. What are normal ranges for systolic and diastolic pressure?
19. How can I improve low SpO₂ levels?
20. Is my heart rate consistent after workouts?
---

## 📂 File Structure

- `Project Colab Notebook.ipynb`: Full implementation with tool use, prompt examples, LLM interactions, and evaluations
- `README.md`: This documentation file

---

# 🧠 How to Install and Use Ollama Locally

Ollama allows you to run large language models like LLaMA 3, Mistral, Gemma, and others *locally* on your machine. This guide helps you get started with installation, model loading, and basic usage.

---

## 🔧 System Requirements

- **OS**: macOS, Linux, or Windows (via WSL2)
- **RAM**: Minimum 32 GB (64+ GB recommended)
- **CPU**: Works on CPU; GPU acceleration available (Minimum requirement RTX 4070 GPU)
- **Disk**: Models take 3–8 GB+ of space each


* This code won't work on a Colab notebook or a Mac or Windows with 16GB of RAM. 

---

## Installation Instructions

### 1. Install Ollama

#### macOS and Windows
Install via visiting ollama.com/download:

#### Linux
Install via APT:
```
curl -fsSL https://ollama.com/install.sh | sh
```
#### 2. Pull and Run Models
To pull and run models, use the following commands:

```
ollama run gemma3:27b or qwen3:4b
```
* Now model is successfully pulled and running.

---
## ⚙️ Setup Instructions

1. Clone the repository or open the notebook in Google Colab
2. Install dependencies (requirements.txt)
   - For local, use `pip install -r requirements.txt` in your terminal
3. Run the notebook cells sequentially
4. Interact with the assistant via notebook or deployed UI

---

## 🚀 Future Improvements

- Integrate real health tracker APIs (e.g., Fitbit, Apple Health)
- Add long-term health goal recommendations
- Improve natural language interface with fine-tuned LLMs
- Implement caching and session memory
- Even with the advanced models, the assistant may not always provide accurate or relevant information. Continuous fine-tuning and evaluation are necessary to improve its performance.
---
