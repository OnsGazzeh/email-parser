from parse_leboncoin_event import parse_leboncoin_event


def test_parse_leboncoin_event():
    with open("events/leboncoin.json", "r") as f:
        event = f.read()

    result = parse_leboncoin_event(event)
    assert result == {
        "channel": "leboncoin",
        "from_email": "message@leboncoin.fr",
        "to_email": "abc.ab77535e-6fe7-4b44-82bb-64c6f82ef5a4@prochaineauto.com",
        "workspace_name": "abc",
        "workspace_id": "ab77535e-6fe7-4b44-82bb-64c6f82ef5a4",
        "brand": "Mazda",
        "model": "CX-3 2.0L Skyactiv-G 120 4x2 Signature",
        "message": "« Bonjour, est-ce un véhicule d’importation a-t-il été entretenu dans le réseau Mazda quel est le pourcentage d’usure des pneus et quelles sont les impacts rayures ou accident de la carrosserie merci de me préciser également quelles sont les frais de mise en service cordialement »",
        "firstname": "leonard",
        "lastname": "oxxo",
        "customer_phone_number": "0123456789",
        "customer_email": "leonard@orange.fr",
        "links": {
            "lead": "https://www.leboncoin.fr/voitures/2085528565.htm"
        },
        "subject": "Nouveau message concernant l\'annonce \"Mazda CX-3 2.0L Skyactiv-G 120 4x2 Signature\" sur leboncoin",
        "contact_info": [
            {
                "type": "email",
                "value": "leonard@orange.fr"
            },
            {
                "type": "phone_number",
                "value": "0123456789"
            }
        ]
    }

