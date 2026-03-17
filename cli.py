from ai.intent_parser import parse_intent
from dispatcher import execute_action

while True:

    user_input = input("AI > ")

    intent_data = parse_intent(user_input)

    result = execute_action(intent_data)

    print(result)