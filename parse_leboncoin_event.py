import json
import re
from lxml import etree
def parse_leboncoin_event(event):
    event = json.loads(event)

    # Extraction des données
    from_email_match = re.search(r'<(.+?)>', event['to'])
    from_email = from_email_match.group(1) if from_email_match else ""

    
    to_emails = [email.strip() for email in event['to'].split(",")]

   
    workspace_email = event['to'].split('<')[-1].strip('>')
    workspace_id, workspace_name = workspace_email.split('@')

   
    subject_match = re.search(r'"(.+?)"', event['subject'])
    brand_model = subject_match.group(1) if subject_match else ""
    brand, model = brand_model.split(" ", 1) if brand_model else ("", "")

   
    message = event['text']

  
    customer_info = {
        "firstname": event['text'].split("Prénom : ")[1].split("\n")[0].strip(),
        "lastname": event['text'].split("Nom : ")[1].split("\n")[0].strip(),
        "customer_phone_number": event['text'].split("Téléphone : ")[1].split("\n")[0].strip(),
        "customer_email": event['text'].split("E-mail : ")[1].split("\n")[0].strip(),
    }

 
    lead_link = re.search(r'href="([^"]+)"', event['text']).group(1) if re.search(r'href="([^"]+)"', event['text']) else ""

    
    result = {
        "channel": "leboncoin",
        "from_email": from_email,
        "to_email": event['to'],
        "workspace_name": workspace_name,
        "workspace_id": workspace_id,
        "brand": brand,
        "model": model,
        "message": message,
        "firstname": customer_info["firstname"],
        "lastname": customer_info["lastname"],
        "customer_phone_number": customer_info["customer_phone_number"],
        "customer_email": customer_info["customer_email"],
        "links": {
            "lead": lead_link
        },
        "subject": event['subject'],
        "contact_info": [
            {
                "type": "email",
                "value": customer_info["customer_email"]
            },
            {
                "type": "phone_number",
                "value": customer_info["customer_phone_number"]
            }
        ]
    }

    return result
