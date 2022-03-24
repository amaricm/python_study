def count_substring(string, sub_string):
    counter = 0
    for x in range(0, len(string)):
        sentence_start_at = string[x:x+len(sub_string)]
        if sentence_start_at == sub_string:
            counter += 1
    return counter
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)