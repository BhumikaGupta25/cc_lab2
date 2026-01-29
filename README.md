CC LAB 2 – Monolithic Architecture & Load Testing

Name: Bhumika Gupta
SRN: PES2UG2C3S128

Overview

This lab demonstrates the concept of Monolithic Architecture using a fest management application built with FastAPI.
All features such as registration, events, checkout, and my-events run inside a single application and deployment unit.

Through intentional crashes and load testing using Locust, we observe the limitations of monolithic systems and apply small optimizations to improve performance.

Architecture Used

Monolithic Architecture

Single FastAPI application

Shared codebase and database

All modules tightly coupled

Single point of failure

Tech Stack

Backend: FastAPI

Database: SQLite

Load Testing: Locust

Language: Python

Lab Objectives

Understand monolithic architecture using a real application

Observe how a failure in one module crashes the entire system

Perform load testing using Locust

Optimize API routes and analyze performance improvements

Steps Performed
1. Application Setup

Created virtual environment

Installed dependencies

Initialized database using insert_events.py

Ran FastAPI server using uvicorn

2. Functional Testing

Registered user

Logged in

Accessed /events

Verified /my-events and /checkout

3. Monolithic Failure Demonstration

Accessing /checkout caused the entire server to crash

Demonstrated single point of failure in monolithic systems

Bug was fixed by commenting out faulty logic

Load Testing with Locust
Optimized Routes

/checkout

/events

/my-events

Observations

Before optimization: higher average response time and unstable tail latency

After optimization: lower average response time and more stable performance

Optimization Summary
Bottlenecks Identified

Inefficient logic

Slow tail responses

Client-side request overhead

No request timeout

Fragmented endpoint statistics

Changes Made

Optimized backend logic (for /checkout)

Used request parameters instead of query strings

Added request timeouts

Grouped Locust endpoint statistics

Reduced wait time to reuse connections

Why Performance Improved

Reduced unnecessary computation

Prevented slow requests from inflating averages

Better connection reuse

Cleaner and more accurate load testing metrics

Conclusion

This lab highlights why monolithic applications are simple but risky at scale.
While easy to build and deploy, failures and scaling issues affect the entire system.
Through load testing and optimization, we improved performance but also understood why microservices are preferred for large-scale applications.
