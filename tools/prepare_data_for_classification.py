import csv

from sentiment.tweet_preprocessor import TweetPreprocessor


def clean_data(source_filename, target_filename):
    preprocessor = TweetPreprocessor()
    count = 0
    with open(source_filename, encoding="windows-1252") as source_file:
        with open(target_filename, 'w', encoding="windows-1252", newline='') as target_file:
            reader = csv.reader(source_file)
            writer = csv.writer(target_file)
            for row in reader:
                # For now let's ignore neutral tweets - later threshold in bayes classifier need to be supplied
                # Currently training data contains only positive and negative, thus neutral classification can be only by threshold
                if int(row[0]) != 2:
                    text = [int(row[0]), *preprocessor.stem_tweet(preprocessor.tokenize_tweet(row[5]))]
                    writer.writerow(text)
                    count += 1
                if count % 10000 == 0: print(count)

clean_data('../app/classifier_data/training.1600000.processed.noemoticon.csv', '../classifier_data/training.1600000.processed.noemoticon_clean.csv')
clean_data('../app/classifier_data/testdata.manual.2009.06.14.csv', '../classifier_data/testdata.manual.2009.06.14_clean.csv')
