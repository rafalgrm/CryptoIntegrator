emoticons_sentiment = {'EMOT_SMILE':[':)', ':-)', '(:', '(-:', ';)'],
                       'EMOT_LAUGH':[':D', ':-D', ';D', 'XD', 'xd', 'xD'],
                       'EMOT_LOVE':['<3', ':*', ';*'],
                       'EMOT_SADNESS':[':(', ';(', ':-(', ';-(']}

emoticons_map = {}

for k, v in emoticons_sentiment.items():
    for icon in v:
        emoticons_map[icon] = k