# Home Weather Station

## AUTHORS
Fares Sassi - [Github](https://https://github.com/Fares84) / [Twitter](https://twitter.com/faressassi) / [LinkedIn](https://www.linkedin.com/in/faress-s-8b55a61b1/)

## Blog, Landing Page & Demo
[Blog in LinkedIn]()
[Landing Page](https://252892.wixsite.com/landingpagefares)
[Youtube Video](https://www.youtube.com/watch?v=bUlbu-Joi_0)

## Introduction
I chose to do this project which is to monitor and display the temperature
and humidity of the house in real time for two reason. the main reason is that
I wanted to follow the field of cloud and devops which is the future. secondly
i got this idea after my cousin who just had a baby express a need to know
if the baby's room was warm relative to the room temperature or not
and evenetually cold or not.

## Project Description
The project takes place in 3 stages:
* 1st part: Data from HOME is sent to Azure IoT Hub when it packages a data stream
* 2nd part: the event is received by the Azure Iot Hub, it is processed and sent
to the Azure function. Then the event is processed and saved in an Azure Sql Database.
* 3 rd: Grafana can later read and display data from the database

## Technologies
Project is created with:
* Visual Studio Code version: 1.57
* Python version: 3.9
* Grafanaversion: 8.1
* Raspberry Pi Azure IoT Online Simulator
* Azure Cloud

## License
Copyright (c) Microsoft Corporation. All rights reserved.
A short and simple permissive license with conditions only requiring
preservation of copyright and license notices.
Licensed works, modifications, and larger works may be distributed under
different terms and without source code.

## ScreenShot Grafana end point
[Imgur](https://imgur.com/7LyeP4a)