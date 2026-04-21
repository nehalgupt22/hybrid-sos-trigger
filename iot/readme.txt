# IoT Hardware Implementation

This folder contains the hardware-oriented implementation of the Hybrid SOS Trigger System.

## Components Used
- Arduino UNO
- MPU6050 Accelerometer Sensor
- GPS Module (Neo-6M)
- GSM Module (SIM800/900)
- Buzzer
- Push Button
- Breadboard and jumper wires

## System Description
The system detects emergency situations using two methods:

1. Manual SOS Trigger (Push Button)
2. Motion Detection using MPU6050 accelerometer

When an abnormal condition is detected:
- GPS module fetches location coordinates
- GSM module sends SMS alert with location link
- Buzzer provides immediate local alert

---

## Hardware Setup (Real Prototype)

![Hardware Setup](hardware_setup.jpg)

**Description:**  
This image shows the actual physical setup of the system. It includes the Arduino UNO connected with MPU6050 sensor, GSM module, GPS module, and supporting components on a breadboard. This setup represents the initial hardware implementation of the SOS detection system.

---

## Circuit Design

![Circuit Diagram](circuit_diagram.png)

**Description:**  
This diagram represents the planned circuit connections between Arduino, sensors, GSM, and GPS modules. It illustrates how different components are interconnected to enable data acquisition and communication.

---

## Arduino Implementation

The file `sos_device.ino` contains:
- Accelerometer-based motion detection
- Manual SOS trigger using button
- GPS location retrieval
- GSM-based SMS alert system

---

## Note
The hardware implementation is partially completed. The primary focus of this project is the hybrid detection logic implemented in Python. The Arduino setup demonstrates how this logic can be extended to real-world embedded systems.
