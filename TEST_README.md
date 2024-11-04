## Overview
This document provides a comprehensive description of the testing framework and approach used to validate the `Library System` project. The test cases are developed using the `unittest` module in Python, which is a standard testing library that offers a robust structure for creating and running test cases.

## Testing Framework
### 1. `unittest` Module
The `unittest` module was chosen as the primary testing resource for this project for several reasons:
   - **Standardization**: `unittest` is part of Python’s standard library, making it highly reliable and compatible with most Python environments.
   - **Ease of Use**: The module provides clear methods (`setUp`, `tearDown`, `assertTrue`, `assertEqual`, etc.) that facilitate writing clear and effective test cases.
   - **Comprehensive Assertions**: `unittest` offers a wide range of assertions to validate conditions, making it versatile for various testing scenarios.
   - **Readability**: By using `unittest`, each test case remains modular and easy to read, which is ideal for expanding or debugging as the project grows.

Using `unittest` also allows us to automate the testing process, run tests in batches, and gather comprehensive insights into the success or failure of each case.

## Test Case Justification
The test cases are designed to cover the primary functionalities and edge cases of the Library System. Each test case was created based on user stories and system requirements, ensuring that the system meets expected behaviors under typical and atypical conditions. Here’s a breakdown:

1. **Valid Book Borrowing**: Verifies that users can successfully borrow a book and that the system correctly updates the book's availability status.
   - **Resource Justification**: This test is essential to validate the `borrow_book` method, ensuring that the book status is accurately tracked when borrowed.

2. **Invalid Book Borrowing**: Ensures that users cannot borrow a book that is already borrowed by another user.
   - **Resource Justification**: This test handles the case where a book’s availability status is already marked as borrowed, testing that duplicate borrowing requests are gracefully denied.

3. **Valid Book Returning**: Checks that users can return a book they’ve borrowed, updating its availability status.
   - **Resource Justification**: This test verifies that the `return_book` method correctly restores the book’s availability, supporting the integrity of borrowing and returning workflows.

4. **Invalid Book Returning**: Ensures that users cannot return a book that was not borrowed, verifying that no unintended changes occur to the book’s availability.
   - **Resource Justification**: By testing this, we ensure that the system accurately tracks the borrow/return status, preventing users from returning unborrowed books.

5. **Admin Adding Books**: Validates that the admin can add new books, and these books appear in the library’s collection.
   - **Resource Justification**: Testing this is crucial to confirm that the `add_book` functionality works as expected, ensuring the library can be dynamically updated with new titles.

6. **Boundary Case (Borrowing All Books)**: Confirms that when all books are borrowed, their status is updated accordingly, covering a boundary scenario.
   - **Resource Justification**: This test is essential for validating that the system can handle situations where all resources are in use, ensuring robustness.

7. **Edge Case (Returning Unborrowed Book)**: Ensures that attempting to return a book that has not been borrowed does not impact its availability.
   - **Resource Justification**: This edge case checks the system’s resilience, ensuring unborrowed items remain correctly available.

## Running the Tests
1. **Setup**: Ensure you have Python installed. The tests are written to run in any standard Python environment.
2. **Execution**: To execute the tests, navigate to the project directory in the terminal and run:
   ```bash
   python -m unittest