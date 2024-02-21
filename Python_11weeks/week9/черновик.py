def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    all_text = file_contents.split()
    correct_text = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    for one_word in all_text:
        one_word = one_word.lower()
        if one_word not in uninteresting_words:
            for symbol in one_word:
                if symbol in punctuations:
                    one_word = one_word.replace(symbol, "")
            correct_text.append(one_word)
    my_dict = {}
    for i in correct_text:
        if i not in my_dict:
            my_dict[i] = 0
        my_dict[i] += 1
    return print(my_dict)


file_contents = ""'The Emilia-Romagna region was formed by the merging together of different yet complementary areas. Between the lapping waves of the Adriatic Sea and the peaks of the Apennines lies a wonderful variety of history, traditions and landscapes, offering just as many destinations to visit. The Emilia area is the land of the castles and citadels of the Parma and Piacenza Duchy, of world-renowned PDO and PGI products − especially Parmigiano Reggiano and Prosciutto di Parma − and the music of Giuseppe Verdi, who hails from Busseto. The city of Reggio Emilia was in fact the birthplace of Italys tricolour flag. When it comes to culinary specialities, the Bologna and Modena area  is also worthy of mention. This is the birthplace of balsamic vinegar, Mortadella Bologna and many other flavours that pair beautifully with local wines. This area is home to major car and motorbike manufacturers − Ferrari, Lamborghini, Ducati and Maserati to name a few − and world-famous racetracks. The vast ski resorts on Monte Cimone, the highest peak in the region (2,165 metres above sea level), and on the Corno alle Scale mountain are also a testament to the regions deep-seated sporting tradition.Romagna, on the other hand, has always been about seaside and entertainment, from Ferraras beaches to Rimini'

calculate_frequencies(file_contents)