from post_election_details import post_election_details as cp

sad = cp()
response = sad.post_after_creation(election_name = "sa1", command_id = 0)
print(response)
