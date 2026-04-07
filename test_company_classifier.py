"""
File: test_company_classifier.py

Description:
This file tests the classification logic on sample companies.
(Simulating database testing – Day 12)
"""

from company_classifier import classify_from_job_description

job_samples = [
    "We are hiring data entry operators for manual Excel reporting and tracking.",
    "Looking for software engineer with Python and React experience.",
    "Back office executive required for manual coordination and reporting.",
]

for i, job in enumerate(job_samples):
    result = classify_from_job_description(job)
    print(f"Job {i+1}: {result}")
