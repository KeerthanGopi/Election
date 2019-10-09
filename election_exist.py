
class election_state():
    def exists(post, get):
        print("Voting Machine:\n1.Create Election\n2.Choose Election(to vote)\n3.Election Status\n4.Exit")
        id1 = input("Enter id: ")
        print()

        response = get.election_details(command_id = 0)
        if response:
            einfo = response.json()['results'][0]['values']
            if id1 == '1':
                check = False
                while not check:
                    election_name = input("Enter Election Name: ")
                    check = False
                    for i in range(0 , len(einfo)):
                        if name == einfo[i][1]:
                            check = True
                            print("Name already in use.\n")
                            print("Names in use:")
                            for i in range(0, len(einfo)):
                                print(i + 1, '. ', einfo[i][1], sep = '')

                cno = 's'
                while not(cno.isdigit() and cno !='0'):
                    cno = input("Enter number of candidates: ")
                        check = True
                    elif cno == '0':
                        print("0 is not a valid number for candidates")
                    else:
                        print("Not a valid number")
                cno = int(cno)

                candidate_name = []
                count = 0
                while count < cno:
                    cnam = input("Enter candidate name: ").rstrip()
                    if cnam != " " and cnam != '':
                        candidate_name.append(cnam)
                        count += 1
                    else:
                        print("Invalid candidate_name")

                election = post.appending_tables(election_name = election_name)
                election = post.appending_tables(candidate_list = candidate_name, command = 1, election_id = str(int(einfo[-1][0]) + 1))
                print("Election has been created")

            elif id1 == '3' or id1 == '2':
                check = False
                while not check:
                    election_id = '0'
                    while not(election_id > '0' and election_id <= str(len(einfo))):
                        print("Election Names:")
                        for i in range(0, len(einfo)):
                            print(i + 1, '. ', einfo[i][1], sep = '' )
                        election_id = input("Enter id: ")
                        if not(election_id > '0' and election_id <= len(einfo)):
                            print("Invalid Number")
                    election_id = str(int(election_id) - 1)

                    check = False
                    for i in range(0 ,len(einfo)):
                        if election_id == str(einfo[i][0]):
                            cinfo = get_election_details(command_id = 1, election_id = election_id)
                            check = True
                            break
                        elif election_id == 'a' and id1 == '3':
                            cinfo = get_election_details(command_id = 1)
                            check = True
                            break

                    if not check:
                        print("Invalid id.\n")

                if id1 == '3':
                    if election_id != 'a':
                        print()
                        print("Election Name:", einfo[int(election_id) - 1][1])
                        print("Date Of Creation:", einfo[int(election_id) - 1][2])
                        print("Date Of Election Start:", einfo[int(election_id) - 1][3])
                        print('Candidate Names: ')
                        for i in range(0, len(cinfo)):
                            print(i + 1, ". ", cinfo[i][1], cinfo[i][2])
                    else:
                        for i in range(0, len(einfo)):
                            print()
                            print("Election Name:", einfo[i][1])
                            print("Date Of Creation:", einfo[i][2])
                            print("Date Of Election Start:", einfo[i][3])
                            print('Candidate Names: ')
                            count = 1
                            for j in range(0, len(cinfo)):
                                if int(cinfo[j][0]) == i + 1:
                                    print(count, ". ", cinfo[j][1], cinfo[j][2])
                                    count += 1
                            if i != len(einfo):
                                print()
                elif id1 == '2':
                    check = False
                    while not check:
                        for i in range(0, len(cinfo)):
                            print(i + 1, '. ', cinfo[i][1], sep = '' )
                        candidate_id = input("Enter id: ")
                        check = False
                        for i in range(0 ,len(cinfo)):
                            if int(candidate_id) == cinfo[i][3]:
                                check = True
                                break
                        if not check:
                            print("Invalid id.\n")
                    response = post.table_updater(election_id, candidate_id, cinfo, einfo)

            elif id1 == '4':
                break

            else:
                print("Enter Valid id.\n")
        else:
            print("Error")

    def not_exists(post):
        response = post.create_tables()
            if response:
                print("No Election Exists\nPlease Create Election")
                name = input("Enter Election Name: ")
                cno = 's'
                while not(cno.isdigit() and cno != '0'):
                    cno = input("Enter number of candidates: ")
                    if cno.isdigit() and cno != '0':
                        cno = int(cno)
                    elif cno == '0':
                        print("0 is not a valid number for candidates")
                    else:
                        print("Not a valid number")

                candidate_name = []
                election_id ='1'
                count = 0
                while count < cno:
                    cnam = input("Enter candidate name: ").rstrip()
                    if cnam != " " and cnam != '':
                        candidate_name.append(cnam)
                        count += 1
                    else:
                        print("Invalid candidate_name")
                election = post.appending_tables(election_name = election_name)
                election = post.appending_tables(candidate_list = candidate_name, command = 1, election_id = '1')
                print("Election has been made.")
            else:
                print("Error")




