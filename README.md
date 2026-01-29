# CC LAB 2 – Monolithic Architecture & Load Testing

## Overview
This lab demonstrates **Monolithic Architecture** using a fest management application built with **FastAPI**.  
All features such as registration, events, checkout, and my-events run inside a **single application and deployment unit**.

The lab also uses **Locust** to perform load testing and analyze performance before and after optimization.

---

## Architecture Used
**Monolithic Architecture**
- Single FastAPI application
- Shared codebase and database
- All modules tightly coupled
- Single point of failure

---

## Tech Stack
- Backend: FastAPI  
- Database: SQLite  
- Load Testing Tool: Locust  
- Language: Python  

---

## Lab Objectives
1. Understand monolithic architecture
2. Observe system-wide failure due to a single bug
3. Perform load testing using Locust
4. Optimize API routes and compare performance

---

## Steps Performed

### 1. Setup & Run
- Created virtual environment
- Installed dependencies from `requirements.txt`
- Initialized database using `insert_events.py`
- Started FastAPI server using `uvicorn`

---

### 2. Application Usage
- Registered a user
- Logged in
- Accessed `/events`
- Accessed `/my-events` and `/checkout`

---

### 3. Monolithic Failure Demonstration
- Accessing `/checkout` crashed the entire server
- Demonstrated the **single point of failure** in monolithic applications
- Fixed the bug and restarted the server

---

## Load Testing with Locust

Load testing was performed on the following routes:
- `/checkout`
- `/events`
- `/my-events`

Tests were run **before and after optimization** to compare performance.

---

## Optimization Summary

### Bottlenecks
- Inefficient backend logic
- Slow tail responses
- Client-side request overhead
- No request timeout
- Fragmented endpoint statistics

---

### Changes Made
- Optimized inefficient logic
- Used request parameters instead of query strings
- Added request timeouts
- Grouped endpoint statistics in Locust
- Reduced wait time to improve connection reuse

---

### Performance Improvement
- Reduced average response time
- More stable latency values
- Better throughput consistency
- Cleaner and more accurate load testing metrics

---

## Conclusion
Monolithic applications are simple and easy to build but suffer from scalability and reliability issues.  
This lab demonstrates how a failure in one module can crash the entire system and why performance optimization and microservices are important for larger applications.

---

## Submission Contents
- Public GitHub repository
- Screenshots SS1 to SS9
- Optimized code
- This README
