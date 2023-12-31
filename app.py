import os
import nltk
import re

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_text():
    search_string = request.args.get('string')
    if not search_string:
        return jsonify({"error": "Please provide a search string using 'string' parameter"}), 400
    file_path = 'king-i-150.txt'
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    with open(file_path, 'r') as file:
        text = file.read()
    occurrences = find_string(text, search_string)
    return jsonify({
        "query_text": search_string,
        "number_of_occurrences": len(occurrences),
        "occurrences": occurrences
    })


def find_string(text, search_string):
    occurrences = []
    matches = re.finditer(search_string, text.replace('\n', ' '))
    lines = text.split('\n')
    sentences = nltk.tokenize.sent_tokenize(text)
    # If storing them in lists, then we don't have to use find(), it can be more efficient in terms of time, but consumes more memory.
    for match in matches:
        in_sentence = []
        for sentence in sentences:
            if  match.end() <= text.find(sentence) + len(sentence):
                in_sentence.append(sentence.replace('\n', ' '))
                break
            if text.find(sentence) + len(sentence) < match.end() and text.find(sentence) + len(sentence) >= match.start():
                in_sentence.append(sentence.replace('\n', ' '))
                continue

        for i, line in enumerate(lines):
            if text.find(line) <= match.start() <= text.find(line) + len(line):
                line_number = i + 1
                start = match.start() - text.find(line) + 1
            if text.find(line) <= match.end() <= text.find(line) + len(line):
                end = match.end() - text.find(line) + 1
                break

        occurrences.append({
            "start": start,
            "end": end,
            "line": line_number,
            "in_sentence": in_sentence[0] if len(in_sentence) == 1 else in_sentence
        })
    return occurrences


if __name__ == "__main__":
    nltk.download('punkt')
    app.run(port=8001, debug=True, host='0.0.0.0')

