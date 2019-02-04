from api_func import *

token = get_token_authentication()

lab_vm = ["vm-186", "vm-188", "vm-197", "vm-1432"]
print("-" * 50, "Stopping Windows Virtual Machine ", "-" * 50)
for vm in lab_vm:
    post_response = post(api="/vcenter/vm/" + vm + "/guest/power?action=shutdown", token = token)
    time.sleep(1)
