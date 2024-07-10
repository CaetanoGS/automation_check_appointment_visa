import time

from dotenv import load_dotenv

from services.appointment import check_appointment
from datetime import datetime

from services.basic import time_running_script


dotenv_path = '.env'
load_dotenv(dotenv_path)
start_time = datetime.now()

while True:
    teams = [
        {"id": 1, "button_id": "button-plus-293"},
        {"id": 2, "button_id": "button-plus-296"},
        {"id": 3, "button_id": "button-plus-297"}
    ]

    for team in teams:
        check_appointment(team["id"], team["button_id"])
    
    print(f"{datetime.now()} - No Appointment found")
    print(time_running_script(start_time))

    time.sleep(180)
