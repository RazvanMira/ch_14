import random

prompts_for_hello = [
    "Hi!", "Hi there!", "Hello!"
]

prompts_for_name = [
    "Who are you? ", "What's your name? ", "I am ChatGPL, you are? "
]

prompts_for_interaction = [
    "Nice to meet you!", "Oh, that's great, good to have you here!", "Nice."
]

print(random.choice(prompts_for_hello))
input(random.choice(prompts_for_name))
print(random.choice(prompts_for_interaction))