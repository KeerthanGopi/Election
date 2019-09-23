import requests
import configparser
import time
import socket

class get_election_details():
    def __init__(self, config):

        config = config['rqlite']
        self.ip = config['ip']
        self.port = config['port']
        self.url_get = 'http://' + self.ip + ':' + self.port + '/db/query?'

        self.headers = {'Content-type' : 'application/json'}

    def election_info(self, election_id = 'a', command_id = 4, candidate_id = 0):
        tables = ["ElectionName", "CandidatesName"]
        if command_id != 0 and command_id != 1:
            return "Error function does not satisfy your needs"
        else:
            command = tables[command_id]
        success = False
        tries = 0
        while tries <= 3:
            host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = host.connect_ex((self.ip, int(self.port)))
            host.close()
            if result == 0:
                while not success:
                    try:
                        query = 'SELECT * FROM ' + command
                        if election_id != 'a':
                            query += ' WHERE election_id = ' + election_id
                            if candidate_id != 0:
                                query += ' AND candidate_id = ' + str(candidate_id)
                        select = {'q': query}

                        response = requests.get(url = self.url_get, params = select, headers = self.headers)
                        required_info = response.json()['results'][0]

                        if 'values' in required_info:
                            required_info = required_info['values']
                            return required_info
                        else:
                            return None
                        success = True
                    except KeyboardInterrupt:
                        exit = input("Do you wanna quit(y/n): ")
                        if exit == 'y':
                            print("Exiting on command")
                            break
                    except:
                        pass
            else:
                tries += 1
                if tries == 4:
                    print("Contact EVM Manager")
                    print("Exiting")
                    print("ERROR_CODE: 1", command[0], "\n", sep = '')
                    return '1' + command[0]

                print("Port 4001 down")
                print("Server not running.")
                print("Waiting for 5s\n")
                time.sleep(5)

