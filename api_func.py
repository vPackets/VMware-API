import requests
import api_config
import getpass
import sys
import time
#import urllib3

requests.packages.urllib3.disable_warnings()
#urllib3.disable_warning(urllib3.exceptions.InsecureRequestWarning)

def get_token_authentication(url = api_config.URL):
    print("*"*10,"Authentication with the vCenter: ", url, "*"*10)
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    url = url + "rest/com/vmware/cis/session"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'vmware-use-header-authn': "",
        'vmware-api-session-id': "null",
        'Cache-Control': "no-cache",
    }
    print("\n\n" + "Processing GET " + url )
    try:
        response = requests.post(url, headers=headers, auth = (username, password),verify = False)
        if response.status_code != 200:
            print("Something was wrong during the token creation (Credentials, Host down...)")
            print("The status code is: ", response.status_code)
            sys.exit()
        else:    
            print("The status code is: ", response.status_code)
            print("The Token ID is: ", response.json()["value"]) 
            print("*"*35,"End of Authentication","*"*35)
            print("\n" * 10)
            return response.json()["value"]
    except:
        sys.exit()
        

def post(url = api_config.URL, api = '', token = ''):
    #token = get_token_authentication()
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'vmware-api-session-id': token,
    'Cache-Control': "no-cache",
    }

    post_url = api_config.URL + "rest" + api
    print("\n")
    print("*"*50,"Executing POST with the vCenter :",post_url,"*"*50)
    try:
        post_response = requests.post(post_url, headers = headers, verify = False)
        print("The status code is: ", post_response.status_code)
        return(post_response)
    except:
        print("The response from vCenter is: ", post_response.text)
        print("Exiting the script - ERROR - ")
        sys.exit()    

   

