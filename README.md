# AI-First CRM HCP Module – Log Interaction System

## Overview

This project is a simplified AI-first Customer Relationship Management (CRM) system designed to log interactions with Healthcare Professionals (HCPs). It supports both structured form input and conversational chat input, demonstrating how AI can transform unstructured data into structured CRM records.

---

## Tech Stack

Frontend: React.js
Backend: FastAPI (Python)
AI Concept: LangGraph + LLM (Groq / Gemini)
Database: In-memory (for demonstration)

---

## Features

* Log interaction using structured form input
* Log interaction using conversational chat input
* Edit interaction via API
* Retrieve stored interactions
* Simulated AI workflow using LangGraph concept

---

## System Flow

React (Frontend) → FastAPI (Backend) → LangGraph Agent → LLM → Data Storage

---

## LangGraph Agent

LangGraph acts as the decision-making engine of the system. It processes user input, determines which tool to use, and coordinates workflows such as logging, editing, retrieving, and summarizing interactions using AI.

---

## Tools Implemented

**1. Log Interaction Tool**
Captures user input from form or chat and structures it using AI.

**2. Edit Interaction Tool**
Allows modification of previously stored interaction data.

**3. Fetch Interaction History Tool**
Retrieves past interaction records.

**4. Suggest Next Action Tool**
Uses AI to recommend follow-up actions.

**5. Summarize Interaction Tool**
Generates concise summaries of interactions using AI.

---

## How to Run the Project

### Backend

cd backend
uvicorn main:app --reload

### Frontend

cd frontend
npm install
npm start

---

## Key Concept

This project demonstrates how AI-first systems can convert conversational input into structured CRM data, improving productivity and decision-making.

---

## Demo Includes

* Frontend UI walkthrough (Form + Chat)
* Backend API demonstration
* Explanation of LangGraph agent and tools
