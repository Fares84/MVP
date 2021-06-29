# Home Weather Station

##AUTHORS
Fares Sassi - [Github](https://https://github.com/Fares84) / [Twitter](https://twitter.com/faressassi) / [LinkedIn](https://www.linkedin.com/in/faress-s-8b55a61b1/)

## Introduction
We will create a web application that will be our weather station,
we will use a Rasperry PI simulator device (not a real simulator,
you can buy some for the fun too) which sends the temperature
and humidity inside the house into real time to our API in the
Azure cloud.

## Project Description
The project takes place in 3 stages:
1st part: Data from HOME is sent to Azure IoT Hub when it packages a data stream
2nd part: the event is received by the Azure Iot Hub, it is processed and sent
to the Azure function. Then the event is processed and saved in an Azure Sql
Database.
3 rd: Grafana can later read and display data from the database

## Technologies
Project is created with:
Visual Studio Code 1.57
Python 3.9
Grafana 8
Raspberry Pi Azure IoT Online Simulator
Azure Cloud

## License
Public Domain. No copy write protection.

[Imgur](https://imgur.com/7LyeP4a)