Given a sorted integer array where the range of elements are `[lower, upper]` inclusive, return its missing ranges. For example, given `[0, 1, 3, 50, 75], lower = 0, upper = 99`, return `[“2”, “4->49”, “51->74”, “76->99”]`.

Example Questions Candidate Might Ask:

* Q: What if the given array is empty?
* A: Then you should return [“0->99”] as those ranges are missing.
* Q: What if the given array contains all elements from the ranges?
* A: Return an empty list, which means no range is missing.