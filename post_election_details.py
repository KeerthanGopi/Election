import requests
import configparser
import time
from configparser import ConfigParser
from get_election_details import get_election_details

class post_election_details():
    def __init__(self):

        config = ConfigParser()
        config.read('election.cnf')
        config = config['rqlite']
        self.ip = config['ip']
        self.port = config['port']
        self.url_post = 'http://' + self.ip + ':' + self.port + '/db/execute?'
        self.headers = {'Content-type' : 'application/json'}

    def create_tables(self):
        try:
            election_data = '["CREATE TABLE ElectionName (election_id INTEGER not null PRIMARY KEY, election_name text, DateOfCreation text, DateOfStart Text DEFAULT ' + "'NOT STARTED'" + ')",'
            election_data += '"CREATE TABLE CandidatesName (election_id text,  candidate_name text, votes INTEGER DEFAULT 0, candidate_id INTEGER not null, FOREIGN KEY (election_id) REFERENCES ElectionName(election_id))"]'

            count = 0
            while count < 3:
                response = requests.post(url = self.url_post, headers = self.headers, data = query)
                response = response.json()['results'][0]
                if 'error' not in response:
                    return response
                time.sleep(2)
                count += 1
            print("ERROR CODE: 3" + command[0])
        except KeyboardInterrupt:
            raise

        except requests.ConnectionError:
            print("Port 4001 down")
            tries += 1
            if tries == 4:
                print("Contact EVM Manager")
                print("Exiting")
                print("ERROR_CODE: 2", command[0], "\n", sep = '')
                return None
            print("Server not running.")
            print("Waiting for 5s\n")
            time.sleep(5)
        except:
            return None

    def table_updater(election_id, candidate_id, candidate_info, election_info):
        try:
            if election_info[int(election_id) - 1][-1] == 'NOT STARTED':
                date_updater = '[ "UPDATE ElectionName SET DateOfStart = CURRENT_DATE WHERE election_id =  '+ election_id + '" ]'
                count = 0
                while count < 3:
                    response = requests.post(url = self.url_post, headers = self.headers, data = query)
                    response = response.json()['results'][0]
                    if 'error' not in response:
                        return response
                    time.sleep(2)
                    count += 1

            vote_adder = '[ "UPDATE CandidatesName SET votes = votes + 1 WHERE candidate_id = ' + candidate_id + ' AND election_id = ' + str(candidate_info[int(candidate_id) - 1][0])+ '" ]'
                count = 0
                while count < 3:
                    response = requests.post(url = self.url_post, headers = self.headers, data = query)
                    response = response.json()['results'][0]
                    if 'error' not in response:
                        return response
                    time.sleep(2)
                    count += 1
        except KeyboardInterrupt:
            raise

        except requests.ConnectionError:
            print("Port 4001 down")
            tries += 1
            if tries == 4:
                print("Contact EVM Manager")
                print("Exiting")
                print("ERROR_CODE: 2", command[0], "\n", sep = '')
                return None
            print("Server not running.")
            print("Waiting for 5s\n")
            time.sleep(5)
        except:
            return None


    def table_appender(self, command_id = 0, election_name = '', candidate_list = []):
        tables = ["ElectionName", "CandidatesName"]

        response = get_election_details(command_id = 0).json()['results'][0]['values']
        election_id = str(int(response[-1][0]) + 1)
        try:
            query = '[ "INSERT INTO ' + command
            if command_id == 1:
                query += "(election_name, DateOfCreation) VALUES(\\\"" + election_name + "\\\", CURRENT_DATE)\""

                for i in range(0, len(candidate_list)):
                    print(i + 1, ". ", candidate_list[i], sep = "")
                    query += '(\\ \"' + candidate_list[i] + '\\ \",' + election_id +  ',' + str(i + 1) + ') '
                    if i != len(candidate_list):
                        query += ','
            elif command_id == 0:
                query += '(election_name, DateOfCreation) VALUES(\\"' + election_name +'\\", CURRENT_DATE)"'

            query += " ]"


            count = 0
            while count < 3:
                response = requests.post(url = self.url_post, headers = self.headers, data = query)
                response = response.json()['results'][0]
                if 'error' not in response:
                    return response
                time.sleep(2)
                count += 1
            else:
                print("ERROR CODE: 3" + command[0])
                return None

        except KeyboardInterrupt:
            raise

        except requests.ConnectionError:
            print("Port 4001 down")
            tries += 1
            if tries == 4:
                print("Contact EVM Manager")
                print("Exiting")
                print("ERROR_CODE: 2", command[0], "\n", sep = '')
                return None
            print("Server not running.")
            print("Waiting for 5s\n")
            time.sleep(5)
        except:
            return None

