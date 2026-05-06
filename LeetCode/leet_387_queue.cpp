//https://leetcode.com/problems/first-unique-character-in-a-string/?envType=problem-list-v2&envId=queue

//387
//FristUnique

#include <stack>
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> hash;

        for(const auto c : s){
            const auto ptr = hash.find(c);
            // first find
            if(ptr == hash.end())
                hash.insert({c, 1});
            // already found
            else
                ptr -> second += 1;
        }

        for(auto idx = 0; idx < s.size(); ++idx){
            if(hash.find(s[idx]) -> second == 1)
                return idx;
        }
        return -1;
    }

};