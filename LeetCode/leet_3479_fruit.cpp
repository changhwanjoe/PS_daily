//https://leetcode.com/problems/fruits-into-baskets-iii/
//3479

class Solution {
    bool traverse_sg(int no, int fruit, vector<int>& sg_tree, int leaf_st)
    {
        bool ret = false;
        if (sg_tree[no] < fruit) 
            return ret;

        if (no < leaf_st) {
            ret = traverse_sg(no * 2, fruit, sg_tree, leaf_st);
            if (!ret)
                ret = traverse_sg(no * 2 + 1, fruit, sg_tree, leaf_st);
            return ret;
        }
        ret = true;

        sg_tree[no] = -1;
        
        // update 
        while (no > 1) {
            int v;
            if (no % 2 == 0) { // left
                v = sg_tree[no + 1];
            }
            else { // right
                v = sg_tree[no - 1];
            }
            
            sg_tree[no >> 1] = max(sg_tree[no], v);
            no = no >> 1;
        }

        return ret;
    }
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int ans = 0;
        int n = fruits.size();

        int k = (int)ceil(log2(n));
        int leaf_st = pow(2, k);
        int tree_sz = 2 * leaf_st;
        cout << tree_sz << endl;

        vector<int> seg_tree(tree_sz, -1);

        for (int i = 0; i < n; i++) {
            seg_tree[leaf_st + i] = baskets[i];
        }

        for (int i = tree_sz - 1; i > 0; i--) {
            int p_idx = i >> 1;
            seg_tree[p_idx] = max(seg_tree[p_idx], seg_tree[i]);
        }

        for (int i = 0; i < n; i++) {
            bool found;
            found = traverse_sg(1, fruits[i], seg_tree, leaf_st);
            if (!found)
                ans++;
        }
        return ans;
    }
};