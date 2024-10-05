#######PHISHING EMAIL DETECTOR###
# ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡
# ♡



#dictionary  ♡ ♡ ♡ ♡ ♡ ♡ ♡
emails = [
{"sender": "unknown@scammymcscammer.com", "subject": "YOU WIN!!", "BODY": "CLICK HERE STUOOPID."},
{"sender": "friend@yahoo.com", "subject": "hi", "body": "wagwan???"}    
]

sus_words = ["prize", "WIN", "scam", "CLICK HERE"]


# THE LOOP ♡ ♡ ♡ ♡ ♡ ♡ ♡
for email in emails:
        if "unknown" in email["sender"]:
                print(f"SUS SENDER ALERT: {EMAIL['sender']})
        else:
                      for word in sus_words: 
                      if word in email["body"]:
                      print(f"suspicvious content detected in email frommmmmmm {email['sender']}")              


