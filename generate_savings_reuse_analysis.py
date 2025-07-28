# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2025 Contributors to the CMS Knowledge Management Platform and Open Source Program Office
# This work is dedicated to the public domain under Creative Commons Zero 1.0 Universal


import matplotlib.pyplot as plt
import numpy as np


# Input variables for metadata automation
total_repositories = 10000
automated_percentage = 0.80
manual_time_minutes = 60  # Original manual time per repo
automated_time_minutes = 2  # Average automated processing time
manual_portion_time_minutes = 10  # Time for manual portion after automation
hourly_rate = 80  # Cost per hour
years_to_project = [1, 5, 10]


# Input variables for code reuse
avg_project_cost = 1000000  # $1M per project
num_projects = 100          # Number of new projects per year
reuse_rates = [0.10, 0.25, 0.50]
efficiency_factor = 0.8     # Adjustment for reuse implementation effort


def calculate_metadata_savings(repos, years):
    """Calculate time and cost savings for metadata automation"""
    # Original manual process time (in hours)
    original_time = (repos * manual_time_minutes) / 60

    # New process time (in hours)
    automated_repos = repos * automated_percentage
    manual_repos = repos * (1 - automated_percentage)
    new_time = (automated_repos * automated_time_minutes + 
                manual_repos * manual_portion_time_minutes) / 60

    # Calculate savings for each year
    time_saved = [int((original_time - new_time) * year) for year in years]
    cost_saved = [int(t * hourly_rate) for t in time_saved]

    return time_saved, cost_saved


def calculate_reuse_savings(avg_cost, num_proj, rates, efficiency=0.8):
    """Calculate potential savings from code reuse"""
    annual_spend = avg_cost * num_proj
    savings = []
    for rate in rates:
        savings.append(annual_spend * rate * efficiency)

    return annual_spend, savings

# Generate metadata savings data
time_saved, cost_saved = calculate_metadata_savings(total_repositories, years_to_project)

# Generate reuse savings data
annual_spend, reuse_savings = calculate_reuse_savings(avg_project_cost, num_projects, reuse_rates)

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3))

# Time Savings Plot
ax1.bar(years_to_project, time_saved, color='blue', alpha=0.6)
ax1.set_title('Metadata: Time Saved by Period', fontsize=9)
ax1.set_xlabel('Years', fontsize=8)
ax1.set_ylabel('Hours Saved', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='both', which='major', labelsize=8)


# Cost Savings Plot
ax2.bar(years_to_project, cost_saved, color='green', alpha=0.6)
ax2.set_title('Metadata: Cost Savings', fontsize=9)
ax2.set_xlabel('Years', fontsize=8)
ax2.set_ylabel('Dollars Saved ($)', fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))


# Reuse Savings Plot
reuse_labels = ['10%', '25%', '50%']
ax3.bar(reuse_labels, reuse_savings, color='purple', alpha=0.6)
ax3.set_title('Code Reuse Savings', fontsize=9)
ax3.set_xlabel('Reuse Percentage', fontsize=8)
ax3.set_ylabel('Dollars Saved ($)', fontsize=8)
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='both', which='major', labelsize=8)
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

plt.tight_layout()


# Save plots
plt.savefig('combined_savings_reuse_plots.png', dpi=300, bbox_inches='tight')

# Print calculated values
print("\nMetadata Automation Savings:")

for i, year in enumerate(years_to_project):
    print(f"{year} Year(s): {time_saved[i]:,} hours (${cost_saved[i]:,})")

print("\nCode Reuse Potential Savings:")
print(f"Annual IT Spend: ${annual_spend:,.2f}")
for rate, saving in zip(reuse_labels, reuse_savings):
    print(f"At {rate} reuse: ${saving:,.2f}")
