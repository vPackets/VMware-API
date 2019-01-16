from api_func import *

token = get_token_authentication()

windows_vm = ["vm-186", "vm-188", "vm-197"]
print("-" * 50, "Starting Windows Virtual Machine ", "-" * 50)
for vm in windows_vm:
    post_response = post(api="/vcenter/vm/" + vm + "/power/start", token = token)
    time.sleep(1)
