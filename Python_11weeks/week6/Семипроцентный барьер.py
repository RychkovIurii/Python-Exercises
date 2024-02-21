fin = open('input.txt', 'r', encoding='utf8')
text = []
for line in fin:
    text.append(line.strip())
parties = []
votes = []
for i in text[1:text.index('VOTES:')]:
    parties.append(i)
for i in text[text.index('VOTES:') + 1:]:
    votes.append(i)
for party in parties:
    parties[parties.index(party)] = [party, votes.count(party)]
for i in parties:
    if i[1] / len(votes) >= 0.07:
        print(i[0])
fin.close()
