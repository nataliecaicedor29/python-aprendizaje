#Candidates dictionary
candidates = {
    "Ana" : 0,
    "Carlos" : 0,
    "Pedro" : 0
}
votes = int(input("How many people will vote? "))

for i in range(votes):
    print("Candidates:", list(candidates.keys()))
    while True:
        vote = input("Enter your vote: ").title()
        if vote in candidates:
            candidates[vote] += 1
            break
        else:
            print(f"Invalid vote!please choose from: {list(candidates.keys())}")
    
print("\n--- Results ---")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes} votes")
    
winner = max(candidates, key=candidates.get)
print(f"The winner is {winner} with {candidates[winner]} votes!")