#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
using namespace std;

vector<int> encoding(string s1) {
    unordered_map<string, int> table;
    for (int i = 0; i <= 255; i++) {
        string ch = "";
        ch += char(i);
        table[ch] = i;
    }

    string p = "", c = "";
    p += s1[0];
    int code = 256;
    vector<int> output_code;
    cout << "String\tOutput_Code\tAddition\n";
    for (int i = 0; i < s1.length(); i++) {
        if (i != s1.length() - 1)
            c += s1[i + 1];
        if (table.find(p + c) != table.end()) {
            p = p + c;
        } else {
            cout << p << "\t" << table[p] << "\t\t"
                 << p + c << "\t" << code << endl;
            output_code.push_back(table[p]);
            table[p + c] = code;
            code++;
            p = c;
        }
        c = "";
    }
    cout << p << "\t" << table[p] << endl;
    output_code.push_back(table[p]);
    return output_code;
}

void decoding(vector<int> op) {
    cout << "\nDecoded String:\n";
    unordered_map<int, string> table;
    for (int i = 0; i <= 255; i++) {
        string ch = "";
        ch += char(i);
        table[i] = ch;
    }
    int old = op[0], n;
    string s = table[old];
    string c = "";
    c += s[0];
    cout << s;
    int count = 256;
    for (int i = 0; i < op.size() - 1; i++) {
        n = op[i + 1];
        if (table.find(n) == table.end()) {
            s = table[old];
            s = s + c;
        } else {
            s = table[n];
        }
        cout << s;
        c = "";
        c += s[0];
        table[count] = table[old] + c;
        count++;
        old = n;
    }
}

int main(int argc, char *argv[]) {
    string text = "";

    if (argc == 2) {
        text = argv[1];
    }

    vector<int> output_code = encoding(text);
	cout<<"-----------------------------------------------------------"<<endl;

    cout << "Input String: " << text << endl;
	cout<<endl;

    cout << "Encoded Codes are: ";
    for (int i = 0; i < output_code.size(); i++) {
        cout << output_code[i] << " ";
    }
    cout << endl;
    decoding(output_code);

    // Compression calculations
    double inputSize = text.size() * 8; // assuming 8 bits per character
    double outputSize = output_code.size() * sizeof(output_code[0]) * 8; // size of vector in bits

    double compressionRatio = inputSize / outputSize;
    double compressionPercentage = (1 - (outputSize / inputSize)) * 100;

	cout<<endl;
		cout<<endl;


    cout << "\nCompression Ratio: " << compressionRatio << endl;
    cout << "Compression Percentage: " << compressionPercentage << "%" << endl;
		cout<<endl;
cout<<"-----------------------------------------------------------"<<endl;

    return 0;
}
