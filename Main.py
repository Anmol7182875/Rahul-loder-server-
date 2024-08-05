import requests
import time

# Token और अन्य फाइलें पढ़ें
with open('Token.txt', 'r') as f:
    access_token = f.read().strip()

with open('Fil.txt', 'r') as f:
    post_ids = [line.strip() for line in f]

with open('CONVO.txt', 'r') as f:
    comments = [line.strip() for line in f]

def post_comment(post_id, comment):
    url = f'https://graph.facebook.com/{post_id}/comments'
    payload = {
        'message': comment,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    for post_id in post_ids:
        for comment in comments:
            response = post_comment(post_id, comment)
            print(f'Comment posted: {response}')
            time.sleep(5)  # समय अंतराल

if __name__ == "__main__":
    main()
