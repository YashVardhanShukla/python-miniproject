def vote(candidate, votes):
    if candidate in votes:
        votes[candidate] += 1
    else:
        print("Invalid candidate!")

def display_results(votes):
    print("Voting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

def main():
    candidates = ["B.J.P", "I.N.C", "A.A.P"]
    votes = {candidate: 0 for candidate in candidates}

    print("Welcome to the Voting System")
    print("Candidates:")
    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate}")

    while True:
        choice = input("Enter the number of your chosen candidate (or '0' to finish voting): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(candidates):
                vote(candidates[choice - 1], votes)
                print("Vote recorded!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input! Please enter a number.")

    display_results(votes)

if __name__ == "__main__":
    main()
