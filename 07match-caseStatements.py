#Match-Case Statements
#Just like if-else, but less code

day = input("Enter the day today: ")

match day:
    case "monday":
        print("Its Monday today, get ready for work")
    case "tuesday":
        print("Its Tuesday today, work day")
    case "wednesday":
        print("Its Wednesday today, work day")
    case "thursday":
        print("Its Thursday today, work day")
    case "friday":
        print("Its Friday today, half work day")
    case "saturday":
        print("Its Saturday today, holiday day")
    case "sunday":
        print("Its Sunday today, international holiday day")
    case _:
        print("Pls enter a valid day")