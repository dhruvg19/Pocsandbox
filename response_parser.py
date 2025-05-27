import json

def parse_response(response_str):
    try:
        return json.loads(response_str)
    except Exception as e:
        return f"Error parsing JSON: {e}"