#include <iostream>
#include <iterator>
#include <list>
#include <unordered_map>

using namespace std;

list<int>::iterator forward(list<int> &orig, list<int>::iterator curr, int num) {
  if (num == 0) {
    return curr;
  }
  if (curr == prev(orig.end())) {
    return forward(orig, orig.begin(), num - 1);
  }
  return forward(orig, next(curr), num - 1);
}

list<int>::iterator back(list<int> &orig, list<int>::iterator curr, int num) {
  if (num == 0) {
    return curr;
  }
  if (curr == orig.begin()) {
    return back(orig, prev(orig.end()), num - 1);
  }
  return back(orig, prev(curr), num - 1);
}

int main() {
  int players = 425;
  int last_marble = 7084800;

  list<int> marbles;
  marbles.push_back(0);
  list<int>::iterator curr = marbles.begin();
  int lowest_marble = 1;
  int curr_player = 0;
  unordered_map<int, long> scores;

  while (lowest_marble <= last_marble) {
    if (lowest_marble % 23 == 0) {
      scores[curr_player] += lowest_marble;
      curr = back(marbles, curr, 7);
      scores[curr_player] += *curr;
      curr = marbles.erase(curr);
    } else {
      curr = forward(marbles, curr, 2);
      if (curr == marbles.begin()) {
        marbles.push_back(lowest_marble);
      } else {
        marbles.insert(curr, lowest_marble);
      }
      curr = back(marbles, curr, 1);
    }
    curr_player = (curr_player + 1) % players;
    lowest_marble++;
  }

  long max_score = 0;
  for (const auto& score : scores) {
    if (score.second > max_score) {
      max_score = score.second;
    }
  }
  cout << max_score << endl;
  return 0;
}
