# split string that was returned by ChatGPT

def format_reply(string, chunk_size=100):
    words = string.split()
    result = ""
    line_length = 0
    for word in words:
        if line_length + len(word) > chunk_size:
            result += "\n"
            line_length = 0
        result += word + " "
        line_length += len(word) + 1
    return result.strip()

print(">>> Fn format_reply... Loaded")