class Player:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def __del__(self):
        print(f"Player destroyed: {self.name}")


class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)

    def roster(self):
        return [f"{p.name} ({p.position})" for p in self.players]

    def __del__(self):
        print(f"Team disbanded: {self.team_name}")


if __name__ == "__main__":
    juan = Player("Juan", "Guard")
    pedro = Player("Pedro", "Center")

    cebu_team = Team("Cebu Sharks")
    cebu_team.add_player(juan)
    cebu_team.add_player(pedro)
    print(f"{cebu_team.team_name} roster: {cebu_team.roster()}")

    print("\nExecuting: del cebu_team")
    del cebu_team

    print("\nPlayers after team deletion:")
    print(f"Still active -> {juan.name}")
    print(f"Still active -> {pedro.name}")

    new_team = Team("Davao Eagles")
    new_team.add_player(juan)
    print(f"{new_team.team_name} roster: {new_team.roster()}")
