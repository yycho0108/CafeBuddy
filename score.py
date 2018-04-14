def table_score(person, table):
    """ 
    Returns score of table based on personal preferences and table data.
    see test() in score.py for more information.
    """
    table_person = set(table['person'])

    friend = set(person.get('friend', [])).intersection(table_person)
    acquaintance = set(person.get('acquaintance', [])).intersection(table_person)
    enemy = set(person.get('enemy', [])).intersection(table_person)

    # default weight
    weight = person.get('weight', { 
        'friend' : 2,
        'acquaintance' : 1,
        'empty'  : 0,
        'stranger' : -1,
        'enemy' : -2
        })

    if len(table_person) == 0:
        return weight['empty']
    else:
        score = 0
        score += len(friend) * weight['friend']
        score += len(acquaintance) * weight['acquaintance']
        score += len(enemy) * weight['enemy']
        n_stranger = len(table_person) - len(friend) - len(acquaintance) - len(enemy)
        return score

def sort_table(pref, tables):
    """
    sort table by the scoring metric
    returns [(score[i], table_id[i]) for i in range(n)]
    """
    scores = [table_score(pref, table) for _, table in tables.items()]
    return sorted(zip(scores, tables.iterkeys()), reverse=True)

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
            'weight' : { # preference score
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
