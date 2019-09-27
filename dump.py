from get_election_details import get_election_details as edata
from configparser import ConfigParser as CP
from post_election_details import post_election_details as cp

config = CP()
config.read('election.cnf')
sad = cp(config)
response = sad.post_after_creation(election_name = "sa1", command_id = 0)
print(response)
