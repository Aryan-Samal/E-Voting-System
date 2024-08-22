import hashlib

class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.votes = {}
        self.hashed_votes = set()
    
    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"Candidate {candidate_name} is already in the system.")
        else:
            self.candidates[candidate_name] = 0
            print(f"Candidate {candidate_name} added successfully.")
    
    def display_candidates(self):
        print("\nList of candidates:")
        for candidate in self.candidates:
            print(f"- {candidate}")
    
    def cast_vote(self, voter_id, candidate_name):

        voter_hash = hashlib.sha256(voter_id.encode()).hexdigest()
        
        if voter_hash in self.hashed_votes:
            print("You have already voted. Duplicate votes are not allowed.")
            return
        
        if candidate_name not in self.candidates:
            print(f"Candidate {candidate_name} does not exist. Vote not recorded.")
            return
        
        self.candidates[candidate_name] += 1
        self.hashed_votes.add(voter_hash)
        print(f"Vote cast for {candidate_name}. Thank you for voting!")
    
    def display_results(self):
        print("\nElection Results:")
        for candidate, vote_count in self.candidates.items():
            print(f"{candidate}: {vote_count} votes")
    
    def ensure_integrity(self):
        data_to_check = "".join([f"{candidate}:{vote_count}" for candidate, vote_count in self.candidates.items()])
        integrity_hash = hashlib.sha256(data_to_check.encode()).hexdigest()
        print(f"\nIntegrity Check Hash: {integrity_hash}")
        print("This hash can be used to verify that the data has not been tampered with.")


def main():
    voting_system = VotingSystem()
    
    voting_system.add_candidate("Candidate 1")
    voting_system.add_candidate("Candidate 2")
    voting_system.add_candidate("Candidate 3")
    
    while True:
        print("\nMenu:")
        print("1. Display Candidates")
        print("2. Cast Vote")
        print("3. Display Results")
        print("4. Integrity Check")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            voting_system.display_candidates()
        
        elif choice == '2':
            voter_id = input("Enter your voter ID: ")
            candidate_name = input("Enter the candidate's name you want to vote for: ")
            voting_system.cast_vote(voter_id, candidate_name)
        
        elif choice == '3':
            voting_system.display_results()
        
        elif choice == '4':
            voting_system.ensure_integrity()
        
        elif choice == '5':
            print("Exiting the voting system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
