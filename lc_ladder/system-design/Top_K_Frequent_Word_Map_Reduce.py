#!/usr/local/bin/python3

# https://www.lintcode.com/problem/top-k-frequent-words-map-reduce/description?_from=ladder&&fromId=8
# Example
# 使用map reduce框架查找最常使用的k个单词.
# mapper的key为文档的id, 值是文档的内容, 文档中的单词由空格分割.
# 对于reducer，应该输出最多为k个key-value对, 包括最常用的k个单词以及他们在当前reducer中的使用频率.评判系统会合并不同的reducer中的结果以得到 全局 最常使用的k个单词, 所以你不需要关注这一环节. k 在TopK类的构造器中给出.
#
# 样例
# 给出文档 A =
#
# lintcode is the best online judge
# I love lintcode
# 以及文档 B =
#
# lintcode is an online judge for coding interview
# you can test your code online at lintcode
# 最常用的2个单词以及他们的使用频率应该为:
#
# lintcode, 4
# online, 3
# 注意事项
# 如果单词有相同的使用频率,那么按照字母排序

"""
Solution:
lintcode 只支持Java c++ version

Corner cases:
"""

/**
 * Definition of Input:
 * template<class T>
 * class Input {
 * public:
 *     bool done();
 *         // Returns true if the iteration has elements or false.
 *     void next();
 *         // Move to the next element in the iteration
 *         // Runtime error if the iteration has no more elements
 *     T value();
 *        // Get the current element, Runtime error if
 *        // the iteration has no more elements
 * }
 * Definition of Document:
 * class Document {
 * public:
 *     int id; // document id
 *     string content; // document content
 * }
 */

class MyPair {
public:
    string key;
    int value;
    MyPair(string word, int times) {
        key = word;
        value = times;
    };
    // override operator < which is used in priority_queue
    bool operator<(const MyPair& obj) const {
        return value > obj.value || value == obj.value && key < obj.key;
    }
};

class TopKFrequentWordsMapper: public Mapper {
public:
    void Map(Input<Document>* input) {
        // Write your code here
        // Please directly use func 'output' to output
        // the results into output buffer.
        // void output(string &key, int value);
        while (!input->done()) {
            vector<string> words = split(input->value().content, " ");
            for (string word : words) {
                if (word.size() > 0) {
                    output(word, 1);
                }
            }
            input->next();
        }
    }

    vector<string> split(const string &str, const string &delim) {
        vector<string> results;
        int lastIndex = 0;
        int index;
        while ((index = str.find(delim, lastIndex)) != string::npos) {
            results.push_back(str.substr(lastIndex, index - lastIndex));
            lastIndex = index + delim.length();
        }
        if (lastIndex != str.length()) {
            results.push_back(str.substr(lastIndex, str.length() - lastIndex));
        }
        return results;
    }
};


class TopKFrequentWordsReducer: public Reducer {
private:
    int k;
    priority_queue<MyPair> q;
public:
    void setUp(int k) {
        // initialize your data structure here
        this->k = k;
    }

    void Reduce(string &key, Input<int>* input) {
        // Write your code here
        int sum = 0;
        while (!input->done()) {
            sum += input->value();
            input->next();
        }

        MyPair myPair(key, sum);
        if (q.size() < k)
            q.push(myPair);
        else {
            q.push(myPair);
            q.pop();
        }
    }

    void cleanUp() {
        // Please directly use func 'output' to output
        // the top k pairs <word, times> into output buffer.
        // void output(string &key, int &value);
        vector<MyPair> list;
        while (!q.empty()) {
            list.push_back(q.top());
            q.pop();
        }

        // reverse
        int n = list.size();
        for (int i = n - 1; i >=0; --i) {
            // Write into output in ascending order
            output(list[i].key, list[i].value);
        }
    }
};
# Test Cases
if __name__ == "__main__":
    solution = Solution()
