/*
https://www.codechef.com/IARCSJUD/problems/IAREVERS
*/

#include <bits/stdc++.h>
using namespace std;

// <-- Template code for utility -->
#define watch(x) cout << (#x) << " is " << (x) << endl
#define forl(i, b, e) for (i = b; i < e; i++)
#define fore(i, b, e) for (i = b; i <= e; i++)

void input_arr(vector<int> &arr, int n)
{
    int i;
    forl(i, 0, n)
    {
        int num;
        cin>>num;
        arr.push_back(num);
    }
}

template <typename T1, typename T2>
inline std::ostream &operator<<(std::ostream &os, const std::pair<T1, T2> &p)
{
    return os << "(" << p.first << ", " << p.second << ")";
}

template <typename T>
inline std::ostream &operator<<(std::ostream &os, const std::vector<T> &v)
{
    bool first = true;
    os << "[";
    for (unsigned int i = 0; i < v.size(); i++)
    {
        if (!first)
            os << ", ";
        os << v[i];
        first = false;
    }
    return os << "]";
}

template <typename T>
inline std::ostream &operator<<(std::ostream &os, const std::set<T> &v)
{
    bool first = true;
    os << "[";
    for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii;
        first = false;
    }
    return os << "]";
}

template <typename T1, typename T2>
inline std::ostream &operator<<(std::ostream &os, const std::map<T1, T2> &v)
{
    bool first = true;
    os << "[";
    for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii;
        first = false;
    }
    return os << "]";
}

// <-- Main funtion -->
// This is where the actual program is

int main(int argc, char *argv[])
{
    // <-- Fast I/O -->
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1;
    // <-- Multiple test cases -->
    // cin>>t;
    while (t--) {
        int n, i, j;
        cin>>n;
        cin.ignore();
        stack<string> st;

        string s;

        forl(i, 0, n) {
            string s;
            
            getline(cin, s);
            string word;
            s.push_back(' ');
            forl(j, 0, s.size()) {
                char c;
                c = s[j];
                if(c == ' ') {
                    if(!word.empty())
                        st.push(word);
                    word.clear();
                }
                else if(isalpha(c)) 
                    word.push_back(c);
                else continue;
            }
            st.push("\n");
        }
        
        while(!st.empty()) {
            cout<<st.top()<<" ";
            st.pop();
        }

    }
    return 0;
}