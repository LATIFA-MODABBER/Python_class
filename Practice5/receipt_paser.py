import re
import json


def parse_receipt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Extract all prices

    price_pattern = r"\b\d{1,3}(?:,\d{3})*\.\d{2}\b"
    prices = re.findall(price_pattern, text)

    # Convert prices to floats
    price_values = [float(price.replace(",", "")) for price in prices]

    # Extract product names

    product_pattern = re.compile(
        r'^\d+\.\s*\n?(.+?)\n\s*\d+\s*[x×]',
        re.MULTILINE
    )

    products = [p.strip() for p in product_pattern.findall(text)]


    # Calculate total amount

    total_match = re.search(r"total:\s*([\d,]+\.\d{2})", text, re.IGNORECASE)

    if total_match:
        total_amount = float(total_match.group(1).replace(",", ""))
    else:
        total_amount = None


    # Extract date and time

    datetime_pattern = r"(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})"
    datetime_match = re.search(datetime_pattern, text)

    if datetime_match:
        date = datetime_match.group(1)
        time = datetime_match.group(2)
    else:
        date = None
        time = None


    # Extract payment method

    payment_match = re.search(r"(bank card|cash)", text, re.IGNORECASE)

    if payment_match:
        payment_method = payment_match.group(1).lower()
    else:
        payment_method = None


    # Create structured output

    data = {
        "products": products,
        "prices": price_values,
        "total_amount": total_amount,
        "date": date,
        "time": time,
        "payment_method": payment_method
    }

    return data


def main():
    receipt = parse_receipt("raw.txt")

    print("\nParsed Receipt")
    print("-" * 40)
    print(json.dumps(receipt, indent=4, ensure_ascii=False))

    with open("parsed_receipt.json", "w", encoding="utf-8") as f:
        json.dump(receipt, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()


