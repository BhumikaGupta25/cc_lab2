## CC Lab 2 – Monolithic Architecture

In this lab, a monolithic fest management application was run using FastAPI, where all features such as events, checkout, and my-events existed in a single codebase and deployment.

A failure in the `/checkout` route was used to demonstrate the single point of failure in monolithic architecture, where one bug caused the entire application to crash. The bug was fixed and the application was restarted successfully.

Load testing was performed using Locust on the `/checkout`, `/events`, and `/my-events` routes. Performance was measured before and after optimization. Minor code and request-handling optimizations were applied, which reduced the average response time while maintaining similar request throughput.

This lab highlights how monolithic systems are easy to build but can suffer from reliability and performance issues as load increases.
