# FastBox Mystery Delivery System

A Python-based logistics simulation project that models a one-day delivery operation for a fictional company called **FastBox**.
The system assigns packages to the nearest delivery agents, simulates deliveries, calculates travel distances, and generates performance reports.

---

# Project Objective

The objective of this project is to simulate real-world delivery operations using:

* JSON data parsing
* Euclidean distance calculations
* Agent-package assignment logic
* Delivery simulation
* Report generation and analytics

---

# Features

## Core Features

* Read and parse JSON input data
* Assign packages to the nearest delivery agent
* Simulate package deliveries
* Calculate total travel distance
* Generate delivery performance report
* Identify the most efficient delivery agent
* Save report in JSON format

---

## Bonus Features

* Random delivery delays
* ASCII route visualization
* CSV export for top-performing agent
* Dynamic agent movement after delivery

---

# Technologies Used

* Python
* JSON
* CSV
* Math Module
* Random Module

-----

# Input Data Format

Example `base_case.json`

```json
{
  "warehouses": {
    "W1": [0, 0],
    "W2": [50, 75],
    "W3": [100, 25]
  },

  "agents": {
    "A1": [5, 5],
    "A2": [60, 60],
    "A3": [95, 30]
  },

  "packages": [
    {"id": "P1", "warehouse": "W1", "destination": [30, 40]},
    {"id": "P2", "warehouse": "W2", "destination": [70, 90]},
    {"id": "P3", "warehouse": "W3", "destination": [105, 20]},
    {"id": "P4", "warehouse": "W1", "destination": [10, 10]},
    {"id": "P5", "warehouse": "W2", "destination": [40, 80]}
  ]
}
```

---

# How the System Works

## Step 1 — Read JSON Data

The system reads warehouse, agent, and package information from a JSON file.

---

## Step 2 — Find Nearest Agent

Each package is assigned to the nearest delivery agent using Euclidean distance.

Distance Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}"}}

---

## Step 3 — Simulate Delivery

The assigned agent:

1. Travels to the warehouse
2. Picks up the package
3. Delivers it to the destination

The total distance traveled is calculated.

---

## Step 4 — Generate Report

The system calculates:

* Packages delivered
* Total distance traveled
* Efficiency score

Efficiency Formula:

\text{Efficiency}=\frac{\text{Total Distance}}{\text{Packages Delivered}}

Lower efficiency value indicates better performance.

---

# Engineering Decisions

## Why Euclidean Distance?

Euclidean distance calculates the shortest straight-line distance between two coordinates, making it suitable for delivery route estimation.

---

## Why Update Agent Position?

After completing a delivery, the agent’s location is updated to the destination point.
This simulates realistic movement and affects future package assignments.

---

## Why Use Dictionaries?

Python dictionaries provide fast access to agents, warehouses, and package data using keys.

---

## Why Add Random Delays?

Random delays simulate real-world delivery uncertainties such as:

* Traffic
* Weather
* Loading delays

---

# ASCII Route Visualization

Example:

```text
W1 ---> [30, 40]
W2 ---> [70, 90]
W3 ---> [105, 20]
```

---

# CSV Export

The best-performing delivery agent is exported to:

```text
top_performer.csv
```

This file contains:

* Agent name
* Packages delivered
* Total distance
* Efficiency score

---

# How to Run the Project

## Step 1 — Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2 — Open Project Folder

```bash
cd FastBox-Delivery-System
```

---

## Step 3 — Run Python File

```bash
python mystery_delivery_system.py
```

---

# Evaluation Criteria Covered

| Criteria             | Status |
| -------------------- | ------ |
| JSON Parsing         | ✅      |
| Distance Calculation | ✅      |
| Agent Assignment     | ✅      |
| Simulation           | ✅      |
| Report Generation    | ✅      |
| Code Clarity         | ✅      |
| Bonus Features       | ✅      |

---

# Future Improvements

* Graphical route visualization
* Real-time tracking dashboard
* Multiple delivery optimization
* Traffic-aware route calculation
* Database integration
* Web application version

---

# Author

**Rudraksh Ganjoo**
B.E. Artificial Intelligence & Data Science
PVG COETM

