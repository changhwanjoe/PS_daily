//https://leetcode.com/problems/number-of-recent-calls/submissions/1750318364/?envType=problem-list-v2&envId=queue
class RecentCounter {
public:
    queue <int> requests;
    RecentCounter() {
        
    }
    
    int ping(int t) {
        requests.push(t);
        while(requests.size() && requests.front() < t - 3000) {
            requests.pop();
        }
        return requests.size();

    }
};