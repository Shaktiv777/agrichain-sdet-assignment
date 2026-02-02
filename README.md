# Agrichain SDET Assignment

This repository contains my solution for the SDET assignment shared as part of the recruitment process.

The assignment evaluates:
- Problem-solving and coding skills
- Test case design and categorization
- Web automation thinking for a hypothetical application

---

## Problem 1: Longest Substring Without Repeating Characters

### Problem Statement
Given a string, find the length of the longest substring without repeating characters.

**Examples:**
- Input: `abcabcbb` → Output: `3`
- Input: `bbbbb` → Output: `1`

---

### Approach
- Implemented using the sliding window technique.
- Two pointers maintain a window of unique characters.
- A set is used to track characters currently in the window.
- The window expands until a duplicate character is found, then shrinks until the duplicate is removed.

---

### Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(min(n, character set size))

---

### Implementation Location
```
problem1/longest_substring.py
```

---

## Problem 2: Website Testing and Automation

### Problem Description
Assume a website that:
- Accepts a string input on the homepage
- Processes the input on clicking a Submit button
- Navigates to a result page
- Displays the length of the longest substring without repeating characters

As mentioned in the assignment, **there is no actual website**.

---

## Test Case Design

### Manual Test Cases
Manual test cases focus on:
- UI validation
- Input handling
- Navigation behavior
- User experience scenarios

---

### Automation Test Cases
Automation test cases focus on:
- Functional correctness
- Regression scenarios
- Valid and invalid input combinations

All test cases are clearly documented and categorized.

---

### Test Case Documentation Location
```
problem2/test_cases.md
```

---

## Automation Approach

- Selenium with Python is used for web automation.
- Page Object Model (POM) is followed to separate test logic from UI locators.
- Web element locators are assumed based on expected UI behavior.

---

### Automation Framework Structure
```
problem2/automation/
├── pages/
├── tests/
├── utils/
└── config/
```

---

## Assumptions

- The website is hypothetical as stated in the assignment.
- All web element locators are assumed based on expected UI behavior.
- Automation code demonstrates structure and approach rather than execution against a real environment.

---

## Tech Stack

- Python 3
- Selenium WebDriver
- Page Object Model (POM)

---

## How to Run

### Run Problem 1
```bash
python problem1/longest_substring.py
```

### Run Problem 2 (Automation)
```bash
python problem2/automation/tests/test_longest_substring.py
```

---

## Conclusion

This assignment demonstrates my approach to writing efficient code, designing comprehensive test cases, and structuring automation frameworks for hypothetical applications.
