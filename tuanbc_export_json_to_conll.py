from label_studio_converter import Converter
import unittest
import label_studio_converter.utils as utils

if __name__ == "__main__":
    # c = Converter('examples/named_entity/config.xml')
    # c.convert_to_conll2003('examples/named_entity/completions/', 'tmp/output.conll')

    text = 'We gave Jane Smith the ball.'
    spans = [{'end': 18, 'labels': ['Person'], 'start': 7, 'text': ' Jane Smith'}]
    tokens, tags = utils.create_tokens_and_tags(text, spans)
    print(tokens)
    print(tags)
    # assert(tokens, ['We', 'gave', 'Jane', 'Smith', 'the', 'ball', '.'])
    # assert(tags, ['O', 'O', 'B-Person', 'I-Person', 'O', 'O', 'O'])