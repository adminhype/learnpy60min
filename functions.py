absender = input("Wer ist der Absender? ")



def generate_newsletter(absender):
    name = input("An wen geht diese Nachricht? ")
    print(f"Hey {name}")
    print("")
    print("Mit dieser E-Mail möchte ich dich über meine neue Adresse informieren.")
    print("")
    print("Musterstraße 123")
    print("1234 Musterhausen")
    print("")
    print("Viele Grüße")
    print(f"{absender}")

generate_newsletter(absender)
generate_newsletter(absender)
generate_newsletter(absender)
generate_newsletter(absender)