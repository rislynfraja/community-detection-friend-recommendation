# Community Detection & Friend Recommendation
### Honors Project for CSE 3500 - Algorithms & Complexity

---
 
## What It Does
 
### `community-detection.py`
Implements the **Girvan-Newman algorithm** to split a weighted social graph into strong communities. It works by repeatedly removing the edge with the highest *betweenness centrality* (the edge most frequently on shortest paths between any two nodes) until the graph splits into groups with more internal connections than external ones. The result is visualized using NetworkX and Matplotlib.
 
### `friend-recommendation.py`
Implements a friend recommendation system inspired by **FRUTAI** (Friend Recommendation Using a User's Total Attributes Information). Each user is assigned random candidates, and candidates are ranked using a score based on:
- Jaccard-similarity-weighted gender match
- Jaccard-similarity-weighted location match
- Number of mutual friends
Users already in a person's friend list are automatically excluded from recommendations.

---
 
## Files
 
| File | Description |
|---|---|
| `community-detection.py` | Girvan-Newman community detection on a 34-node test graph |
| `friend-recommendation.py` | FRUTAI-based friend ranking for a 347-user social network |
 
---

## Requirements
 
```
networkx
matplotlib
numpy
```
 
Install with:
```bash
pip install networkx matplotlib numpy
```
 
---

## How to Run
 
**Community Detection:**
```bash
python community-detection.py
```
A graph visualization will pop up showing the detected communities. The test data uses a 34-node weighted graph. To use your own data, modify the `vertices` and `edges` lists at the bottom of the file. Edges are formatted as `(user_a, user_b, weight)`.
 
**Friend Recommendation:**
```bash
python friend-recommendation.py
```
Prints each user's ranked candidate list to the terminal. To use your own data, define `user` objects with `(user_num, gender, location)` and add friends with `.add_friend()`.
 
---



