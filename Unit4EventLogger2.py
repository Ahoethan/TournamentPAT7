TOTAL_INDIVIDUALS = 1
TOTAL_TEAMS = 2
TOTAL_MEMBERS = 2
TOTAL_EVENTS = 2

class Tournament:
    def __init__(self, totalIndividuals, totalTeams, totalMembers, totalEvents):
        self.totalIndividuals = totalIndividuals
        self.totalTeams = totalTeams
        self.totalMembers = totalMembers
        self.totalEvents = totalEvents
        self.individuals = []
        self.teams = {}
        self.events = []
        self.individualScores = {}
        self.teamScores = {}
        self.rankScores = [10, 7, 5, 3]
    def addEvents(self):
        print("Please enter an event name: ")
        while len(self.events) < self.totalEvents:
            eventName = input(f"Event {len(self.events) + 1}: ")
            if not all(sections.isalpha() for sections in eventName.split()):
                print(" Please enter a valid event name, only allows alphabetical letters.")
            elif eventName in self.events:
                print("Please enter a unique event name.")
            else:
                self.events.append(eventName)

        print(f"Added {eventName}. Current events entered: {self.events}")

    def addIndividuals(self):
        print("Please enter individual name: ")
        while len(self.individuals) < self.totalIndividuals:
            individualName = input(f"Individuals {len(self.individuals) + 1}: ")
            if not all(sections.isalpha() for sections in individualName.split()):
                print(" Please enter a valid individual name, only allows alphabetical letters.")
            elif individualName in self.individuals:
                print("Please enter a unique individual name.")
            else:
                self.individuals.append(individualName)
                self.individualScores[individualName] = 0
        print(f"Added {individualName}. Current individuals entered: {self.individuals}")

    def addTeams(self):
        print("Please enter a team name: ")
        while len(self.teams) < self.totalTeams:
            teamName = input(f"Team {len(self.teams) + 1}: ")
            if not all(sections.isalpha() for sections in teamName.split()):
                print("Please enter a valid team name, only allows for alphabetical letters.")
            elif teamName in self.teams:
                print("Please enter a unique team name.")
            else:
                members = []
                print(f"Please enter {self.totalMembers} members for team '{teamName}':")
                while len(members) < self.totalMembers:
                    memberName = input("Please enter a member name:")
                    if not all(sections.isalpha() for sections in memberName.split()):
                        print("Please enter a valid name, only allows for alphabetical letters.")
                    elif memberName in members:
                        print("Please enter a unique name.")
                    else:
                        members.append(memberName)
                        print(f"Added member {memberName} to the team {teamName}")
                self.teams[teamName] = members
                self.teamScores[teamName] = 0
                print(f"{memberName} has been added to the team '{teamName}'.")
            print("All teams have been added:")
            for team, members in self.teams.items():
                print(f"The team {team} with {members} has been added")

    def eventScores(self):
        for event in self.events:
            print(f"Scores for event: {event}")
            eventType = input("Is this an individual or team event? (I/T): ")
            if eventType == "I":
                print("Ranks of Individuals in this event, please enter the indviduals in the order of rank:")
                print(f"All individuals: {', '.join(self.individuals)}")
                sortedIndividuals = input("Enter ranked individuals separated by commas: ").split(",")
                sortedIndividuals = [ind.strip() for ind in sortedIndividuals]
                for rank, individual, in enumerate(sortedIndividuals):
                    if individual in self.individualScores and rank < len(self.rankScores):
                        self.individualScores[individual] += self.rankScores[rank]
                    else:
                        print(f"Invalid individual name or rank position.")

            elif eventType == "T":
                print("Ranks of Teams in this event, please enter the teams in the order of rank:")
                print(f"All teams: {', '.join(self.teams.keys())}")
                sortedTeams = input("Enter ranked teams separated by commas: ").split(",")
                sortedTeams = [team.strip() for team in sortedTeams]
                for rank, team in enumerate(sortedTeams):
                    if team in self.teamScores and rank < len(self.rankScores):
                        self.teamScores[team] += self.rankScores[rank]
                    else:
                        print(f"Invalid team name or rank position.")
            else:
                print("Invalid input, please choose between individual or team. (I/T)")

    def displayAll(self):
        print("Tournament Setup Summary:")
        print(f"Total Individuals: {len(self.individuals)}")
        print(f"Individuals: {self.individuals}")
        print(f"Total Teams: {len(self.teams)}")
        for team, members in self.teams.items():
            print(f"Team '{team}' And the team's memebers are: {members}")
        print(f"Total Events: {len(self.events)}")
        print(f"Events: {self.events}")

        print("Final Scores:")
        print("Individual Scores:")
        for individual, score in self.individualScores.items():
            print(f"{individual}: {score}")
        print("Team Scores:")
        for team, score in self.teamScores.items():
            print(f"{team}: {score}")

    



tournament = Tournament(TOTAL_INDIVIDUALS, TOTAL_TEAMS, TOTAL_MEMBERS, TOTAL_EVENTS)
tournament.addIndividuals()
tournament.addTeams()
tournament.addEvents()
tournament.eventScores()
tournament.displayAll()