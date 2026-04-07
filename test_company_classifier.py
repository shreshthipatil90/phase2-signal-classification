"""
File: test_company_classifier.py

Description:
This file tests the classification logic on sample companies.
(Simulating database testing – Day 12)
"""

from company_classifier import classify_company

# Sample test data (simulating company signals)
test_companies = [
    {"manual_roles": 6, "manual_keywords": 4, "scaling": True},
    {"manual_roles": 2, "manual_keywords": 1, "scaling": False},
    {"manual_roles": 4, "manual_keywords": 2, "scaling": False},
    {"manual_roles": 1, "manual_keywords": 0, "scaling": False},
    {"manual_roles": 5, "manual_keywords": 3, "scaling": True},
]

# Run tests
for i, signals in enumerate(test_companies):
    result = classify_company(signals)
    print(f"Company {i+1}: {result}")
