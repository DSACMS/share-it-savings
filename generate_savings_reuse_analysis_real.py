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
annual_it_spend = 2800000000  # $2.8B annual IT spending
development_budget = 700000000  # $700M development budget (25%)
reuse_rates = [0.01, 0.05, 0.10]
efficiency_factor = 0.8


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


def calculate_reuse_savings(dev_budget, rates, efficiency=0.8):
    """Calculate potential savings from code reuse"""
    savings = []
    for rate in rates:
        savings.append(dev_budget * rate * efficiency)

    return savings

# Generate metadata savings data
time_saved, cost_saved = calculate_metadata_savings(total_repositories, years_to_project)

# Generate reuse savings data
reuse_savings = calculate_reuse_savings(development_budget, reuse_rates)

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# Time Savings Plot
ax1.bar(years_to_project, time_saved, color='blue', alpha=0.6)
ax1.set_title('Metadata Automation: Time Saved for Reuse', fontsize=9)
ax1.set_xlabel('Years', fontsize=8)
ax1.set_ylabel('Hours Saved', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='both', which='major', labelsize=8)

# Metadata Cost Savings Plot
ax2.bar(years_to_project, cost_saved, color='green', alpha=0.6)
ax2.set_title('Metadata Automation: Cost Savings for Reuse', fontsize=9)
ax2.set_xlabel('Years', fontsize=8)
ax2.set_ylabel('Dollars Saved ($)', fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

# Code Reuse Savings Plot
reuse_labels = ['1%', '5%', '10%']
ax3.bar(reuse_labels, reuse_savings, color='purple', alpha=0.6)
ax3.set_title('Annual Code Reuse Savings Potential', fontsize=9)
ax3.set_xlabel('Reuse Percentage', fontsize=8)
ax3.set_ylabel('Dollars Saved ($)', fontsize=8)
ax3.grid(True, alpha=0.3)
ax3.tick_params(axis='both', which='major', labelsize=8)
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

plt.tight_layout()

# Save plots
plt.savefig('reuse_savings_analysis_real.png', dpi=300, bbox_inches='tight')

# Print calculated values
print("\nMetadata Automation Savings:")
for i, year in enumerate(years_to_project):
    print(f"{year} Year(s): {time_saved[i]:,} hours (${cost_saved[i]:,})")

print("\nCode Reuse Potential Savings:")
print(f"Based on ${development_budget:,.2f} development budget:")

for rate, saving in zip(reuse_labels, reuse_savings):
    print(f"At {rate} reuse: ${saving:,.2f}")
