import os

def load_template(filename):
    with open(os.path.join("prompts", filename), "r") as f:
        return f.read()

base_prompt = load_template("base_prompt.txt")
decade_prompt_template = load_template("decade_prompt.txt")
time_travel_prompt_template = load_template("time_travel_prompt.txt")

def build_decade_prompt(decade_data, user_message, memory=""):
    prompt = decade_prompt_template
    prompt = prompt.replace("{{decade}}", decade_data["decade"])
    prompt = prompt.replace("{{style}}", decade_data["style"])
    prompt = prompt.replace("{{examples}}", "\n".join(decade_data["examples"]))
    prompt = prompt.replace("{{user_message}}", user_message)

    full_prompt = base_prompt + "\n"
    if memory:
        full_prompt += f"\nConversation so far:\n{memory}\n\n"

    return full_prompt + prompt

def build_time_travel_prompt(current_decade, user_message, menory=""):
    prompt = time_travel_prompt_template
    prompt = prompt.replace("{{current_decade}}", current_decade)
    prompt = prompt.replace("{{user_message}}", user_message)

    return base_prompt + "\n" + prompt
