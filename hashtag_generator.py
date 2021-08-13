def generate_hashtag(s):
    if (len(s) == 0):
        return False
    ns = ""
    for i in s:
        # Convert multiple spaces to single in the passed string
        ns = ' '.join(s.split())
    words = ns.split(" ")
    for i in range(len(words)):
        # Capitalize the first letter of every word and convert the remaining to lowercase
        words[i] = words[i][0].upper() + words[i][1:].lower()
    s = ""
    for i in range(len(words)):
        s = s + words[i]
    s = "#" + s
    # Return False if the length of the message is 0 or greater than 140
    if len(s) > 140 or len(s) == 0:
        return False
    return s