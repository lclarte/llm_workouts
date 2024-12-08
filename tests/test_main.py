import pytest

import llm_workouts.main as main

def test_main():
    prompt = "return the base workout"
    result = main.generate_json(
        prompt=prompt, model = "llama3"
    )

    print(result)