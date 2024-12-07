"""
Prototype : we get a "log" by the user saying which exercise they want to do or not, save the log in a json file and output a workout 
"""

import datetime
from typing import Deque, List, Optional, Tuple

from pydantic import BaseModel
import ollama

import workout

class UserLog(BaseModel):
    user_id : int 
    log : str

def generate_json(prompt : str, *, model : str = "tinyllama") -> str:
    # load the default workout 
    workout_json = workout.base_workout.model_dump_json()

    final_prompt = f" Given the following base workout as a JSON file: \
    {workout_json} and the following prompt : {prompt} \
    provide a workout as close as possible to the base workout, in the same template and that takes into account \
    the constraints of the prompt."


    response = ollama.generate(model = model, prompt = final_prompt, stream = False, 
                    format = workout.Workout.model_json_schema())
    return response

def write_log(user_id : int, log : str) -> bool:
    user_log = UserLog(user_id = user_id, log = log)
    # write in a JSON with the date
    date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    try:
        with open(f"logs/{user_id}_{date}.json", "w") as f:
            f.write(user_log.model_dump_json(indent = 4))
        return True
    except Exception as e:
        return False    
    
## 

if __name__ == "__main__":
    prompt = input()
    response = generate_json(prompt)
    print(response["response"])