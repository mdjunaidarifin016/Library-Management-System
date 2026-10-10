import json 

def load_data():
    try:
        with open ("library.json","r") as f :
            return json.load(f)
    except FileNotFoundError:
        return []   
    except json.JSONDecodeError:
        return []
def save_data(content):
    with open ("library.json","w") as f :
        json.dump(content,f)

class LibraryManagement:
    def __init__(self,id):
        self.id=id 
    def add_book(self,title,author):
        data=load_data()
        for d in data:
            if d["id"]==self.id:
                return "book with same id is already available"
        data.append({"id":self.id,"title":title,"author":author,"availability":"available"})
        save_data(data)
        return "Book added successfully"

    def veiw_all_books(self):
        data=load_data()
        return data
    def search_book(self):
        data=load_data()
        for d in data:
            if d["id"]==self.id :
                return d
        return "Book not found" 
    
    def borrow_book(self):
        data=load_data()
        for d in data:
            if d["id"] == self.id :
                if d["availability"] == "available" :
                    d["availability"]="borrowed"
                    save_data(data)
                    return "borrow successfully"
                else :
                    return "Book is already borrowed"
        return "Book not found"
           
    def return_book(self):
        data=load_data()
        for d in data :
            if d["id"] == self.id :
                if d["availability"] == "borrowed":
                    d["availability"] = "available"
                    save_data(data)
                    return "return successfully"
                else:
                    return "Book is already returned"
        return "Book not found"
    def delete_book(self):
        book_found=False
        new_list=[]
        data=load_data()
        for d in data :
            if d["id"]==self.id:
                book_found=True
                if d["availability"] != "available":
                    return "book is not available"
        if not book_found:
            return "Book not found"
        choice=input("Are you sure, you want to delete this book(y/n):").lower()
        if choice == "y":
            for d in data:
                if d["id"] != self.id :
                    new_list.append(d)
            if len(new_list)==len(data):
                return "Book not deleted"
            data=new_list
            save_data(data)
            return "book deleted successfully"
        elif choice == "n":
            return "Deletion cancelled"
        else:
            return "please enter a valid choice"

def menu():
    i_d=input("Enter the book ID:")
    n=LibraryManagement(i_d)
    while True :
        print("========Library Management========")
        print("1.Add Book")
        print("2.Veiw All Book")
        print("3.Search Book")
        print("4.Borrow Book")
        print("5.Return Book")
        print("6.Delete book")
        print("7.Give ID again")
        print("8.Exit")

        try:
            choice=int(input("Enter a choice:"))
        except ValueError:
            print("Enter a valid choice!")
            continue
        if choice == 1 :
            title=input("Enter the title of the book:").capitalize()
            author=input("Enter the name of the author:").capitalize()
            print(n.add_book(title,author))
        elif choice == 2 :
            print(n.veiw_all_book())
        elif choice == 3:
            print (n.search_book())
        elif choice == 4:
            print(n.borrow_book())
        elif choice == 5 :
            print(n.return_book())
        elif choice == 6 :
            print(n.delete_book())
        elif choice == 7:
            new_i_d=input("Enter Book ID:")
            n=LibraryManagement(new_i_d)
        elif choice == 8 :
            print("Thank You")
            break
        else:
            print("Enter a valid choice")

menu()
        

