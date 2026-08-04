from app.services.psx_service import PSXService

psx = PSXService()

# ------------------------
# Companies
# ------------------------
companies = psx.get_symbols()

print(f"Companies: {len(companies)}")
print(companies[:5])

# ------------------------
# Market Watch
# ------------------------
market = psx.get_market_watch()

print(f"\nMarket Watch Stocks: {len(market)}")
print(market[:3])

# ------------------------
# Top Performers (still HTML)
# ------------------------
performers = psx.get_top_performers()

print("\nTop Active")
print(performers["top_active"][:3])

print("\nTop Gainers")
print(performers["top_gainers"][:3])

print("\nTop Losers")
print(performers["top_losers"][:3])

# ------------------------
# KSE100 Chart
# ------------------------
chart = psx.get_kse100_chart()

print("\nKSE100 Chart:")
print(chart)