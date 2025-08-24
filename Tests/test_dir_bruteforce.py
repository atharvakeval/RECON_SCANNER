from modules import dir_bruteforce

def test_dir_bruteforce():
    test_target = "example.com"
    wordlist = "wordlists/test_wordlist.txt"

    # Create a simple test wordlist file
    with open(wordlist, 'w') as f:
        f.write("robots.txt\n")

    result = dir_bruteforce.dir_bruteforce(test_target, wordlist, verbose=False)
    assert isinstance(result, list)
