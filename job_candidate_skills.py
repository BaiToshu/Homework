job_requires={"Python", "Django", "SQL", "Git"}
candidate_skills={"Python", "Flask", "Git", "JavaScript"}
matching_skills= job_requires & candidate_skills
missing_skills=job_requires - candidate_skills
extra_skills=candidate_skills - job_requires

print(f"Matched Skills: {matching_skills}")
print(f"Missing Skills: {missing_skills}")
print(f"Extra Skills: {extra_skills}")

