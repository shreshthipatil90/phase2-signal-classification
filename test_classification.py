
from classification import classify_company

test_data = [
    {"manual_roles": 6, "manual_keywords": 4, "scaling": True},
    {"manual_roles": 1, "manual_keywords": 0, "scaling": False},
    {"manual_roles": 3, "manual_keywords": 2, "scaling": False},
    {"manual_roles": 0, "manual_keywords": 1, "scaling": False},
    {"manual_roles": 5, "manual_keywords": 3, "scaling": False},
]

for i, company in enumerate(test_data):
    result = classify_company(company)
    print(f"Company {i+1}: {result}")
