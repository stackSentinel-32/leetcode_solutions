#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    static const int INF = 1000000000;

    struct Node {
        int max0;
        int max00;
        int min1;
        bool is_entire;
        
        int p_v[4], p_l[4], p_sz;
        int s_v[4], s_l[4], s_sz;
        
        Node() : max0(0), max00(0), min1(INF), is_entire(true), p_sz(0), s_sz(0) {}
    };

    vector<Node> tree;

    Node merge_nodes(const Node& A, const Node& B) {
        Node C;
        C.is_entire = false;
        
        // Use a static-sized buffer to accumulate runs at the boundary
        int mid_v[8], mid_l[8], mid_sz = 0;
        
        auto add_mid = [&](int v, int l) {
            if (mid_sz > 0 && mid_v[mid_sz - 1] == v) {
                mid_l[mid_sz - 1] += l;
            } else {
                mid_v[mid_sz] = v;
                mid_l[mid_sz] = l;
                mid_sz++;
            }
        };

        // Extract A's rightmost/entire runs
        if (A.is_entire) {
            for (int i = 0; i < A.p_sz; i++) add_mid(A.p_v[i], A.p_l[i]);
        } else {
            for (int i = 0; i < A.s_sz; i++) add_mid(A.s_v[i], A.s_l[i]);
        }

        // Extract B's leftmost/entire runs
        if (B.is_entire) {
            for (int i = 0; i < B.p_sz; i++) add_mid(B.p_v[i], B.p_l[i]);
        } else {
            for (int i = 0; i < B.p_sz; i++) add_mid(B.p_v[i], B.p_l[i]);
        }

        int m_max0 = 0, m_max00 = 0, m_min1 = INF;

        for (int i = 0; i < mid_sz; i++) {
            if (mid_v[i] == 0) m_max0 = max(m_max0, mid_l[i]);
        }

        for (int i = 1; i + 1 < mid_sz; i++) {
            if (mid_v[i] == 1 && mid_v[i - 1] == 0 && mid_v[i + 1] == 0) {
                m_min1 = min(m_min1, mid_l[i]);
                m_max00 = max(m_max00, mid_l[i - 1] + mid_l[i + 1]);
            }
        }

        C.max0 = max({A.max0, B.max0, m_max0});
        C.max00 = max({A.max00, B.max00, m_max00});
        C.min1 = min({A.min1, B.min1, m_min1});

        if (A.is_entire && B.is_entire) {
            if (mid_sz <= 4) {
                C.is_entire = true;
                C.p_sz = mid_sz;
                C.s_sz = mid_sz;
                for (int i = 0; i < mid_sz; i++) {
                    C.p_v[i] = C.s_v[i] = mid_v[i];
                    C.p_l[i] = C.s_l[i] = mid_l[i];
                }
            } else {
                C.is_entire = false;
                C.p_sz = 4;
                for (int i = 0; i < 4; i++) { C.p_v[i] = mid_v[i]; C.p_l[i] = mid_l[i]; }
                C.s_sz = 4;
                for (int i = 0; i < 4; i++) { C.s_v[i] = mid_v[mid_sz - 4 + i]; C.s_l[i] = mid_l[mid_sz - 4 + i]; }
            }
        } else {
            C.is_entire = false;
            
            // Rebuild Prefix limit of 4
            if (A.is_entire) {
                C.p_sz = min(4, mid_sz);
                for (int i = 0; i < C.p_sz; i++) { C.p_v[i] = mid_v[i]; C.p_l[i] = mid_l[i]; }
            } else {
                C.p_sz = A.p_sz;
                for (int i = 0; i < C.p_sz; i++) { C.p_v[i] = A.p_v[i]; C.p_l[i] = A.p_l[i]; }
            }
            
            // Rebuild Suffix limit of 4
            if (B.is_entire) {
                C.s_sz = min(4, mid_sz);
                for (int i = 0; i < C.s_sz; i++) {
                    C.s_v[i] = mid_v[mid_sz - C.s_sz + i];
                    C.s_l[i] = mid_l[mid_sz - C.s_sz + i];
                }
            } else {
                C.s_sz = B.s_sz;
                for (int i = 0; i < C.s_sz; i++) { C.s_v[i] = B.s_v[i]; C.s_l[i] = B.s_l[i]; }
            }
        }
        return C;
    }

    void build(int node, int l, int r, const string& s) {
        if (l == r) {
            tree[node].max0 = (s[l] == '0' ? 1 : 0);
            tree[node].max00 = 0;
            tree[node].min1 = INF;
            tree[node].is_entire = true;
            
            tree[node].p_sz = 1;
            tree[node].p_v[0] = s[l] - '0';
            tree[node].p_l[0] = 1;
            
            tree[node].s_sz = 1;
            tree[node].s_v[0] = s[l] - '0';
            tree[node].s_l[0] = 1;
            return;
        }

        int mid = l + (r - l) / 2;
        build(node * 2, l, mid, s);
        build(node * 2 + 1, mid + 1, r, s);
        tree[node] = merge_nodes(tree[node * 2], tree[node * 2 + 1]);
    }

    Node query(int node, int l, int r, int ql, int qr) {
        // Prevents querying empty nodes natively by strictly descending overlapping ranges
        if (ql <= l && r <= qr)
            return tree[node];

        int mid = l + (r - l) / 2;
        if (qr <= mid)
            return query(node * 2, l, mid, ql, qr);
        if (ql > mid)
            return query(node * 2 + 1, mid + 1, r, ql, qr);

        return merge_nodes(
            query(node * 2, l, mid, ql, qr),
            query(node * 2 + 1, mid + 1, r, ql, qr)
        );
    }

public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int totalOnes = 0;
        
        for (char c : s) {
            if (c == '1') totalOnes++;
        }

        tree.assign(4 * n + 5, Node());
        build(1, 0, n - 1, s);

        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            Node res = query(1, 0, n - 1, q[0], q[1]);
            int gain = 0;
            
            // Verify there exists at least one '1' isolated by '0's allowing a valid trade
            if (res.min1 != INF) {
                gain = max(res.max00, res.max0 - res.min1);
            }

            ans.push_back(totalOnes + gain);
        }

        return ans;
    }
};