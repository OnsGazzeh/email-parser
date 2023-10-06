import json
import re
#from lxml import etree

def parse_lacentrale_event(event):

      
        event_data = json.loads(event)

        #Extraction des données
        subject = event_data.get("subject", "")
        from_email = event_data.get("from", "")
        to_email = event_data.get("to", "").split(',')[0].strip()
        message = event_data.get("text", "")
        firstname, lastname = "", ""

        # nom
        from_name = event_data.get("from", "")
        if from_name:
            parts = from_name.split()
            if len(parts) >= 2:
                firstname = parts[0].strip("\"")
                lastname = parts[1].strip("\"")

        # marque
        subject_parts = subject.split("-")
        brand_model = subject_parts[-1].strip()
        brand, model = brand_model.split(" ", 1)

        
        result = {
            "channel": "lacentrale",
            "from_email": from_email,
            "to_email": to_email,
            "workspace_name": "",
            "workspace_id": "",
            "brand": brand.strip(),
            "model": model.strip(),
            "message": message.strip(),
            "firstname": firstname.strip(),
            "lastname": lastname.strip(),
            "customer_email": from_email,
            "subject": subject.strip(),
            "contact_info": [
                {
                    "type": "email",
                    "value": from_email
                }
            ]
        }

        return result

