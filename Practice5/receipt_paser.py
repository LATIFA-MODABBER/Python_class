import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

receipt_no = re.search(r"Receipt No\.\s*(\d+)", text)

prices = re.findall(r"=\s*([\d,]+\.\d+)", text)
prices = [float(price.replace(",", "")) for price in prices]

total = re.search(r"TOTAL:\s*([\d,]+\.\d+)", text)

payment = re.search(r"(Bank card):\s*([\d,]+\.\d+)", text)

datetime = re.search(
    r"(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
    text
)

products = re.findall(
    r"\d+\.\s(.+?)\n\s+\d+\.\d+\s*x",
    text
)

print("Receipt Number:", receipt_no.group(1))
print("Date:", datetime.group(1))
print("Time:", datetime.group(2))
print("Payment Method:", payment.group(1))
print("Total:", total.group(1))
print("Calculated Total:", sum(prices))

print("\nProducts:")
for product in products:
    print("-", product)