import sys

def read_conllu(file_path):
    sentences = []
    current_sentence = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            continue
        elif line == "":
            if current_sentence:
                sentences.append(current_sentence)
                current_sentence = []
        else:
            current_sentence.append(line.split('\t'))
    
    if current_sentence:
        sentences.append(current_sentence)
    
    return sentences

def calculate_uas_las(groundtruth_file, predict_file):
    gt_sentences = read_conllu(groundtruth_file)
    pred_sentences = read_conllu(predict_file)
    
    if len(gt_sentences) != len(pred_sentences):
        raise ValueError("Files have different numbers of sentences.")
    
    total_tokens = 0
    correct_heads = 0
    correct_labels = 0
    
    for gt_sent, pred_sent in zip(gt_sentences, pred_sentences):
        if len(gt_sent) != len(pred_sent):
            raise ValueError("Mismatched sentence lengths.")
        
        for gt_token, pred_token in zip(gt_sent, pred_sent):
            if len(gt_token) < 8 or len(pred_token) < 8:
                continue  # Skip malformed lines
            
            total_tokens += 1
            if gt_token[6] == pred_token[6]:  # Compare HEAD column
                correct_heads += 1
                if gt_token[7] == pred_token[7]:  # Compare DEPREL column
                    correct_labels += 1
    
    uas = correct_heads / total_tokens if total_tokens > 0 else 0
    las = correct_labels / total_tokens if total_tokens > 0 else 0
    
    return uas, las

def main(groundtruth_file, predict_file):
    uas, las = calculate_uas_las(groundtruth_file, predict_file)
    print(f"Unlabeled Attachment Score (UAS): {uas:.4f}")
    print(f"Labeled Attachment Score (LAS): {las:.4f}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py groundtruth.conllu predict.conllu")
    else:
        main(sys.argv[1], sys.argv[2])
