import requests

def send_group_message():
    try:
        # Token.txt से टोकन पढ़ें
        with open("Token.txt", "r") as token_file:
            access_token = token_file.read().strip()
        
        # Fil.txt से ग्रुप आईडी पढ़ें
        with open("Fil.txt", "r") as file:
            group_id = file.read().strip()
        
        # CONVO.txt से संदेश पढ़ें
        with open("CONVO.txt", "r") as convo_file:
            message = convo_file.read().strip()
        
        # Facebook Graph API URL
        url = f"https://graph.facebook.com/{group_id}/feed"
        params = {
            "message": message,
            "access_token": access_token
        }
        
        # POST Request भेजें
        response = requests.post(url, data=params)
        
        # Response प्रिंट करें
        print(response.json())
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_group_message()
