import csv
from collections import defaultdict

def check_k_anonymity(data, q, k):
    try:
        # Group records based on quasi-identifiers
        group_dict = defaultdict(list)
        for record in data:
            q_values = tuple(record[i] for i in range(q))
            group_dict[q_values].append(record)

        # Check for k-anonymity violations
        violations = []
        for q_values, group in group_dict.items():
            if len(group) < k:
                violations.append(q_values)

        if not violations:
            print(f"The dataset satisfies k-anonymity with k = {k}.")
            return True, []
        else:
            print(f"The dataset violates k-anonymity with k = {k}.")
            return False, violations
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, []

# Example usage:
file_path = "KAnonymityDataset.csv"
k = 2

# Read the dataset
data = []
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Skip header row
    for row in csv_reader:
        data.append(row[1:9])

#Removing quasi-identifiers: Attrition_Flag, Gender
for i in data:
    i.pop(0)
    i.pop(1)

#Generalizing Data: 
# Age: Place into ranges
# Dependent count: Generalize to greater than or less than 2
# Education Level: Generalized to above high school, or at or below high school
# Marital Status: Generalize to married or not married or unknown
# Income Category: Generalize to either above or below 60k
# Card Category: Generalize to either above blue or blue
for i in data:
    if (int)(i[0]) < 35:
        i[0] = "<35"
    elif (int)(i[0]) >= 35 and (int)(i[0]) <= 50:
        i[0] = "35-50"
    elif (int)(i[0]) > 50:
        i[0] = ">50"
    
    if (int)(i[1]) > 2:
        i[1] = ">2"
    else:
        i[1] = "<2"
        
    if i[2] != "High School" and i[2] != "Uneducated" and i[2] != "Unknown":
        i[2] = "Above High School"
    else:
        i[2] = "At or below High School or Unknown"
        
    if i[3] != "Married":
        i[3] = "Not Married or Unknown"
    
    if i[4] != "$60K - $80K" or i[4] != "$80K - $120K" or i[4] != "$120K +":
        i[4] = "Less than $60K or Unknown"
    else:
        i[4] = "Greater than $60K"
        
    if i[5] != "Blue":
        i[5] = "Above Blue"

print(data[0])
# print(len(data))

is_anonymous, violations = check_k_anonymity(data, 6, k)

# for i in violations:
#     print(i)
print(len(violations))