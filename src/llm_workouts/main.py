"""
Prototype : we get a "log" by the user saying which exercise they want to do or not, save the log in a json file and output a workout 
"""

import datetime
from typing import Deque, List, Optional, Tuple

from pydantic import BaseModel
import ollama

import llm_workouts.workout as workout

class UserLog(BaseModel):
    user_id : int 
    log : str

def generate_json(prompt : str, *, model : str = "tinyllama") -> str:
    # load the default workout 
    workout_json = workout.base_workout.model_dump_json()

    final_prompt = f" Given the following base workout as a JSON file: \
    {workout_json} and the following comments : {prompt} \
    modify the base workout taking the comments into account. return a valid JON"

    # if stream is set to False, we can't constraint the output to follow the JSON format
    response = ollama.generate(
        prompt=final_prompt,
        model = model,
        format = workout.Workout.model_json_schema(),
        options={'temperature' : 0}
        )
    
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
    prompt = "return exactly the base workout provided, with the exercises, same reps and same sets"
    result = generate_json(
        prompt=prompt, model = "llama3"
    )

    print(result["response"])