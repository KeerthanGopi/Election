from get_election_details import get_election_details as edata
from configparser import ConfigParser as CP
from post_election_details import post_election_details as cp

config = CP()
config.read('election.cnf')
sad = cp(config)
sad = sad.post(election_name = "sa1", command_id = 0)
print(sad)
