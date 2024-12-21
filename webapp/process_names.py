def process_word(word, next_word=None):
    """Process a single word to ensure it's exactly 5 letters."""
    if len(word) >= 5:
        return word[:5]
    elif next_word and len(word) < 5:
        combined = word + next_word
        return combined[:5]
    else:
        return None  # Skip words that can't be made into 5 letters

def process_name_line(line):
    """Process a single line containing 1-5 words."""
    # Split by comma and strip whitespace
    names = [name.strip() for name in line.split(',')]
    result = []
    
    for name in names:
        # First split by hyphen, then by space
        hyphenated_parts = name.strip().split('-')
        words = []
        for part in hyphenated_parts:
            words.extend(part.strip().split())
        
        for i in range(len(words)):
            current_word = words[i]
            next_word = words[i + 1] if i + 1 < len(words) else None
            
            processed = process_word(current_word, next_word)
            if processed:
                result.append(processed)
    
    return result

def main():
    input_file = "webapp/names.csv"
    output_file = "webapp/names_processed.txt"
    
    processed_words = set()  # Using set to avoid duplicates
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            words = process_name_line(line)
            processed_words.update(words)
    
    # Write the results to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(processed_words):
            f.write(word + '\n')

if __name__ == "__main__":
    main() 