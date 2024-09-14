def split_line(line, max_length=160):
    """
    Splits a line if its length exceeds max_length.
    If no period, question mark, or comma is found before max_length, split after the first period, question mark, or comma in the line.
    Returns a list of strings (split lines).
    """
    if ':' not in line:
        return [line]  # Return the line as-is if no colon is found

    name, text = line.split(':', 1)
    name = name.strip()
    text = text.strip()
    result = []
    
    while len(text) > max_length:
        # Search for the last period, question mark, or comma before max_length
        split_index = max(
            text.rfind('.', 0, max_length), 
            text.rfind('?', 0, max_length),
            text.rfind(',', 0, max_length)
        )
        
        if split_index == -1:  # No period, question mark, or comma before max_length
            # Search for the first period, question mark, or comma in the entire text
            split_index = min(
                (i for i in [text.find('.'), text.find('?'), text.find(',')] if i != -1), 
                default=-1
            )

            if split_index == -1:  # No punctuation mark at all
                split_index = max_length
            elif text.count('.') + text.count('?') + text.count(',') == 1:  # Only one punctuation mark, don't split
                break
            else:
                split_index += 1  # Split after the first period, question mark, or comma found
        else:
            split_index += 1  # Ensure we split *after* the punctuation

        # If split_index doesn't reduce text length, break the loop to avoid infinite loop
        if split_index >= len(text):
            break
        
        # Add the part up to the split point to the result
        result.append(f"{name}: {text[:split_index].strip()}")
        
        # Update text to the remaining part after the split point
        text = text[split_index:].strip()

    result.append(f"{name}: {text}")
    
    return result




def process_file(input_file, output_file):
    """
    Processes the input .txt file, copying it to output_file, and splitting lines over 160 characters.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()  # Remove leading/trailing whitespace/newlines
            if not line:
                continue  # Skip empty lines

            # Split the line if needed
            split_lines = split_line(line)
            
            # Write each split line to the output file
            for split_line_item in split_lines:
                outfile.write(split_line_item + '\n')

if __name__ == "__main__":
    input_file = "dialogs.txt"  # Replace with the name of your input file
    output_file = "output.txt"  # Replace with the desired output file name
    process_file(input_file, output_file)
