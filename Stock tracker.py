import csv   # only used if you choose to save as CSV

# ------------ 1. Hard‑coded stock prices ------------
prices = {
    "TATA": 400,
    "HDFC": 220,
    "REL": 420,
    "GOOGLE": 160,
    "AMAZON": 190
}

# ------------ 2. Gather user portfolio ------------
portfolio = {}          # {symbol: quantity}
print("📈  Simple Stock Tracker")
print("Enter one stock per line in the format  SYMBOL  QUANTITY")
print("Press Enter on an empty line when you’re done.\n")

while True:
    line = input("Stock (or hit Enter to finish): ").strip().upper()
    if not line:
        break
    try:
        symbol, qty = line.split()
        qty = int(qty)
        if symbol not in prices:
            print("  ⚠️  Symbol not in price list — try again.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    except ValueError:
        print("  ⚠️  Please type:  SYMBOL  QUANTITY (e.g. AAPL 5)")

# ------------ 3. Compute totals ------------
total_value = 0
print("\nYour Holdings:")
for sym, qty in portfolio.items():
    value = prices[sym] * qty
    total_value += value
    print(f"  {sym:<5}  x{qty:<4} @ ${prices[sym]:>6}  = ${value:,.2f}")

print(f"\n💰  Total investment value: ${total_value:,.2f}")

# ------------ 4. Optional: save to file ------------
save = input("\nSave results to a file? (y/n): ").strip().lower()
if save == "y":
    fmt = input("Choose format — txt or csv: ").strip().lower()
    if fmt == "txt":
        fname = "portfolio_summary.txt"
        with open(fname, "w") as f:
            for sym, qty in portfolio.items():
                f.write(f"{sym} {qty} {prices[sym]} {prices[sym]*qty}\n")
            f.write(f"TOTAL {total_value}\n")
    elif fmt == "csv":
        fname = "portfolio_summary.csv"
        with open(fname, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for sym, qty in portfolio.items():
                writer.writerow([sym, qty, prices[sym], prices[sym]*qty])
            writer.writerow(["TOTAL", "", "", total_value])
    else:
        print("Unknown format — skipped saving.")
        fname = None

    if fmt in {"txt", "csv"}:
        print(f"✅  Saved to {fname}")
else:
    print("Okay, not saved. Goodbye!")
