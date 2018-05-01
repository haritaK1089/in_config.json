import json
json_data = json.loads(open('http_server_input.json').read())
print(json_data["http"]["service_name"])
