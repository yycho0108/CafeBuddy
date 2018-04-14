def table_score(person, table):
    """ 
    Returns score of table based on personal preferences and table data.
    see test() in score.py for more information.
    """
    table_person = set(table['person'])

    friend = set(person['friend']).intersection(table_person)
    acquaintance = set(person['friend']).intersection(table_person)
    enemy = set(person['friend']).intersection(table_person)

    preference = person['preference']

    if len(table_person) == 0:
        return preference['empty']
    else:
        score = 0
        score += len(friend) * preference['friend']
        score += len(acquaintance) * preference['acquaintance']
        score += len(enemy) * preference['enemy']
        n_stranger = len(table_person) - len(friend) - len(acquaintance) - len(enemy)
        score += n_stranger * preference['stranger']
        return score

def sort_table(person, tables):
    """
    sort table by the scoring metric
    returns [(score[i], table_id[i]) for i in range(n)]
    """
    scores = [table_score(person, table) for table in tables.itervalues()]
    return sorted(zip(scores, tables.iterkeys()))

def test():
    table_data = {
            'table_1' : {
                'capacity' : 6,
                'location' : (25.0, 34.0),
                'person' : ['a','b','c','d'],
                },
            'table_2' : {
                'capacity' : 5,
                'location' : (35.0, 34.0),
                'person' : ['e','f','h'],
                }
            }
    
    person_data = {
            'friend' : ['a','b','c','d'],
            'acquaintance' : ['e','f','g'], # or other features, like "classes"
            'enemy' : ['h'],
            'preference' : { # preference score
                'friend' : 2,
                'acquaintance' : 1,
                'empty'  : 0,
                'stranger' : -1,
                'enemy' : -2
                }
            }
    res = sort_table(person_data, table_data)
    print('Test Result : {}'.format(res))

if __name__ == "__main__":
    test()
