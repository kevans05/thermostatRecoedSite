thermostatRecord
================
Project Proposal:
Instrumentation for Monitoring Environmental Data of a Temperature Based System
Team Kyle Evans & Cody Morton 
7-Apr-14
1.	Introduction
There are many different systems in industry the require precise temperatures to be completed; this is especially true in the chemical processes of fractional distillation used in tuning crude oil in Fuel oil, Diesel, Kerosene, Petrol, and Propane. If we use the example of turning crude oil into Fuel this happens at 370°C if we go too much cooler we produce Diesel. This is not the process that requires accurate temperature to be taken; food process also needs these measurements and this is the process we will be mimicking in our experiment. We plan on measuring water temperature similar to industrial food process; with temperatures of water varying from 3°C to 100°C.   
2.	System Specification
We will be measuring water temperature in a verity of sensors to try and develop a good model for the system.     
Function	Range	Resolution	Error	Display
Absolute Water temperature T (°C)	0 to 100 OC	12 bit
	0.5°C	Thermometer

3.	Selection of Sensors 
The following sensor was selected to measure the water temperature 
a)	Temperature sensor – DS18B20
b)	Temperature sensor 2 - MLX90614
4.	System Design
The implementation of the system functions are investigated, and divided into two groups: primary functions, and derived function. The primary functions are measured through physical sensors, and the derived functions are calculated according to the primary functions. The table below shows the system design.


Primary/Derived	Function	HW/SW	Sensor	Formula
Primary Function	Temperature (P)	HW + SW	MLX90614	NA
	Temperature (P)	HW + SW	DS18B20	NA

5.	Testing System
To calibrate the instrumentation system, we will be exposing our sensors to different water conditions and comparing it to alcohol thermometers. 
6
