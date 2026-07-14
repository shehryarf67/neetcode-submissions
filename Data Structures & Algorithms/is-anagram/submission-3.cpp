class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        if (s.length() != t.length()) 
        {
            return false;
        }
        string temp = t;
        
        for (char c : s) 
        {
            bool found = false;
            for (int j = 0; j < temp.length(); j++) 
            {
                if (c == temp[j]) 
                {
                    temp[j] = '\0';
                    found = true;
                    break;
                }
            }
            if (!found) 
            {
                return false;
            }
        }
        return true;
    }
};
