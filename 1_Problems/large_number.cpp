#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
class Solution {
public:
    string simplifyPath(string path)
    {
        vector<string> directory_stack;
        string token;

        for (size_t i = 0; i <= path.size(); ++i)
        {
            if (i == path.size() || path[i] == '/')
            {
                if (!token.empty())
                {
                    if (token == ".")
                    {
                        // no-op
                    }
                    else if (token == "..")
                    {
                        if (!directory_stack.empty())
                        {
                            directory_stack.pop_back();
                        }
                    }
                    else
                    {
                        directory_stack.push_back(token);
                    }
                    token.clear();
                }
            }
            else
            {
                token.push_back(path[i]);
            }
        }

        if (directory_stack.empty())
        {
            return "/";
        }

        string result;
        for (const string& name : directory_stack)
        {
            result += '/';
            result += name;
        }
        return result;
    }
};