/*
https://www.codechef.com/IARCSJUD/problems/LONGPALI
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

int max_even_palindrome(string s, int pos, int n) {
    int i = pos-1, j = pos;
    while(i >= 0 && j < n && s[i] == s[j]) {
        i--;
        j++;
    }

    return (j-i-1);
}

int max_odd_palindrome(string s, int pos, int n) {
    int i = pos-1, j = pos + 1;
    while(i >= 0 && j < n && s[i] == s[j]) {
        i--;
        j++;
    }

    return (j-i-1);
}

int main(int argc, char *argv[])
{
    // <-- Fast I/O -->
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t = 1;
    // <-- Multiple test cases -->
    // cin>>t;
    while (t--) {
        int n;
        cin>>n;
        string word;
        cin>>word;

        int i, max_pal = 0, max_pos = 0;
        forl(i, 0, n) {
            int odd_pal = max_odd_palindrome(word, i, n);
            int even_pal = max_even_palindrome(word, i, n);

            if(even_pal > max_pal) {
                max_pal = even_pal;
                max_pos = i - (even_pal/2);
            }

            if(odd_pal > max_pal) {
                max_pal = odd_pal;
                max_pos = i - (odd_pal/2);
            }
        }
        cout<<max_pal<<"\n";
        forl(i, max_pos, max_pos + max_pal)
            cout<<word[i];
        cout<<"\n";
    }
    return 0;
}