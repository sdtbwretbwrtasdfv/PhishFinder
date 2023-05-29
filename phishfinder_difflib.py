import argparse
import difflib
import datetime
import time

start_time = time.time()
min_ratio_means_phish = float(0.8)


def main(filepath, compare_word):

    log_file = filepath

    # loading criteria from a file
    with open(filepath, 'r') as f:
        criteria_list = [line.strip() for line in f]

    # calculating all similarity ratios
    detected_similar_words = []
    for criteria in criteria_list:
        if difflib.SequenceMatcher(None, compare_word, criteria).ratio() >= min_ratio_means_phish:
            print(compare_word + ' : ' + criteria)
            detected_similar_words.append([compare_word, criteria])

    # writing log
    with open(log_file, 'a') as writing_log:
        writing_log.write(datetime.date.today().strftime('%d/%m/%Y') + '\n')
        writing_log.write('List of criteria:\n')
        writing_log.write(compare_word + '\n')
        writing_log.write('Detected similar words:\n')
        if len(detected_similar_words) > 0:
            for element in detected_similar_words:
                writing_log.write(element[0] + ' : ' + element[1] + '\n')
        else:
            writing_log.write('No similar words with ratio = {}!\n'.format(min_ratio_means_phish))
        writing_log.write('It took {}\n'.format(time.time() - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script compares a word with a list of words in a file.')
    parser.add_argument('-f', '--filepath', required=True, help='Full path to the file.')
    parser.add_argument('-w', '--word', required=True, help='Word for comparison.')
    args = parser.parse_args()
    main(args.filepath, args.word)

