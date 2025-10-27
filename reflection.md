1. Easiest and Hardest Issues to Fix? Why?
The easiest fixes were cosmetic issues like trailing whitespace and unused imports, as these just involved simple deletion or formatting changes. The hardest fixes involved architectural changes, such as resolving the mutable default argument in add_item and enforcing full snake_case naming, which required updating logic and function calls throughout the code.

2. Did the Static Analysis Tools Report Any False Positives?
Yes, static analysis tools often report subjective issues that can be considered false positives for simple scripts. A primary example is the Pylint warning W0603 regarding the use of the global stock_data statement in load_data. While generally discouraged, using a global variable is the necessary and simplest pattern for maintaining the central inventory state in this small, single-module application.

3. How to Integrate Static Analysis Tools into Your Workflow?
I'd integrate them into both the local environment and the CI pipeline. Locally, I'd use IDE extensions to run Pylint and Flake8 on save, providing immediate feedback. In the CI/CD pipeline, I'd enforce a mandatory check using Bandit (for security) and Pylint/Flake8, blocking any code merge if the quality score drops below a set threshold (e.g., 9/10).

4. Tangible Improvements Observed in the Code?
The code is now significantly more robust because input validation prevents runtime crashes from bad data, and the specific exception handling prevents error masking. It is also more readable due to consistent snake_case naming and the addition of comprehensive docstrings, which greatly improves maintainability.