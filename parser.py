import stanza
import sys

# Download Vietnamese model if not already downloaded
stanza.download('vi')

# Initialize Vietnamese pipeline with dependency parser
nlp = stanza.Pipeline(lang='vi', processors='tokenize,pos,lemma,depparse')

# Function to process CoNLL-U text
def process_conllu(conllu_lines):
    sentences = []
    current_sentence = []
    sentence_id = ""
    sentence_text = ""
    
    for line in conllu_lines:
        line = line.strip()
        if line.startswith('# sent_id'):
            if current_sentence:
                sentences.append((sentence_id, sentence_text, current_sentence))
                current_sentence = []
            sentence_id = line
        elif line.startswith('# text'):
            sentence_text = line.replace('# text =', '').strip()
        elif line and not line.startswith('#'):
            current_sentence.append(line)
    
    if current_sentence:
        sentences.append((sentence_id, sentence_text, current_sentence))
    
    return sentences

# Function to get dependency relationships using Stanza
def get_dependency_relations(sentences):
    results = []
    
    for sent_id, text, tokens in sentences:
        doc = nlp(text)
        stanza_tokens = [(word.id, word.head, word.deprel) for sentence in doc.sentences for word in sentence.words]
        
        updated_lines = [sent_id, f'# text = {text}']
        
        for i, line in enumerate(tokens):
            parts = line.split('\t')
            if len(parts) >= 8:
                token_id = int(parts[0])
                token_head = int(parts[6]) if parts[6].isdigit() else 0
                
                for st_id, st_head, st_deprel in stanza_tokens:
                    if st_id == token_id:
                        parts[7] = "root" if token_head == 0 else st_deprel
                        break
                
            parts.append('_')  # Add empty column at the end
            updated_lines.append('\t'.join(parts))
        
        results.append('\n'.join(updated_lines))
    
    return results

# Main function to process file
def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        conllu_lines = f.readlines()
    
    sentences = process_conllu(conllu_lines)
    results = get_dependency_relations(sentences)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(results) + '\n')
    
    print(f'Processed file saved to {output_file}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.conllu output.conllu")
    else:
        main(sys.argv[1], sys.argv[2])
