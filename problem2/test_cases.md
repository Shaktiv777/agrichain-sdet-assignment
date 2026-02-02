# Problem 2 – Test Cases for Agrichain Website

## Feature
Find the length of the longest substring without repeating characters.

## Assumptions
- Homepage has an input textbox and Submit button
- On submit, user is navigated to a result page
- Result page displays the calculated length
- Element locators are assumed

---

## Manual Test Cases

### TC-M-01
**Title:** Verify homepage loads successfully  
**Steps:**  
1. Open browser  
2. Navigate to https://agrichain.com  
**Expected Result:**  
Homepage loads with input textbox and Submit button visible.

---

### TC-M-02
**Title:** Verify input field accepts text  
**Steps:**  
1. Click on input field  
2. Enter a valid string  
**Expected Result:**  
User is able to enter text.

---

### TC-M-03
**Title:** Verify Submit button functionality  
**Steps:**  
1. Enter valid input  
2. Click Submit  
**Expected Result:**  
User is navigated to result page.

---

### TC-M-04
**Title:** Verify empty input validation  
**Steps:**  
1. Leave input empty  
2. Click Submit  
**Expected Result:**  
Validation message is displayed.

---

### TC-M-05
**Title:** Verify special character input  
**Steps:**  
1. Enter special characters  
2. Click Submit  
**Expected Result:**  
Input is accepted and processed.

---

### TC-M-06
**Title:** Verify browser back navigation  
**Steps:**  
1. Submit valid input  
2. Click browser back  
**Expected Result:**  
User returns to homepage without error.

---

## Automation Test Cases

### TC-A-01
**Title:** Verify correct output for valid input  
**Input:** abcabcbb  
**Expected Output:** 3

---

### TC-A-02
**Title:** Verify output for repeating characters  
**Input:** bbbbb  
**Expected Output:** 1

---

### TC-A-03
**Title:** Verify numeric input  
**Input:** 123451  
**Expected Output:** 5

---

### TC-A-04
**Title:** Verify alphanumeric input  
**Input:** a1b2c3  
**Expected Output:** 6

---

### TC-A-05
**Title:** Verify special character input  
**Input:** @#@!  
**Expected Output:** 2

---

## Notes
- Manual test cases focus on UI and exploratory testing  
- Automation test cases focus on functional and regression coverage