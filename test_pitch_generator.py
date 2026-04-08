from pitch_generator import generate_pitch

test_companies = [
    ("XYZ Logistics", ["data entry", "manual reporting"], 85),
    ("ABC Retail", ["excel tracking", "back office work"], 70),
    ("TechSoft", ["software development"], 40),
]

for company, signals, score in test_companies:
    print("="*50)
    print(generate_pitch(company, signals, score))
