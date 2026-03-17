from ai.intent_parser import parse_intent
from dispatcher import execute_action


def process(user_input):
    data = parse_intent(user_input)
    result = execute_action(data)
    return result
