# Hybrid SOS Trigger Analysis System

## Project Overview
This project analyzes the reliability of automatic SOS trigger mechanisms
in wearable safety systems.

The system compares:

- Basic Threshold Detection
- Threshold + Minimum Duration Detection

## Problem

Threshold-only detection often produces false alarms during normal motion
such as running or jumping.

False alarms reduce trust in emergency systems and may lead to alarm fatigue.

## Solution

This project implements duration-based filtering:

Trigger SOS only if acceleration exceeds threshold
for a minimum number of consecutive readings.

This reduces short spike false positives.

## Implementation

Language: Python  
Logic: Threshold + Minimum Duration  
Simulation-Based Dataset

## How to Run

1. Install Python.
2. Open terminal inside project folder.
3. Run:

   python main.py

4. Enter threshold and duration values.

## Future Scope

- Inactivity detection
- Repeated spike detection
- Hybrid manual + automatic trigger
- Hardware integration
