import json, sys
from pprint import pprint
from converter import PMCverter



def rename_dialogues(jsondict, out):
    new_dict = {}
    for dialogue in jsondict:
        # dialogue = jsondict[dialogue][0]['usr']
        new_dict.update({jsondict[dialogue][0]['usr']: jsondict[dialogue]})
    pprint(new_dict)
    out.write(json.dumps(new_dict, ensure_ascii=False).encode("utf-8"))


def slot_corrector(jsondict, out, slots):
    new_dict = {}
    d = 0
    for dialogue in jsondict:

        d += 1
        new_dialogue = []
        x = 0
        new_slots = []
        for turn in jsondict[dialogue]:
            x += 1
            new_turn = {'turn_idx': x}
            for dic in turn:
                new_values = {}
                # slots['slots'] = list(set(slots['slots']))
                if type(turn[dic]) == list:
                    for elem in turn[dic]:

                        if 'belief_state' in dic and elem:

                            if 'Store' not in elem[0]:

                                if elem in slots:
                                    # print(type(elem))
                                    print(elem, '\n\n###############\n\n', turn['usr'], turn['sys'])
                                    new_slot_value = input(
                                        "\n\n###############\n\nQuelle est la forme correcte (cle, valeur)? \n\n").rstrip()
                                    if new_slot_value:
                                        if ',' in new_slot_value:
                                            elem = new_slot_value.split(',')
                                        else:
                                            elem[1] = new_slot_value
                            if {elem[0]: elem[1]} not in new_slots:
                                new_slots.append({elem[0]: elem[1]})

                        if dic not in new_values:
                            new_values[dic] = [elem]
                        else:
                            new_values[dic].append(elem)

                else:
                    elem = turn[dic]
                    if dic not in new_values:
                        new_values[dic] = elem
                new_turn.update(new_values)
                # pprint(new_turn)
                # if 'slots' in new_turn :
                #     new_turn['slots']= []

            print(f' turn {x} and new slots : {new_slots}')
            new_turn['slots'] = [dic for dic in new_slots]
            new_dialogue.append(new_turn)
            new_turn = {}
            # pprint(new_dialogue)
            # sys.exit()

            # sys.exit()
        # pprint(new_dialogue)
        new_dict.update({dialogue: new_dialogue})
    out.write(json.dumps(new_dict, ensure_ascii=False, indent=4, sort_keys=True).encode("utf-8"))


def slot_filler(jsondict, out):
    new_dict = {}
    all_slots = {}
    for dialogue in jsondict:
        slots = {}
        new_dialogue = []
        for turn in jsondict[dialogue]:
            for dic in turn:
                if 'belief_state' in dic and type(turn[dic]) == list:
                    for elem in turn[dic]:
                        if elem:
                            if 'slots' not in slots:
                                slots['slots'] = [{elem[0]: elem[1]}]
                                if 'slots' not in all_slots:
                                    all_slots['slots'] = [{elem[0]: elem[1]}]
                            elif {elem[0]: elem[1]} not in slots['slots']:
                                slots['slots'].append({elem[0]: elem[1]})
                                all_slots['slots'].append({elem[0]: elem[1]})

            # slots['slots'] = list(set(slots['slots']))
            turn.update(slots)
            new_dialogue.append(turn)
        new_dict.update({dialogue: new_dialogue})
    out.write(json.dumps(new_dict, ensure_ascii=False, indent=4, sort_keys=True).encode("utf-8"))
    return [[cle, elem[cle]] for elem in all_slots['slots'] for cle in elem]


def entities_editor(jsondict, out):
    new_dict = {}
    l = len([dialogue for dialogue in jsondict])
    d = len([turn for dialogue in jsondict for turn in dialogue])
    print(d)
    for dialogue in jsondict:
        print(f'\n\nil reste {l} dialogues\n\n')
        l -= 1
        new_dialogue = []
        for turn in jsondict[dialogue]:
            turn['entities'] = []
            print(f'\n\nil reste {d} turns')
            d -= 1
            entities = []
            continu = True
            print(f'\n\n###\n\n{turn["usr"]}')
            while continu:
                entities.append(input("\n\n Définissez les entités sémantiques\n\n").rstrip())
                continu = bool(input("Continue, True or False \n\n"))
            for entity in entities:
                if entity:
                    try:
                        turn['entities'].append({entity.split(',')[0]: entity.split(',')[1]})
                    except IndexError:
                        entity = input(
                            f"\n\n ENTITE MAL DEFINIE {entity} Définissez les entités sémantiques\n\n").rstrip()
                        turn['entities'].append({entity.split(',')[0]: entity.split(',')[1]})

            print(turn['entities'])
            print(turn)
            new_dialogue.append(turn)
        new_dict.update({dialogue: new_dialogue})
        # sys.exit()
        out.write(json.dumps({dialogue: new_dialogue}, ensure_ascii=False, indent=4, sort_keys=True).encode("utf-8"))

def jsontocsv(jsondict, out):
    converter = PMCverter()
    
    convers = {}
    for elem in jsondict:
        convers[elem] = ""
        intents = {}
        entities = {}
        slots = {}
        speak = {}
        print(elem)
        for i in range(1, len(jsondict[elem])) :
            intents[i] = jsondict[elem][i]['intent']
            entities[i] = jsondict[elem][i]['entities']
            slots[i] = jsondict[elem][i]['slots']
            user  = converter.post_treatment_intent(jsondict[elem][i]['usr'])
            agent = converter.post_treatment_intent(jsondict[elem][i]['sys'][0])
            speak[i] = user+"\t"+agent
            convers[elem] += '\t'+speak[i]+'\t'+str(intents[i])+'\t'+str(entities[i])+'\t'+str(slots[i])+'\n'
        convers[elem] += '\n'
    # pprint(convers)
    out.write('ID\tUSER\tAGENT\tINTENT\tENTITIES\tSLOTS\n')
    for elem in convers : 
        out.write(elem+convers[elem])




if __name__ == '__main__':

    jsondict = json.load(open('../input/entitiesintents_dialogues1-100.json'),encoding='utf-8')
    out = open('../input/new_dialogues1-100.csv', 'w')
    # rename_dialogues(jsondict, out)
    # jsondict = json.load(open('../input/new_dialogues1-100.json'), encoding='utf-8')
    # out = open('../input/brandnew_dialogues1-100.json', 'wb')
    # slots = [['Store name', 'Parfum moins cher'], ['date', '09'], ["deliverycost", "free"],['order_nbr', 'email'], ['status', 'en cours de traitement'], ['error', 'no'], ['step', 'delivery'], ['operation', 'payment'], ['cache', 'unable'], ['order_nbr', '00'], ['country', 'USA'], ['order_nbr', '00'], ['order_nbr', '02 00'], ['status', 'processing'], ['email', 'not recieved'], ['complaint', 'splitted delivery'], ['email', 'details'], ['email', 'resend'], ['payment_tool', 'master card'], ['error', 'yes'], ['payment_tool', 'no paypal'], ['place', 'France'], ['order_nbr', '00'], ['complaint', 'bad add'], ['article', 'lolita'], ['price', '36.99'], ['size', '100ml'], ['add', 'yes'], ['error', 'no'], ['payment_tool', 'cb'], ['step', 'payment'], ['payment_tool', 'invalid cb'], ['order_nbr', '00'], ['status', 'unchanged'], ['order_nbr', '00'], ['order_nbr', '00'], ['payment_tool', 'no paypal'], ['payment_tool', 'cb'], ['step', 'delivery'], ['article', 'fdt'], ['profile', 'mate'], ['order_nbr', '00'], ['code', 'NOEL5'], ['uppercase', 'yes'], ['code', 'NOEL10'], ['order_nbr', '00'], ['country', 'USA'], ['operation', 'resend'], ['address', 'address'], ['article', 'valentino'], ['operation', 'refund'], ['place', 'domicile'], ['order_nbr', '00'], ['place', 'point-relais'], ['device', 'computer'], ['error', 'yes'], ['payment_tool', 'cb'], ['topic', 'news'], ['info', 'order 00'], ['complaint', 'no answer'], ['operation', 'resend'], ['code', 'mdm10'], ['article', 'dorella'], ['article', 'correge'], ['email', 'eùaom'], ['address', 'address75'], ['complaint', 'long phone'], ['complaint', 'expensive long phone'], ['email', 'email'], ['address', 'address'], ['complaint', 'fraud'], ['pwd', 'azerty'], ['order_nbr', '00'], ['order_nbr', '00'], ['order_nbr', '00'], ['email', 'email'], ['status', 'lost'], ['operation', 'resend'], ['order_nbr', '00'], ['order_nbr', '03'], ['operation', 'returned'], ['place', 'home'], ['place', 'point relais'], ['operation', 'resend'], ['place', 'point-relais'], ['order_nbr', '00'], ['date', '24/12'], ['separated', 'returned'], ['order_nbr', '?'], ['data', 'password'], ['order_nbr', '00'], ['order_nbr', '00'], ['complaint', 'no package'], ['email', 'email'], ['reinit', 'password'], ['reinit', 'yes'], ['error', 'yes'], ['step', 'authentification'], ['email', 'email'], ['reinit', 'yes'], ['code', 'name1'], ['email', 'email'], ['code', 'amour'], ['uppercase', 'yes'], ['account_connection', 'yes'], ['operation', 'discount'], ['cache', 'yes'], ['error', 'yes'], ['email', 'email'], ['account_connection', 'issue'], ['operation', 'registration'], ['order_nbr', '00'], ['email', 'email'], ['order_nbr', '00'], ['status', 'in deposit'], ['place', 'details'], ['article', 'womanity edp'], ['reload', 'yes'], ['order_nbr', '00'], ['article', 'kenzo'], ['status', 'lost'], ['operation', 'resend'], ['order_nbr', '00'], ['pwd', 'forgotten'], ['relog', 'yes'], ['email', 'email'], ['email', 'email'], ['data', 'address'], ['order_nbr', '00'], ['order_nbr', '00'], ['email', 'email'], ['place', 'letterbox'], ['date', 'dimanche 6'], ['order_nbr', '00'], ['order_nbr', '00'], ['email', 'email'], ['order_nbr', '00'], ['order_nbr', '61'], ['status', 'in deposit'], ['error', 'yes'], ['step', 'payment'], ['payment_tool', 'mastercard'], ['payment_tool', 'no paypal'], ['payment_tool', 'international mastercard'], ['error', 'bank issue'], ['email', 'email1'], ['place', 'douane'], ['operation', 'payment'], ['article', 'guerlain/chanel'], ['article', 'guerlain'], ['date', '24/12'], ['operation', 'resend'], ['status', 'ready'], ['store', 'location'], ['order_nbr', '00'], ['order_nbr', '00'], ['payment_tool', 'cb'], ['payment_tool', 'international cb'], ['order_nbr', '00'], ['email', 'email2'], ['code', 'pantaleo'], ['place', 'free'], ['article', 'present'], ['place', 'home']]

    # print(slots)
    # # sys.exit()
    # jsondict = json.load(open('../input/brandnew_dialogues1-100.json'), encoding='utf-8')
    # out = open('../input/reallybrandnew_dialogues1-100.json', 'wb')
    # slot_corrector(jsondict, out, slots)
    # jsondict = json.load(open('../input/reallybrandnew_dialogues1-100.json'), encoding='utf-8')
    # entities_editor(jsondict, out)
    """
    #FORMATAGE 
    jsondict = json.load(open('../input/entities_dialogues1-100.json'), encoding='utf-8')
    slotsstream = open('../input/slots.json', 'wb')
    slots = {}
    for dialogue in jsondict:
        for turn in jsondict[dialogue]:
            print(turn['slots'])
            for dic in turn['slots']:
                for elem in dic:
                    if elem not in slots:
                        slots[elem] = [dic[elem]]
                    elif dic[elem] not in slots[elem]:
                        slots[elem].append(dic[elem])
    pprint(slots)
    slotsstream.write(json.dumps(slots, ensure_ascii=False, indent=4, sort_keys=True).encode("utf-8"))
    sys.exit()
    out = open('../input/entitiesintents_dialogues1-100.json', 'wb')
    new = {}
    for dialogue in jsondict:
        newd = []
        for turn in jsondict[dialogue]:
            if not 'intent' in turn:
                turn['intent'] = []
            newd.append(turn)
        new.update({dialogue: newd})
    out.write(json.dumps(new, ensure_ascii=False, indent=4, sort_keys=True).encode("utf-8"))
    """

    jsontocsv(jsondict, out)