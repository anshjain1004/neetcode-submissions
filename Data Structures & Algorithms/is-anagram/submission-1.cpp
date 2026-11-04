class Solution {
public:
    bool isAnagram(string s, string t) {
        int m = s.size();
        int n = t.size();
        if(m != n) return 0;

        unordered_map<char, int> freq;

        for(int i = 0 ; i < m ; i++){
            freq[s[i]]++;
            freq[t[i]]--;
        }

        for(auto x : freq){
            if(x.second != 0) return false;
        }
        return true;
    }
};
