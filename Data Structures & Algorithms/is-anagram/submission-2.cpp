class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        // Create a copy of t so we can modify it
        string temp = t;
        
        for (char c : s) {
            bool found = false;
            // Check if c is in temp
            for (int j = 0; j < temp.length(); j++) {
                if (c == temp[j]) {
                    // Mark this character as used
                    temp[j] = '\0';
                    found = true;
                    break;
                }
            }
            // If a character from s is not found in temp, it's not an anagram
            if (!found) {
                return false;
            }
        }
        return true;
    }
};
