 🌱 Smart Plant Care System

An IoT-based plant monitoring and care system that uses Raspberry Pi, sensors, microservices, and ThingSpeak to automate plant care.

The system collects real-time data from temperature, soil moisture, and light sensors, processes the data through a microservices architecture, and provides automated predictions and alerts through Telegram.


 👩‍💻 My Contribution

As part of this group project, I independently developed two components:

 ⏱️ TimeShift — Weekly Prediction Workflow

I independently implemented the weekly prediction workflow for sensor data.

- Fetches historical temperature and soil-moisture data from ThingSpeak
- Uses linear regression to model sensor trends
- Generates predictions for the following 7 days
- Compares predicted values with device-specific thresholds
- Generates prediction alarms for out-of-range values
- Publishes prediction alarms through MQTT
- Runs the prediction workflow once per week

 🚨 Sensor Control — Monitoring & Alerts

Implemented the **sensor monitoring and alert logic** responsible for detecting abnormal sensor readings and notifying users.

- Monitored incoming sensor values
- Applied threshold-based checks for abnormal readings
- Implemented alert/notification logic
- Integrated alerts with the project's Telegram-based communication

> This was a group academic project. The components described above represent my individual contribution.

---

 🚀 Project Overview

The complete system provides:

- 📡 Real-time sensor monitoring
- ☁️ Microservices-based architecture
- 🤖 Automated prediction and alerting
- 💬 Telegram Bot integration
- 🌱 Plant-care monitoring using temperature, soil moisture, and light data
