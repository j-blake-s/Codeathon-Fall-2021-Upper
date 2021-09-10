#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

/* Debug printing functions */
#ifdef DEBUG
#define DBG(args) cout << args;
#else
#define DBG(args)
#endif


string formulaVars(const string &formula) {
    int numVars = (formula.length() + 1) / 2;
    char variables[numVars+1];
    variables[numVars] = '\0';
    for (int i = 0; i < numVars; i++) {
        variables[i] = formula[2*i];
    }
    std::sort(variables, variables+numVars);
    return variables;
}

struct SortListItem {
    int score,   // Score based on a formula applied to the list
    mapPartyID,  // In an array of SortListItems, index i corresponds to lst[i].mapPartyID
    mapIdx;      //                               partyID i corresponds to lst[i].mapIdx
};

bool customCompare(const SortListItem &a, const SortListItem &b) {
    return a.score < b.score;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    int maxFormulas = min(k,1<<m);

    unordered_map<string,int> formulaMap;  // formula key -> formula ID
    pair<int, int> partyMoves[k];  // move number -> (formula ID, step)
    SortListItem *sortLists = new SortListItem[maxFormulas*n];  // formula ID -> party ID -> (score, mapped partyID, mapped index)
    // NOTE: sortLists is allocated on the heap instead of the stack since it can be huge

    // Fill in formulaMap and partyMoves : O(k)
    int formulaID, step, nextFormulaID = 0;
    string formula, formulaKey;
    for (int moveID = 0; moveID < k; moveID++) {
        cin >> formula >> step;
        formulaKey = formulaVars(formula);
        
        auto result = formulaMap.emplace(formulaKey, nextFormulaID);
        formulaID = result.first->second;
        if (result.second)
            nextFormulaID++;

        partyMoves[moveID] = pair<int,int>(formulaID, step);
    }

    // Fill in sortLists : O(n * m * min(k, 2^m)); if naive, O(n * m * k)
    int partyScores[m];
    int score, scoreIDx, formulaLen;
    unordered_map<string, int>::iterator it;
    for (int partyID = 0; partyID < n; partyID++) {
        DBG("DBG: ");
        for (int i = 0; i < m; i++) {
            cin >> partyScores[i];
            DBG(partyScores[i] << " ");
        }
        DBG(endl);
        for (it = formulaMap.begin(); it != formulaMap.end(); it++) {
            tie(formulaKey, formulaID) = *it;
            formulaLen = formulaKey.length();
            
            score = 0;
            DBG(" > ");
            for (int i = 0; i < formulaLen; i++) {
                scoreIDx = (formulaKey[i] - 'a');
                score += partyScores[scoreIDx];
                DBG(partyScores[scoreIDx] << " [" << formulaKey[i] << ":" << scoreIDx << "] * ");
            }
            DBG(" = " << score << endl);

            sortLists[formulaID*n+partyID] = SortListItem {score, partyID, 0};
        }
        DBG(endl);
    }

    // Sort each row and assign inverse map : O(min(k, 2^m) * n log n); if naive, O(k * n log n)
    int partyID;
    for (it = formulaMap.begin(); it != formulaMap.end(); it++) {
        formulaID = it->second;
        stable_sort(sortLists + formulaID*n, sortLists + (formulaID+1)*n, customCompare);

        // Assign inverse map
        for (int idx = 0; idx < n; idx++) {
            partyID = sortLists[formulaID*n+idx].mapPartyID;
            sortLists[formulaID*n+partyID].mapIdx = idx;
        }
    }

    #ifdef DEBUG
    cout << "formulaMap" << endl;
    for (unordered_map<string, int>::iterator it = formulaMap.begin(); it != formulaMap.end(); it++) {
        cout << "  " << it->first << " : " << it->second << endl;
    }
    cout << endl << "sortLists" << endl;
    for (int formulaID = 0; formulaID < formulaMap.size(); formulaID++) {
        for (int partyID = 0; partyID < n; partyID++) {
            cout << sortLists[formulaID*n+partyID].score << "," << sortLists[formulaID*n+partyID].mapPartyID << "," << sortLists[formulaID*n+partyID].mapIdx << "  \t";
        }
        cout << endl;
    }
    cout << endl;
    #endif

    // Iterate through moves
    partyID = 0;
    int partyIdx;
    for (int moveID = 0; moveID < k; moveID++) {
        tie(formulaID, step) = partyMoves[moveID];
        partyIdx = sortLists[formulaID*n+partyID].mapIdx;  // Get index in current sort list
        partyIdx = (partyIdx + step) % n;  // Move by step within sort list
        partyID = sortLists[formulaID*n+partyIdx].mapPartyID;  // Convert index back to partyID
        DBG(moveID << " > " << partyID << endl);
    }
    DBG(endl);

    cout << partyID << endl;
    delete sortLists;
}