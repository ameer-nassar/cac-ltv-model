# Plot 2: LTV vs CAC by channel

plt.figure(figsize=(8,5))
plt.bar(ltv_cac["acquisition_channel"], ltv_cac["ltv"], color='teal', label="LTV")
plt.bar(ltv_cac["acquisition_channel"], ltv_cac["marketing_spend"], color='orange', label="CAC")

plt.title("LTV vs CAC by Acquisition Channel")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()

plt.savefig("plot2_ltv_vs_cac.png", dpi=300, bbox_inches='tight')
plt.close()