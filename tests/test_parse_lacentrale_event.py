from parse_lacentrale_event import parse_lacentrale_event


def test_parse_lacentrale_event():
    with open("events/lacentrale.json", "r") as f:
        event = f.read()

    result = parse_lacentrale_event(event)
    assert result == {
        "channel": "lacentrale",
        "from_email": "no_reply@lacentrale.fr",
        "to_email": "volkswagen.f870e411-02bf-4a32-afa0-c7618d7e7315@prochaineauto.com",
        "workspace_name": "volkswagen",
        "workspace_id": "f870e411-02bf-4a32-afa0-c7618d7e7315",
        "brand": "SEAT",
        "model": "LEON III",
        "message": "bonjour. je possède un seat Léon 2 style 1.6 TDI de 2010 ,  250000km. pneu neuf , amotisseurs neuf , embrayage neuf . j'aimerais savoir si il y a une possibilité de reprise , et es-ce que vous pouvez faire une livraison à domicile , si achat .",
        "firstname": "jean-baptiste",
        "lastname": "roi",
        "customer_email": "1cc8bfd6-0009-50c9-9f29-1e6464a55fe2@messagerie.lacentrale.fr",
        "subject": "Nouveau message pour votre annonce E109620631 - SEAT LEON III (2) 1.6 TDI 115 START/STOP STYLE BUSINESS",
        "contact_info": [
            {
                "type": "email",
                "value": "1cc8bfd6-0009-50c9-9f29-1e6464a55fe2@messagerie.lacentrale.fr"
            }
        ]
    }
