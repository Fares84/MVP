import logging
import azure.functions as func
import json
import os
import pyodbc


def main(event: func.EventHubEvent):

        logging.info('Python EventHub trigger processed an event: %s', event.get_body().decode('utf-8'))

            # convert string to a list of dicts
            payload = json.loads(event.get_body().decode('utf-8'))

            # update payload to table
            update_result = update_table(payload)

            # log success/fail status
            if update_result: logging.info(f'Payload update successful!')
            else: logging.info(f'Payload update failed!')


            def update_table(payload):
                ## Get connection string
                # from Azure Functions' configuration
                # conn_str = os.environ["SQLCONNSTR_SQLConnectionString"]
                conn_str = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:iot-project.database.windows.net,1433;Database=WeatherStationDB;Uid=fares;Pwd=Admin2021;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;";
                # initilize connection
                cnxn   = pyodbc.connect(conn_str)
                cursor = cnxn.cursor()

                # update payload
                timestamp   = payload['timestamp']
                device_name = payload['deviceId']
                temperature = payload['temperature']
                humidity    = payload['humidity']

                # stage part to the table
                sql_command = f"""
                insert into [dbo].[home_telemetry_data](timestamp, device_name, temperature, humidity)
                values ('{timestamp}', '{device_name}', {temperature}, {humidity});"""

                logging.info(f'{sql_command}')
                cursor.execute(sql_command)

                # commit when all updates are staged
                cnxn.commit()

                return True
