# Load the report
report_path = 'Research_Report_Data_Mining_Techniques.md'

# Read the existing content
with open(report_path, 'r') as file:
    content = file.readlines()

# Prepare the new content for Results section
results_section = "## Results\n\n"
results_section += "![Yield Strength vs. Difference in Lattice Constants](yield_strength_vs_diff_lattice_constants.png)\n"
results_section += "This scatter plot illustrates the relationship between the difference in lattice constants and the yield strength of various alloys. A trend can be observed, indicating how variations in lattice constants may influence the mechanical properties of the alloys.\n\n"
results_section += "![Distribution of Yield Strength](yield_strength_distribution.png)\n"
results_section += "The histogram shows the frequency distribution of yield strength values across different alloys. This visualization helps identify the most common yield strength ranges and can highlight any outliers or trends in the data.\n\n"

# Update the content
for i, line in enumerate(content):
    if line.startswith('## Results'):
        content[i:i+1] = [results_section]  # Replace the Results section
        break

# Write the updated content back to the report
with open(report_path, 'w') as file:
    file.writelines(content)