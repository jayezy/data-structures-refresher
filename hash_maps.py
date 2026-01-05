from unittest import result


def create_sample_hash_map():
    hash_map = {}
    hash_map["apple"] = 1
    hash_map["pineapple"] = 2
    hash_map["kiwi"] = 3
    hash_map["banana"] = 4
    hash_map["orange"] = 5
    hash_map["mango"] = 6
    hash_map["strawberry"] = 7
    hash_map["watermelon"] = 8
    hash_map["peach"] = 9
    hash_map["pear"] = 10
    hash_map["plum"] = 11
    hash_map["cherry"] = 12
    hash_map["raspberry"] = 13
    hash_map["blueberry"] = 14
    return hash_map

# Used in:
#   Anagrams
#   Most common elements
#   Sliding window
#   Strings and arrays
def frequency_counter(sample_text):
    frequency_map = {}
    for character in sample_text.lower():
        frequency_map[character] = frequency_map.get(character, 0) + 1
    print("Full map:", frequency_map)
    total_vowels = frequency_map.get("a", 0) + frequency_map.get("e", 0) + frequency_map.get("i", 0) + frequency_map.get("o", 0) + frequency_map.get("u", 0)
    total_consonants = frequency_map.get("b", 0) + frequency_map.get("c", 0) + frequency_map.get("d", 0) + frequency_map.get("f", 0) + frequency_map.get("g", 0) + frequency_map.get("h", 0) + frequency_map.get("j", 0) + frequency_map.get("k", 0) + frequency_map.get("l", 0) + frequency_map.get("m", 0) + frequency_map.get("n", 0) + frequency_map.get("p", 0) + frequency_map.get("q", 0) + frequency_map.get("r", 0) + frequency_map.get("s", 0) + frequency_map.get("t", 0) + frequency_map.get("v", 0) + frequency_map.get("w", 0) + frequency_map.get("x", 0) + frequency_map.get("y", 0) + frequency_map.get("z", 0)
    print("Total vowels:", total_vowels)
    print("Total consonants:", total_consonants)
    print("Ratio of vowels to consonants:", total_vowels / total_consonants)
    print("Percentage of vowels:", (total_vowels / (total_vowels + total_consonants)) * 100)
    print("Percentage of consonants:", (total_consonants / (total_vowels + total_consonants)) * 100)

# Mapping values to indices
def two_sum(nums, target):
    indices_map = {}
    for i, num in enumerate(nums):
        if target - num in indices_map:
            return [indices_map[target-num], i]
        indices_map[num] = i
    return []

# Hashmap is used as a cache/memoization tool in
#   DP, Recursive memoization, Avoiding recomputation
def hashmap_as_cache():
    memo = {}
    def dfs(x):
        if x in memo:
            return memo[x]
        # compute something
        result = 1
        memo[x] = result
        return result    
    return None

def hashmap_group_by_key(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)

def sliding_window_application(text):
    count = {}
    left_index = 0
    max_non_repeating_substring = ""

    for right_index, character in enumerate(text):
        count[character] = count.get(character, 0) + 1

        while count[character] > 1:
            count[text[left_index]] -= 1     # Remove the start of sliding window from hash map
            left_index += 1                  # Increment the left index

        if len(text[left_index:right_index+1]) > len(max_non_repeating_substring):
            max_non_repeating_substring = text[left_index:right_index+1]
    return max_non_repeating_substring

def main():
    # hash_map = create_sample_hash_map()
    # sample_text = "this is a sample text and we are going to use this text to counte how often certain letter repeat in this text. It would actually be super interesting to see the ratio of vowels to consonants in this text."
    # frequency_counter(sample_text)
    
    sample_text2 = "abcdefghijklmnokqrstuvwxyzabcdabcdefghijklmnopqrstuvwxyz"
    response = sliding_window_application(sample_text2)
    print(response)

if __name__ == "__main__":
    main()