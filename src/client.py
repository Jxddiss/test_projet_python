import requests

BASE_URL = "http://localhost:5000/books"

def print_response(response):
    print(f"[Statut {response.status_code}]\n")
    try:
        print(response.json())
    except:
        print("Pas de contenu JSON")
    print("-" * 50)

def interactive_client():
    while True:
        choice = input()
        
        # Afficher tous les livres
        if choice == '1':
            response = requests.get(BASE_URL)
            print_response(response)
        
        # Chercher par ID
        elif choice == '2':
            book_id = input()
            response = requests.get(f"{BASE_URL}/{book_id}")
            print_response(response)
        
        # Ajouter un livre
        elif choice == '3':
            title = input()
            author = input()
            year = input()
            response = requests.post(BASE_URL, json={
                "title": title,
                "author": author,
                "year": int(year)
            })
            print_response(response)
        
        # Modifier un livre
        elif choice == '4':
            book_id = input()
            title = input()
            author = input()
            year = input()
            
            update_data = {}
            if title: update_data["title"] = title
            if author: update_data["author"] = author
            if year: update_data["year"] = int(year)
            
            response = requests.put(f"{BASE_URL}/{book_id}", json=update_data)
            print_response(response)
        
        # Supprimer un livre
        elif choice == '5':
            book_id = input()
            response = requests.delete(f"{BASE_URL}/{book_id}")
            print_response(response)
        
        # Quitter
        elif choice == '6':
            print("Au revoir!")
            break
        
        else:
            print("\nOption invalide, réessayez!")

if __name__ == "__main__":
    try:
        interactive_client()
    except requests.exceptions.ConnectionError:
        print("Erreur: L'API ne semble pas démarrée! Lancez 'python app.py' d'abord.")
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur")